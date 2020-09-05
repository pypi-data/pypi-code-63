# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Environment(Model):
    """Environment.

    :param build_date:
    :type build_date: datetime
    :param version:
    :type version: str
    """

    _attribute_map = {
        'build_date': {'key': 'buildDate', 'type': 'iso-8601'},
        'version': {'key': 'version', 'type': 'str'},
    }

    def __init__(self, build_date=None, version=None):
        super(Environment, self).__init__()
        self.build_date = build_date
        self.version = version
