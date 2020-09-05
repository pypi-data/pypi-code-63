# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PermissionsRequest(Model):
    """PermissionsRequest.

    :param accounting_settings:
    :type accounting_settings:
     ~energycap.sdk.models.AccountingSettingsClassPermission
    :param accounts:
    :type accounts: ~energycap.sdk.models.AccountsClassPermission
    :param accounts_module:
    :type accounts_module: ~energycap.sdk.models.AccountsModuleClassPermission
    :param accrual_settings:
    :type accrual_settings:
     ~energycap.sdk.models.AccrualSettingsClassPermission
    :param cost_centers:
    :type cost_centers: ~energycap.sdk.models.CostCentersClassPermission
    :param move_accounts_between_vendors:
    :type move_accounts_between_vendors:
     ~energycap.sdk.models.MoveAccountsBetweenVendorsClassPermission
    :param application_settings:
    :type application_settings:
     ~energycap.sdk.models.ApplicationSettingsClassPermission
    :param approve_bills:
    :type approve_bills: ~energycap.sdk.models.ApproveBillsClassPermission
    :param bill_workflow_settings:
    :type bill_workflow_settings:
     ~energycap.sdk.models.BillWorkflowSettingsClassPermission
    :param bills_and_batches:
    :type bills_and_batches:
     ~energycap.sdk.models.BillsAndBatchesClassPermission
    :param export_bills:
    :type export_bills: ~energycap.sdk.models.ExportBillsClassPermission
    :param export_hold:
    :type export_hold: ~energycap.sdk.models.ExportHoldClassPermission
    :param move_existing_bills:
    :type move_existing_bills:
     ~energycap.sdk.models.MoveExistingBillsClassPermission
    :param shared_bill_lists:
    :type shared_bill_lists:
     ~energycap.sdk.models.SharedBillListsClassPermission
    :param unit_system_settings:
    :type unit_system_settings:
     ~energycap.sdk.models.UnitSystemSettingsClassPermission
    :param update_approved_bills:
    :type update_approved_bills:
     ~energycap.sdk.models.UpdateApprovedBillsClassPermission
    :param update_units_on_existing_bills:
    :type update_units_on_existing_bills:
     ~energycap.sdk.models.UpdateUnitsOnExistingBillsClassPermission
    :param budgets_and_budget_versions:
    :type budgets_and_budget_versions:
     ~energycap.sdk.models.BudgetsAndBudgetVersionsClassPermission
    :param chargebacks_module:
    :type chargebacks_module:
     ~energycap.sdk.models.ChargebacksModuleClassPermission
    :param chargebacks:
    :type chargebacks: ~energycap.sdk.models.ChargebacksClassPermission
    :param chargeback_reversals:
    :type chargeback_reversals:
     ~energycap.sdk.models.ChargebackReversalsClassPermission
    :param meter_savings_settings:
    :type meter_savings_settings:
     ~energycap.sdk.models.MeterSavingsSettingsClassPermission
    :param savings_adjustments:
    :type savings_adjustments:
     ~energycap.sdk.models.SavingsAdjustmentsClassPermission
    :param manually_adjust_savings:
    :type manually_adjust_savings:
     ~energycap.sdk.models.ManuallyAdjustSavingsClassPermission
    :param savings_engine:
    :type savings_engine: ~energycap.sdk.models.SavingsEngineClassPermission
    :param baseline_engine:
    :type baseline_engine: ~energycap.sdk.models.BaselineEngineClassPermission
    :param global_cost_avoidance_settings:
    :type global_cost_avoidance_settings:
     ~energycap.sdk.models.GlobalCostAvoidanceSettingsClassPermission
    :param dashboard_and_maps_module:
    :type dashboard_and_maps_module:
     ~energycap.sdk.models.DashboardAndMapsModuleClassPermission
    :param dashboard_administrator:
    :type dashboard_administrator:
     ~energycap.sdk.models.DashboardAdministratorClassPermission
    :param public_dashboards_or_maps:
    :type public_dashboards_or_maps:
     ~energycap.sdk.models.PublicDashboardsOrMapsClassPermission
    :param shared_dashboards_or_maps:
    :type shared_dashboards_or_maps:
     ~energycap.sdk.models.SharedDashboardsOrMapsClassPermission
    :param buildings_and_meters_module:
    :type buildings_and_meters_module:
     ~energycap.sdk.models.BuildingsAndMetersModuleClassPermission
    :param groups_and_benchmarks_module:
    :type groups_and_benchmarks_module:
     ~energycap.sdk.models.GroupsAndBenchmarksModuleClassPermission
    :param building_and_meter_groups:
    :type building_and_meter_groups:
     ~energycap.sdk.models.BuildingAndMeterGroupsClassPermission
    :param buildings_and_organizations:
    :type buildings_and_organizations:
     ~energycap.sdk.models.BuildingsAndOrganizationsClassPermission
    :param interval_data:
    :type interval_data: ~energycap.sdk.models.IntervalDataClassPermission
    :param interval_data_analysis:
    :type interval_data_analysis:
     ~energycap.sdk.models.IntervalDataAnalysisClassPermission
    :param energystar_submissions:
    :type energystar_submissions:
     ~energycap.sdk.models.ENERGYSTARSubmissionsClassPermission
    :param facility_projects:
    :type facility_projects:
     ~energycap.sdk.models.FacilityProjectsClassPermission
    :param greenhouse_gas_administrator:
    :type greenhouse_gas_administrator:
     ~energycap.sdk.models.GreenhouseGasAdministratorClassPermission
    :param interval_data_rollup:
    :type interval_data_rollup:
     ~energycap.sdk.models.IntervalDataRollupClassPermission
    :param meters:
    :type meters: ~energycap.sdk.models.MetersClassPermission
    :param normalization_settings:
    :type normalization_settings:
     ~energycap.sdk.models.NormalizationSettingsClassPermission
    :param weather_settings:
    :type weather_settings:
     ~energycap.sdk.models.WeatherSettingsClassPermission
    :param reports_module:
    :type reports_module: ~energycap.sdk.models.ReportsModuleClassPermission
    :param distributed_reports_settings:
    :type distributed_reports_settings:
     ~energycap.sdk.models.DistributedReportsSettingsClassPermission
    :param report_administrator:
    :type report_administrator:
     ~energycap.sdk.models.ReportAdministratorClassPermission
    :param report_groups:
    :type report_groups: ~energycap.sdk.models.ReportGroupsClassPermission
    :param shared_reports:
    :type shared_reports: ~energycap.sdk.models.SharedReportsClassPermission
    :param reset_user_passwords:
    :type reset_user_passwords:
     ~energycap.sdk.models.ResetUserPasswordsClassPermission
    :param users_and_roles:
    :type users_and_roles: ~energycap.sdk.models.UsersAndRolesClassPermission
    :param vendors_and_rates_module:
    :type vendors_and_rates_module:
     ~energycap.sdk.models.VendorsAndRatesModuleClassPermission
    :param rate_schedules:
    :type rate_schedules: ~energycap.sdk.models.RateSchedulesClassPermission
    :param vendors:
    :type vendors: ~energycap.sdk.models.VendorsClassPermission
    :param flagged_items:
    :type flagged_items: ~energycap.sdk.models.FlaggedItemsClassPermission
    :param bill_list_administrator:
    :type bill_list_administrator:
     ~energycap.sdk.models.BillListAdministratorClassPermission
    :param all_installed_reports:
    :type all_installed_reports:
     ~energycap.sdk.models.AllInstalledReportsClassPermission
    """

    _attribute_map = {
        'accounting_settings': {'key': 'accountingSettings', 'type': 'AccountingSettingsClassPermission'},
        'accounts': {'key': 'accounts', 'type': 'AccountsClassPermission'},
        'accounts_module': {'key': 'accountsModule', 'type': 'AccountsModuleClassPermission'},
        'accrual_settings': {'key': 'accrualSettings', 'type': 'AccrualSettingsClassPermission'},
        'cost_centers': {'key': 'costCenters', 'type': 'CostCentersClassPermission'},
        'move_accounts_between_vendors': {'key': 'moveAccountsBetweenVendors', 'type': 'MoveAccountsBetweenVendorsClassPermission'},
        'application_settings': {'key': 'applicationSettings', 'type': 'ApplicationSettingsClassPermission'},
        'approve_bills': {'key': 'approveBills', 'type': 'ApproveBillsClassPermission'},
        'bill_workflow_settings': {'key': 'billWorkflowSettings', 'type': 'BillWorkflowSettingsClassPermission'},
        'bills_and_batches': {'key': 'billsAndBatches', 'type': 'BillsAndBatchesClassPermission'},
        'export_bills': {'key': 'exportBills', 'type': 'ExportBillsClassPermission'},
        'export_hold': {'key': 'exportHold', 'type': 'ExportHoldClassPermission'},
        'move_existing_bills': {'key': 'moveExistingBills', 'type': 'MoveExistingBillsClassPermission'},
        'shared_bill_lists': {'key': 'sharedBillLists', 'type': 'SharedBillListsClassPermission'},
        'unit_system_settings': {'key': 'unitSystemSettings', 'type': 'UnitSystemSettingsClassPermission'},
        'update_approved_bills': {'key': 'updateApprovedBills', 'type': 'UpdateApprovedBillsClassPermission'},
        'update_units_on_existing_bills': {'key': 'updateUnitsOnExistingBills', 'type': 'UpdateUnitsOnExistingBillsClassPermission'},
        'budgets_and_budget_versions': {'key': 'budgetsAndBudgetVersions', 'type': 'BudgetsAndBudgetVersionsClassPermission'},
        'chargebacks_module': {'key': 'chargebacksModule', 'type': 'ChargebacksModuleClassPermission'},
        'chargebacks': {'key': 'chargebacks', 'type': 'ChargebacksClassPermission'},
        'chargeback_reversals': {'key': 'chargebackReversals', 'type': 'ChargebackReversalsClassPermission'},
        'meter_savings_settings': {'key': 'meterSavingsSettings', 'type': 'MeterSavingsSettingsClassPermission'},
        'savings_adjustments': {'key': 'savingsAdjustments', 'type': 'SavingsAdjustmentsClassPermission'},
        'manually_adjust_savings': {'key': 'manuallyAdjustSavings', 'type': 'ManuallyAdjustSavingsClassPermission'},
        'savings_engine': {'key': 'savingsEngine', 'type': 'SavingsEngineClassPermission'},
        'baseline_engine': {'key': 'baselineEngine', 'type': 'BaselineEngineClassPermission'},
        'global_cost_avoidance_settings': {'key': 'globalCostAvoidanceSettings', 'type': 'GlobalCostAvoidanceSettingsClassPermission'},
        'dashboard_and_maps_module': {'key': 'dashboardAndMapsModule', 'type': 'DashboardAndMapsModuleClassPermission'},
        'dashboard_administrator': {'key': 'dashboardAdministrator', 'type': 'DashboardAdministratorClassPermission'},
        'public_dashboards_or_maps': {'key': 'publicDashboardsOrMaps', 'type': 'PublicDashboardsOrMapsClassPermission'},
        'shared_dashboards_or_maps': {'key': 'sharedDashboardsOrMaps', 'type': 'SharedDashboardsOrMapsClassPermission'},
        'buildings_and_meters_module': {'key': 'buildingsAndMetersModule', 'type': 'BuildingsAndMetersModuleClassPermission'},
        'groups_and_benchmarks_module': {'key': 'groupsAndBenchmarksModule', 'type': 'GroupsAndBenchmarksModuleClassPermission'},
        'building_and_meter_groups': {'key': 'buildingAndMeterGroups', 'type': 'BuildingAndMeterGroupsClassPermission'},
        'buildings_and_organizations': {'key': 'buildingsAndOrganizations', 'type': 'BuildingsAndOrganizationsClassPermission'},
        'interval_data': {'key': 'intervalData', 'type': 'IntervalDataClassPermission'},
        'interval_data_analysis': {'key': 'intervalDataAnalysis', 'type': 'IntervalDataAnalysisClassPermission'},
        'energystar_submissions': {'key': 'energystarSubmissions', 'type': 'ENERGYSTARSubmissionsClassPermission'},
        'facility_projects': {'key': 'facilityProjects', 'type': 'FacilityProjectsClassPermission'},
        'greenhouse_gas_administrator': {'key': 'greenhouseGasAdministrator', 'type': 'GreenhouseGasAdministratorClassPermission'},
        'interval_data_rollup': {'key': 'intervalDataRollup', 'type': 'IntervalDataRollupClassPermission'},
        'meters': {'key': 'meters', 'type': 'MetersClassPermission'},
        'normalization_settings': {'key': 'normalizationSettings', 'type': 'NormalizationSettingsClassPermission'},
        'weather_settings': {'key': 'weatherSettings', 'type': 'WeatherSettingsClassPermission'},
        'reports_module': {'key': 'reportsModule', 'type': 'ReportsModuleClassPermission'},
        'distributed_reports_settings': {'key': 'distributedReportsSettings', 'type': 'DistributedReportsSettingsClassPermission'},
        'report_administrator': {'key': 'reportAdministrator', 'type': 'ReportAdministratorClassPermission'},
        'report_groups': {'key': 'reportGroups', 'type': 'ReportGroupsClassPermission'},
        'shared_reports': {'key': 'sharedReports', 'type': 'SharedReportsClassPermission'},
        'reset_user_passwords': {'key': 'resetUserPasswords', 'type': 'ResetUserPasswordsClassPermission'},
        'users_and_roles': {'key': 'usersAndRoles', 'type': 'UsersAndRolesClassPermission'},
        'vendors_and_rates_module': {'key': 'vendorsAndRatesModule', 'type': 'VendorsAndRatesModuleClassPermission'},
        'rate_schedules': {'key': 'rateSchedules', 'type': 'RateSchedulesClassPermission'},
        'vendors': {'key': 'vendors', 'type': 'VendorsClassPermission'},
        'flagged_items': {'key': 'flaggedItems', 'type': 'FlaggedItemsClassPermission'},
        'bill_list_administrator': {'key': 'billListAdministrator', 'type': 'BillListAdministratorClassPermission'},
        'all_installed_reports': {'key': 'allInstalledReports', 'type': 'AllInstalledReportsClassPermission'},
    }

    def __init__(self, accounting_settings=None, accounts=None, accounts_module=None, accrual_settings=None, cost_centers=None, move_accounts_between_vendors=None, application_settings=None, approve_bills=None, bill_workflow_settings=None, bills_and_batches=None, export_bills=None, export_hold=None, move_existing_bills=None, shared_bill_lists=None, unit_system_settings=None, update_approved_bills=None, update_units_on_existing_bills=None, budgets_and_budget_versions=None, chargebacks_module=None, chargebacks=None, chargeback_reversals=None, meter_savings_settings=None, savings_adjustments=None, manually_adjust_savings=None, savings_engine=None, baseline_engine=None, global_cost_avoidance_settings=None, dashboard_and_maps_module=None, dashboard_administrator=None, public_dashboards_or_maps=None, shared_dashboards_or_maps=None, buildings_and_meters_module=None, groups_and_benchmarks_module=None, building_and_meter_groups=None, buildings_and_organizations=None, interval_data=None, interval_data_analysis=None, energystar_submissions=None, facility_projects=None, greenhouse_gas_administrator=None, interval_data_rollup=None, meters=None, normalization_settings=None, weather_settings=None, reports_module=None, distributed_reports_settings=None, report_administrator=None, report_groups=None, shared_reports=None, reset_user_passwords=None, users_and_roles=None, vendors_and_rates_module=None, rate_schedules=None, vendors=None, flagged_items=None, bill_list_administrator=None, all_installed_reports=None):
        super(PermissionsRequest, self).__init__()
        self.accounting_settings = accounting_settings
        self.accounts = accounts
        self.accounts_module = accounts_module
        self.accrual_settings = accrual_settings
        self.cost_centers = cost_centers
        self.move_accounts_between_vendors = move_accounts_between_vendors
        self.application_settings = application_settings
        self.approve_bills = approve_bills
        self.bill_workflow_settings = bill_workflow_settings
        self.bills_and_batches = bills_and_batches
        self.export_bills = export_bills
        self.export_hold = export_hold
        self.move_existing_bills = move_existing_bills
        self.shared_bill_lists = shared_bill_lists
        self.unit_system_settings = unit_system_settings
        self.update_approved_bills = update_approved_bills
        self.update_units_on_existing_bills = update_units_on_existing_bills
        self.budgets_and_budget_versions = budgets_and_budget_versions
        self.chargebacks_module = chargebacks_module
        self.chargebacks = chargebacks
        self.chargeback_reversals = chargeback_reversals
        self.meter_savings_settings = meter_savings_settings
        self.savings_adjustments = savings_adjustments
        self.manually_adjust_savings = manually_adjust_savings
        self.savings_engine = savings_engine
        self.baseline_engine = baseline_engine
        self.global_cost_avoidance_settings = global_cost_avoidance_settings
        self.dashboard_and_maps_module = dashboard_and_maps_module
        self.dashboard_administrator = dashboard_administrator
        self.public_dashboards_or_maps = public_dashboards_or_maps
        self.shared_dashboards_or_maps = shared_dashboards_or_maps
        self.buildings_and_meters_module = buildings_and_meters_module
        self.groups_and_benchmarks_module = groups_and_benchmarks_module
        self.building_and_meter_groups = building_and_meter_groups
        self.buildings_and_organizations = buildings_and_organizations
        self.interval_data = interval_data
        self.interval_data_analysis = interval_data_analysis
        self.energystar_submissions = energystar_submissions
        self.facility_projects = facility_projects
        self.greenhouse_gas_administrator = greenhouse_gas_administrator
        self.interval_data_rollup = interval_data_rollup
        self.meters = meters
        self.normalization_settings = normalization_settings
        self.weather_settings = weather_settings
        self.reports_module = reports_module
        self.distributed_reports_settings = distributed_reports_settings
        self.report_administrator = report_administrator
        self.report_groups = report_groups
        self.shared_reports = shared_reports
        self.reset_user_passwords = reset_user_passwords
        self.users_and_roles = users_and_roles
        self.vendors_and_rates_module = vendors_and_rates_module
        self.rate_schedules = rate_schedules
        self.vendors = vendors
        self.flagged_items = flagged_items
        self.bill_list_administrator = bill_list_administrator
        self.all_installed_reports = all_installed_reports
