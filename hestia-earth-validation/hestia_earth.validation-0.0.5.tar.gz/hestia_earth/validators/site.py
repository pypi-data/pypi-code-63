from typing import List
from functools import reduce

from hestia_earth.geojson import get_geojson_area
from .shared import list_has_props, validate_dates, validate_list_dates, validate_list_duplicated, diff_in_years


SOIL_TEXTURE_IDS = ['sandContent', 'siltContent', 'clayContent']


def group_measurements_depth(measurements: List[dict]):
    def group_by(group: dict, measurement: dict):
        key = measurement['depthUpper'] + measurement['depthLower'] \
            if 'depthUpper' in measurement and 'depthLower' in measurement else 'default'
        if key not in group:
            group[key] = []
        group[key].extend([measurement])
        return group

    return reduce(group_by, measurements, {})


def validate_soilTexture(measurements: List[dict]):
    def validate(values):
        values = list(filter(lambda v: v['term']['@id'] in SOIL_TEXTURE_IDS, values))
        terms = list(map(lambda v: v['term']['@id'], values))
        return len(set(terms)) != len(SOIL_TEXTURE_IDS) or 99.5 < sum(map(lambda v: v['value'], values)) < 100.5 or {
            'level': 'error',
            'dataPath': '.measurements',
            'message': 'The sum of Sand, Silt, and Clay content should equal 100% for each soil depth interval.'
        }

    results = list(map(validate, group_measurements_depth(measurements).values()))
    return next((x for x in results if x is not True), True)


def validate_depths(measurements: List[dict]):
    def validate(values):
        measurement = values[1]
        index = values[0]
        return measurement['depthUpper'] < measurement['depthLower'] or {
            'level': 'error',
            'dataPath': f".measurements[{index}].depthLower",
            'message': 'must be greater than depthUpper'
        }

    results = list(map(validate, enumerate(list_has_props(measurements, ['depthUpper', 'depthLower']))))
    return next((x for x in results if x is not True), True)


def validate_lifespan(infrastructure: List[dict]):
    def validate(values):
        value = values[1]
        index = values[0]
        lifespan = diff_in_years(value.get('startDate'), value.get('endDate'))
        return lifespan == round(value.get('lifespan'), 1) or {
            'level': 'error',
            'dataPath': f".infrastructure[{index}].lifespan",
            'message': f"must equal to endDate - startDate in decimal years (~{lifespan})"
        }

    results = list(map(validate, enumerate(list_has_props(infrastructure, ['lifespan', 'startDate', 'endDate']))))
    return next((x for x in results if x is not True), True)


def validate_site_dates(site: dict):
    return validate_dates(site) or {
        'level': 'error',
        'dataPath': '.endDate',
        'message': 'must be greater than startDate'
    }


def validate_area(site: dict):
    try:
        area = get_geojson_area(site.get('boundary'))
        return area == round(site.get('area'), 1) or {
            'level': 'error',
            'dataPath': '.area',
            'message': f"must be equal to boundary (~{area})"
        }
    except KeyError:
        # if getting the geojson fails, the geojson format is invalid
        # and the schema validation step will detect it
        return True


def validate_site(site: dict):
    return [
        validate_site_dates(site),
        validate_area(site) if 'area' in site and 'boundary' in site else True
    ] + ([
        validate_list_dates(site, 'measurements'),
        validate_soilTexture(site['measurements']),
        validate_depths(site['measurements']),
        validate_list_duplicated(site, 'measurements', [
            'term.@id',
            'method.@id',
            'methodDescription',
            'startDate',
            'endDate',
            'depthUpper',
            'depthLower'
        ])
    ] if 'measurements' in site else []) + ([
        validate_list_dates(site, 'infrastructure'),
        validate_lifespan(site['infrastructure'])
    ] if 'infrastructure' in site else [])
