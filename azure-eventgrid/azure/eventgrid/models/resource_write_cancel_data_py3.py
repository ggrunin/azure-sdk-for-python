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


class ResourceWriteCancelData(EventGridEventData):
    """Schema of the Data property of an EventGridEvent for a
    Microsoft.Resources.ResourceWriteCancel event. This is raised when a
    resource create or update operation is canceled.

    :param tenant_id: The tenant ID of the resource.
    :type tenant_id: str
    :param subscription_id: The subscription ID of the resource.
    :type subscription_id: str
    :param resource_group: The resource group of the resource.
    :type resource_group: str
    :param resource_provider: The resource provider performing the operation.
    :type resource_provider: str
    :param resource_uri: The URI of the resource in the operation.
    :type resource_uri: str
    :param operation_name: The operation that was performed.
    :type operation_name: str
    :param status: The status of the operation.
    :type status: str
    :param authorization: The requested authorization for the operation.
    :type authorization: str
    :param claims: The properties of the claims.
    :type claims: str
    :param correlation_id: An operation ID used for troubleshooting.
    :type correlation_id: str
    :param http_request: The details of the operation.
    :type http_request: str
    """

    _attribute_map = {
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'subscription_id': {'key': 'subscriptionId', 'type': 'str'},
        'resource_group': {'key': 'resourceGroup', 'type': 'str'},
        'resource_provider': {'key': 'resourceProvider', 'type': 'str'},
        'resource_uri': {'key': 'resourceUri', 'type': 'str'},
        'operation_name': {'key': 'operationName', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'authorization': {'key': 'authorization', 'type': 'str'},
        'claims': {'key': 'claims', 'type': 'str'},
        'correlation_id': {'key': 'correlationId', 'type': 'str'},
        'http_request': {'key': 'httpRequest', 'type': 'str'},
    }

    def __init__(self, *, tenant_id: str=None, subscription_id: str=None, resource_group: str=None, resource_provider: str=None, resource_uri: str=None, operation_name: str=None, status: str=None, authorization: str=None, claims: str=None, correlation_id: str=None, http_request: str=None, **kwargs) -> None:
        super(ResourceWriteCancelData, self).__init__(**kwargs)
        self.tenant_id = tenant_id
        self.subscription_id = subscription_id
        self.resource_group = resource_group
        self.resource_provider = resource_provider
        self.resource_uri = resource_uri
        self.operation_name = operation_name
        self.status = status
        self.authorization = authorization
        self.claims = claims
        self.correlation_id = correlation_id
        self.http_request = http_request
