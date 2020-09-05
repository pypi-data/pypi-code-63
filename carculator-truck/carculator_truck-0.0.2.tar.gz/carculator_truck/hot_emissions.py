import numpy as np
import xarray
import pandas as pd
from . import DATA_DIR


def _(o):
    """Add a trailing dimension to make input arrays broadcast correctly"""
    if isinstance(o, (np.ndarray, xarray.DataArray)):
        return np.expand_dims(o, -1)
    else:
        return o


class HotEmissionsModel:
    """
    Calculate hot pollutants emissions based on HBEFA 4.1 data, function of speed (given by the driving cycle)
    for vehicles with a combustion engine.

    :param cycle: Driving cycle. Pandas Series of second-by-second speeds (km/h) or name (str)
        of cycle e.g., "Urban delivery", "Regional delivery", "Long haul".
    :type cycle: pandas.Series

    """

    def __init__(self, cycle, cycle_name):

        self.cycle = cycle
        self.cycle_name = cycle_name

        self.cycle_environment = {
            "Urban delivery": {"urban start": 0, "urban stop": -1},
            "Long haul": {"rural start": 0, "rural stop": -1},
            "Regional delivery": {
                "urban start": 0,
                "urban stop": 250,
                "suburban start": 251,
                "suburban stop": 750,
                "rural start": 751,
                "rural stop": -1,
            },
        }
        self.em = self.get_emission_factors()

    def get_emission_factors(self):
        fp = DATA_DIR / "HEM_factors_trucks.xlsx"
        ef = pd.read_excel(fp)
        return (
            ef.groupby(["powertrain", "euro_class", "size", "component"])
            .sum()
            .to_xarray()
        )

    def get_emissions_per_powertrain(
        self, powertrain_type, euro_classes, debug_mode=False
    ):
        """
        Calculate hot pollutants emissions given a powertrain type (i.e., diesel, CNG) and a EURO pollution class, per air sub-compartment
        (i.e., urban, suburban and rural).

        The emission sums are further divided into `air compartments`: urban, suburban and rural.


        :param powertrain_type: "diesel", or "CNG"
        :type powertrain_type: str
        :param euro_class: list of integers, corresponding to the EURO pollution class
        :type euro_class: list
        :return: Pollutants emission per km driven, per air compartment.
        :rtype: numpy.array
        """

        arr = self.em.sel(
            powertrain=powertrain_type,
            euro_class=euro_classes,
            size=["18t", "26t", "3.5t", "40t", "60t", "7.5t"],
            component=[
                "HC",
                "CO",
                "NOx",
                "PM",
                "NO2",
                "CH4",
                "NMHC",
                "SO2",
                "N2O",
                "NH3",
                "Benzene",
            ],
        ).transpose()

        cycle = self.cycle.reshape(-1, 1, 1, 6)

        a = arr["a"].values * cycle ** 3
        b = arr["b"].values * cycle ** 2
        c = arr["c"].values * cycle
        intercept = arr["intercept"].values

        em_arr = a + b + c + intercept

        if powertrain_type not in ("diesel", "CNG"):
            raise TypeError("The powertrain type is not valid.")

        if debug_mode == True:
            return em_arr

        # In case the fit produces negative numbers
        em_arr[em_arr < 0] = 0

        # If the driving cycle selected is one of the driving cycles for which carculator has specifications,
        # we use the driving cycle "official" road section types to compartmentalize emissions.
        # If the driving cycle selected is instead specified by the user (passed directly as an array), we used
        # speed levels to compartmentalize emissions.

        distance = self.cycle.sum(axis=0) / 3600

        if "urban start" in self.cycle_environment[self.cycle_name]:
            start = self.cycle_environment[self.cycle_name]["urban start"]
            stop = self.cycle_environment[self.cycle_name]["urban stop"]
            dist_urban = self.cycle[start:stop].sum(axis=0) / 3600
            urban = np.mean(em_arr[start:stop, :], axis=0) * (dist_urban / distance)
            urban /= 1000  # going from grams to kg

        else:
            urban = np.zeros((11, 6, 6))

        if "suburban start" in self.cycle_environment[self.cycle_name]:
            start = self.cycle_environment[self.cycle_name]["suburban start"]
            stop = self.cycle_environment[self.cycle_name]["suburban stop"]
            dist_suburban = self.cycle[start:stop].sum(axis=0) / 3600
            suburban = np.mean(em_arr[start:stop, :], axis=0) * (
                dist_suburban / distance
            )
            suburban /= 1000  # going from grams to kg

        else:
            suburban = np.zeros((11, 6, 6))

        if "rural start" in self.cycle_environment[self.cycle_name]:
            start = self.cycle_environment[self.cycle_name]["rural start"]
            stop = self.cycle_environment[self.cycle_name]["rural stop"]
            dist_rural = self.cycle[start:stop].sum(axis=0) / 3600
            rural = np.mean(em_arr[start:stop, :], axis=0) * (dist_rural / distance)
            rural /= 1000  # going from grams to kg

        else:
            rural = np.zeros((11, 6, 6))

        res = np.vstack((urban, suburban, rural)).transpose((1, 0, 2))

        if debug_mode == True:
            return (urban, suburban, rural)

        if powertrain_type=="diesel":
            return res[:, np.newaxis, :, :, np.newaxis]
        else:
            return res[..., np.newaxis]

