# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ChargebackWorkflowStepChild(Model):
    """ChargebackWorkflowStepChild.

    :param chargeback_workflow_step_id: Identifier for the chargeback workflow
     step
    :type chargeback_workflow_step_id: int
    :param chargeback_workflow_step_info: Name given to the chargeback
     workflow step
    :type chargeback_workflow_step_info: str
    :param chargeback_workflow_step_description: Description for the
     chargeback workflow step
    :type chargeback_workflow_step_description: str
    :param chargeback_workflow_step_type: The chargeback type that can be
     assign to this chargeback workflow step. <span
     class='property-internal'>One of Split, Calculation </span> <span
     class='property-internal'>One of Split, Calculation </span>
    :type chargeback_workflow_step_type: str
    :param chargeback_workflow_step_order: The order for this step within the
     chargeback workflow
    :type chargeback_workflow_step_order: int
    :param chargeback_workflow:
    :type chargeback_workflow: ~energycap.sdk.models.ChargebackWorkflowBase
    """

    _attribute_map = {
        'chargeback_workflow_step_id': {'key': 'chargebackWorkflowStepId', 'type': 'int'},
        'chargeback_workflow_step_info': {'key': 'chargebackWorkflowStepInfo', 'type': 'str'},
        'chargeback_workflow_step_description': {'key': 'chargebackWorkflowStepDescription', 'type': 'str'},
        'chargeback_workflow_step_type': {'key': 'chargebackWorkflowStepType', 'type': 'str'},
        'chargeback_workflow_step_order': {'key': 'chargebackWorkflowStepOrder', 'type': 'int'},
        'chargeback_workflow': {'key': 'chargebackWorkflow', 'type': 'ChargebackWorkflowBase'},
    }

    def __init__(self, chargeback_workflow_step_id=None, chargeback_workflow_step_info=None, chargeback_workflow_step_description=None, chargeback_workflow_step_type=None, chargeback_workflow_step_order=None, chargeback_workflow=None):
        super(ChargebackWorkflowStepChild, self).__init__()
        self.chargeback_workflow_step_id = chargeback_workflow_step_id
        self.chargeback_workflow_step_info = chargeback_workflow_step_info
        self.chargeback_workflow_step_description = chargeback_workflow_step_description
        self.chargeback_workflow_step_type = chargeback_workflow_step_type
        self.chargeback_workflow_step_order = chargeback_workflow_step_order
        self.chargeback_workflow = chargeback_workflow
