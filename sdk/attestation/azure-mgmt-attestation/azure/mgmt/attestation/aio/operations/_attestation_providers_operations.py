# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._attestation_providers_operations import (
    build_create_request,
    build_delete_request,
    build_get_default_by_location_request,
    build_get_request,
    build_list_by_resource_group_request,
    build_list_default_request,
    build_list_request,
    build_update_request,
)

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class AttestationProvidersOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.attestation.aio.AttestationManagementClient`'s
        :attr:`attestation_providers` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def get(self, resource_group_name: str, provider_name: str, **kwargs: Any) -> _models.AttestationProvider:
        """Get the status of Attestation Provider.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param provider_name: Name of the attestation provider. Required.
        :type provider_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AttestationProvider or the result of cls(response)
        :rtype: ~azure.mgmt.attestation.models.AttestationProvider
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )  # type: Literal["2020-10-01"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.AttestationProvider]

        request = build_get_request(
            resource_group_name=resource_group_name,
            provider_name=provider_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("AttestationProvider", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Attestation/attestationProviders/{providerName}"}  # type: ignore

    @overload
    async def create(
        self,
        resource_group_name: str,
        provider_name: str,
        creation_params: _models.AttestationServiceCreationParams,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.AttestationProvider:
        """Creates a new Attestation Provider.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param provider_name: Name of the attestation provider. Required.
        :type provider_name: str
        :param creation_params: Client supplied parameters. Required.
        :type creation_params: ~azure.mgmt.attestation.models.AttestationServiceCreationParams
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AttestationProvider or the result of cls(response)
        :rtype: ~azure.mgmt.attestation.models.AttestationProvider
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create(
        self,
        resource_group_name: str,
        provider_name: str,
        creation_params: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.AttestationProvider:
        """Creates a new Attestation Provider.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param provider_name: Name of the attestation provider. Required.
        :type provider_name: str
        :param creation_params: Client supplied parameters. Required.
        :type creation_params: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AttestationProvider or the result of cls(response)
        :rtype: ~azure.mgmt.attestation.models.AttestationProvider
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create(
        self,
        resource_group_name: str,
        provider_name: str,
        creation_params: Union[_models.AttestationServiceCreationParams, IO],
        **kwargs: Any
    ) -> _models.AttestationProvider:
        """Creates a new Attestation Provider.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param provider_name: Name of the attestation provider. Required.
        :type provider_name: str
        :param creation_params: Client supplied parameters. Is either a model type or a IO type.
         Required.
        :type creation_params: ~azure.mgmt.attestation.models.AttestationServiceCreationParams or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AttestationProvider or the result of cls(response)
        :rtype: ~azure.mgmt.attestation.models.AttestationProvider
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )  # type: Literal["2020-10-01"]
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.AttestationProvider]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(creation_params, (IO, bytes)):
            _content = creation_params
        else:
            _json = self._serialize.body(creation_params, "AttestationServiceCreationParams")

        request = build_create_request(
            resource_group_name=resource_group_name,
            provider_name=provider_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.create.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("AttestationProvider", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("AttestationProvider", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Attestation/attestationProviders/{providerName}"}  # type: ignore

    @overload
    async def update(
        self,
        resource_group_name: str,
        provider_name: str,
        update_params: _models.AttestationServicePatchParams,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.AttestationProvider:
        """Updates the Attestation Provider.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param provider_name: Name of the attestation provider. Required.
        :type provider_name: str
        :param update_params: Client supplied parameters. Required.
        :type update_params: ~azure.mgmt.attestation.models.AttestationServicePatchParams
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AttestationProvider or the result of cls(response)
        :rtype: ~azure.mgmt.attestation.models.AttestationProvider
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def update(
        self,
        resource_group_name: str,
        provider_name: str,
        update_params: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.AttestationProvider:
        """Updates the Attestation Provider.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param provider_name: Name of the attestation provider. Required.
        :type provider_name: str
        :param update_params: Client supplied parameters. Required.
        :type update_params: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AttestationProvider or the result of cls(response)
        :rtype: ~azure.mgmt.attestation.models.AttestationProvider
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def update(
        self,
        resource_group_name: str,
        provider_name: str,
        update_params: Union[_models.AttestationServicePatchParams, IO],
        **kwargs: Any
    ) -> _models.AttestationProvider:
        """Updates the Attestation Provider.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param provider_name: Name of the attestation provider. Required.
        :type provider_name: str
        :param update_params: Client supplied parameters. Is either a model type or a IO type.
         Required.
        :type update_params: ~azure.mgmt.attestation.models.AttestationServicePatchParams or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AttestationProvider or the result of cls(response)
        :rtype: ~azure.mgmt.attestation.models.AttestationProvider
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )  # type: Literal["2020-10-01"]
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.AttestationProvider]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(update_params, (IO, bytes)):
            _content = update_params
        else:
            _json = self._serialize.body(update_params, "AttestationServicePatchParams")

        request = build_update_request(
            resource_group_name=resource_group_name,
            provider_name=provider_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.update.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("AttestationProvider", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Attestation/attestationProviders/{providerName}"}  # type: ignore

    @distributed_trace_async
    async def delete(  # pylint: disable=inconsistent-return-statements
        self, resource_group_name: str, provider_name: str, **kwargs: Any
    ) -> None:
        """Delete Attestation Service.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param provider_name: Name of the attestation service. Required.
        :type provider_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )  # type: Literal["2020-10-01"]
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_delete_request(
            resource_group_name=resource_group_name,
            provider_name=provider_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.delete.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Attestation/attestationProviders/{providerName}"}  # type: ignore

    @distributed_trace_async
    async def list(self, **kwargs: Any) -> _models.AttestationProviderListResult:
        """Returns a list of attestation providers in a subscription.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AttestationProviderListResult or the result of cls(response)
        :rtype: ~azure.mgmt.attestation.models.AttestationProviderListResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )  # type: Literal["2020-10-01"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.AttestationProviderListResult]

        request = build_list_request(
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.list.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("AttestationProviderListResult", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Attestation/attestationProviders"}  # type: ignore

    @distributed_trace_async
    async def list_by_resource_group(
        self, resource_group_name: str, **kwargs: Any
    ) -> _models.AttestationProviderListResult:
        """Returns attestation providers list in a resource group.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AttestationProviderListResult or the result of cls(response)
        :rtype: ~azure.mgmt.attestation.models.AttestationProviderListResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )  # type: Literal["2020-10-01"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.AttestationProviderListResult]

        request = build_list_by_resource_group_request(
            resource_group_name=resource_group_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.list_by_resource_group.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("AttestationProviderListResult", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list_by_resource_group.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Attestation/attestationProviders"}  # type: ignore

    @distributed_trace_async
    async def list_default(self, **kwargs: Any) -> _models.AttestationProviderListResult:
        """Get the default provider.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AttestationProviderListResult or the result of cls(response)
        :rtype: ~azure.mgmt.attestation.models.AttestationProviderListResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )  # type: Literal["2020-10-01"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.AttestationProviderListResult]

        request = build_list_default_request(
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.list_default.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("AttestationProviderListResult", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list_default.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Attestation/defaultProviders"}  # type: ignore

    @distributed_trace_async
    async def get_default_by_location(self, location: str, **kwargs: Any) -> _models.AttestationProvider:
        """Get the default provider by location.

        :param location: The location of the default provider. Required.
        :type location: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AttestationProvider or the result of cls(response)
        :rtype: ~azure.mgmt.attestation.models.AttestationProvider
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )  # type: Literal["2020-10-01"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.AttestationProvider]

        request = build_get_default_by_location_request(
            location=location,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get_default_by_location.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("AttestationProvider", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_default_by_location.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Attestation/locations/{location}/defaultProvider"}  # type: ignore
