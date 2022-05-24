# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable, TYPE_CHECKING

from msrest import Deserializer, Serializer

from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.mgmt.core import AsyncARMPipelineClient

from .. import models
from ._configuration import KeyVaultManagementClientConfiguration
from .operations import KeysOperations, ManagedHsmsOperations, Operations, PrivateEndpointConnectionsOperations, PrivateLinkResourcesOperations, SecretsOperations, VaultsOperations

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

class KeyVaultManagementClient:    # pylint: disable=too-many-instance-attributes
    """The Azure management API provides a RESTful set of web services that interact with Azure Key
    Vault.

    :ivar keys: KeysOperations operations
    :vartype keys: azure.mgmt.keyvault.v2020_04_01_preview.aio.operations.KeysOperations
    :ivar vaults: VaultsOperations operations
    :vartype vaults: azure.mgmt.keyvault.v2020_04_01_preview.aio.operations.VaultsOperations
    :ivar private_endpoint_connections: PrivateEndpointConnectionsOperations operations
    :vartype private_endpoint_connections:
     azure.mgmt.keyvault.v2020_04_01_preview.aio.operations.PrivateEndpointConnectionsOperations
    :ivar private_link_resources: PrivateLinkResourcesOperations operations
    :vartype private_link_resources:
     azure.mgmt.keyvault.v2020_04_01_preview.aio.operations.PrivateLinkResourcesOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.keyvault.v2020_04_01_preview.aio.operations.Operations
    :ivar secrets: SecretsOperations operations
    :vartype secrets: azure.mgmt.keyvault.v2020_04_01_preview.aio.operations.SecretsOperations
    :ivar managed_hsms: ManagedHsmsOperations operations
    :vartype managed_hsms:
     azure.mgmt.keyvault.v2020_04_01_preview.aio.operations.ManagedHsmsOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure
     subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2020-04-01-preview". Note that overriding
     this default value may result in unsupported behavior.
    :paramtype api_version: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = KeyVaultManagementClientConfiguration(credential=credential, subscription_id=subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.keys = KeysOperations(self._client, self._config, self._serialize, self._deserialize)
        self.vaults = VaultsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.private_link_resources = PrivateLinkResourcesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize)
        self.secrets = SecretsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.managed_hsms = ManagedHsmsOperations(self._client, self._config, self._serialize, self._deserialize)


    def _send_request(
        self,
        request: HttpRequest,
        **kwargs: Any
    ) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = await client._send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/python/protocol/quickstart

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "KeyVaultManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
