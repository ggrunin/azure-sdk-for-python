# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .event_grid_event_data import EventGridEventData


class SubscriptionValidationEventData(EventGridEventData):
    """Schema of the Data property of an EventGridEvent for a
    Microsoft.EventGrid.SubscriptionValidationEvent.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar validation_code: The validation code sent by Azure Event Grid to
     validate an event subscription. To complete the validation handshake, the
     subscriber must either respond with this validation code as part of the
     validation response, or perform a GET request on the validationUrl
     (available starting version 2018-05-01-preview).
    :vartype validation_code: str
    :ivar validation_url: The validation URL sent by Azure Event Grid
     (available starting version 2018-05-01-preview). To complete the
     validation handshake, the subscriber must either respond with the
     validationCode as part of the validation response, or perform a GET
     request on the validationUrl (available starting version
     2018-05-01-preview).
    :vartype validation_url: str
    """

    _validation = {
        'validation_code': {'readonly': True},
        'validation_url': {'readonly': True},
    }

    _attribute_map = {
        'validation_code': {'key': 'validationCode', 'type': 'str'},
        'validation_url': {'key': 'validationUrl', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SubscriptionValidationEventData, self).__init__(**kwargs)
        self.validation_code = None
        self.validation_url = None
