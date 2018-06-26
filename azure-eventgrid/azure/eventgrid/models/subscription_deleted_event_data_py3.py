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

from .event_grid_event_data_py3 import EventGridEventData


class SubscriptionDeletedEventData(EventGridEventData):
    """Schema of the Data property of an EventGridEvent for a
    Microsoft.EventGrid.SubscriptionDeletedEvent.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar event_subscription_id: The Azure resource ID of the deleted event
     subscription.
    :vartype event_subscription_id: str
    """

    _validation = {
        'event_subscription_id': {'readonly': True},
    }

    _attribute_map = {
        'event_subscription_id': {'key': 'eventSubscriptionId', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(SubscriptionDeletedEventData, self).__init__(**kwargs)
        self.event_subscription_id = None
