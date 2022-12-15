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
from ...operations._security_connector_governance_rules_operations import (
    build_create_or_update_request,
    build_delete_request,
    build_get_request,
)

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class SecurityConnectorGovernanceRulesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.security.v2022_01_01_preview.aio.SecurityCenter`'s
        :attr:`security_connector_governance_rules` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def get(
        self, resource_group_name: str, security_connector_name: str, rule_id: str, **kwargs: Any
    ) -> _models.GovernanceRule:
        """Get a specific governanceRule for the requested scope by ruleId.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param security_connector_name: The security connector name. Required.
        :type security_connector_name: str
        :param rule_id: The security GovernanceRule key - unique key for the standard GovernanceRule.
         Required.
        :type rule_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: GovernanceRule or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2022_01_01_preview.models.GovernanceRule
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
            "api_version", _params.pop("api-version", "2022-01-01-preview")
        )  # type: Literal["2022-01-01-preview"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.GovernanceRule]

        request = build_get_request(
            resource_group_name=resource_group_name,
            security_connector_name=security_connector_name,
            rule_id=rule_id,
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

        deserialized = self._deserialize("GovernanceRule", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/securityConnectors/{securityConnectorName}/providers/Microsoft.Security/governanceRules/{ruleId}"}  # type: ignore

    @overload
    async def create_or_update(
        self,
        resource_group_name: str,
        security_connector_name: str,
        rule_id: str,
        governance_rule: _models.GovernanceRule,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.GovernanceRule:
        """Creates or update a security GovernanceRule on the given security connector.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param security_connector_name: The security connector name. Required.
        :type security_connector_name: str
        :param rule_id: The security GovernanceRule key - unique key for the standard GovernanceRule.
         Required.
        :type rule_id: str
        :param governance_rule: GovernanceRule over a subscription scope. Required.
        :type governance_rule: ~azure.mgmt.security.v2022_01_01_preview.models.GovernanceRule
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: GovernanceRule or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2022_01_01_preview.models.GovernanceRule
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_or_update(
        self,
        resource_group_name: str,
        security_connector_name: str,
        rule_id: str,
        governance_rule: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.GovernanceRule:
        """Creates or update a security GovernanceRule on the given security connector.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param security_connector_name: The security connector name. Required.
        :type security_connector_name: str
        :param rule_id: The security GovernanceRule key - unique key for the standard GovernanceRule.
         Required.
        :type rule_id: str
        :param governance_rule: GovernanceRule over a subscription scope. Required.
        :type governance_rule: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: GovernanceRule or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2022_01_01_preview.models.GovernanceRule
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create_or_update(
        self,
        resource_group_name: str,
        security_connector_name: str,
        rule_id: str,
        governance_rule: Union[_models.GovernanceRule, IO],
        **kwargs: Any
    ) -> _models.GovernanceRule:
        """Creates or update a security GovernanceRule on the given security connector.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param security_connector_name: The security connector name. Required.
        :type security_connector_name: str
        :param rule_id: The security GovernanceRule key - unique key for the standard GovernanceRule.
         Required.
        :type rule_id: str
        :param governance_rule: GovernanceRule over a subscription scope. Is either a model type or a
         IO type. Required.
        :type governance_rule: ~azure.mgmt.security.v2022_01_01_preview.models.GovernanceRule or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: GovernanceRule or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2022_01_01_preview.models.GovernanceRule
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
            "api_version", _params.pop("api-version", "2022-01-01-preview")
        )  # type: Literal["2022-01-01-preview"]
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.GovernanceRule]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(governance_rule, (IO, bytes)):
            _content = governance_rule
        else:
            _json = self._serialize.body(governance_rule, "GovernanceRule")

        request = build_create_or_update_request(
            resource_group_name=resource_group_name,
            security_connector_name=security_connector_name,
            rule_id=rule_id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.create_or_update.metadata["url"],
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
            deserialized = self._deserialize("GovernanceRule", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("GovernanceRule", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/securityConnectors/{securityConnectorName}/providers/Microsoft.Security/governanceRules/{ruleId}"}  # type: ignore

    @distributed_trace_async
    async def delete(  # pylint: disable=inconsistent-return-statements
        self, resource_group_name: str, security_connector_name: str, rule_id: str, **kwargs: Any
    ) -> None:
        """Delete a GovernanceRule over a given scope.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param security_connector_name: The security connector name. Required.
        :type security_connector_name: str
        :param rule_id: The security GovernanceRule key - unique key for the standard GovernanceRule.
         Required.
        :type rule_id: str
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
            "api_version", _params.pop("api-version", "2022-01-01-preview")
        )  # type: Literal["2022-01-01-preview"]
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_delete_request(
            resource_group_name=resource_group_name,
            security_connector_name=security_connector_name,
            rule_id=rule_id,
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

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/securityConnectors/{securityConnectorName}/providers/Microsoft.Security/governanceRules/{ruleId}"}  # type: ignore
