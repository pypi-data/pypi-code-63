# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class NormalizationSettingsClassPermission(Model):
    """NormalizationSettingsClassPermission.

    :param view:
    :type view: bool
    :param manage:
    :type manage: bool
    """

    _attribute_map = {
        'view': {'key': 'view', 'type': 'bool'},
        'manage': {'key': 'manage', 'type': 'bool'},
    }

    def __init__(self, view=None, manage=None):
        super(NormalizationSettingsClassPermission, self).__init__()
        self.view = view
        self.manage = manage
