# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, Iterable, Optional, TypeVar, Union
import urllib.parse

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from .._serialization import Serializer
from .._vendor import _convert_request, _format_url_section

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_list_by_billing_account_id_request(
    billing_account_id: str,
    *,
    grain_parameter: Optional[Union[str, _models.GrainParameter]] = None,
    filter: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2022-10-01"))  # type: Literal["2022-10-01"]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.CostManagement/benefitUtilizationSummaries",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "billingAccountId": _SERIALIZER.url("billing_account_id", billing_account_id, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if grain_parameter is not None:
        _params["grainParameter"] = _SERIALIZER.query("grain_parameter", grain_parameter, "str")
    if filter is not None:
        _params["filter"] = _SERIALIZER.query("filter", filter, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_list_by_billing_profile_id_request(
    billing_account_id: str,
    billing_profile_id: str,
    *,
    grain_parameter: Optional[Union[str, _models.GrainParameter]] = None,
    filter: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2022-10-01"))  # type: Literal["2022-10-01"]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/providers/Microsoft.CostManagement/benefitUtilizationSummaries",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "billingAccountId": _SERIALIZER.url("billing_account_id", billing_account_id, "str"),
        "billingProfileId": _SERIALIZER.url("billing_profile_id", billing_profile_id, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if grain_parameter is not None:
        _params["grainParameter"] = _SERIALIZER.query("grain_parameter", grain_parameter, "str")
    if filter is not None:
        _params["filter"] = _SERIALIZER.query("filter", filter, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_list_by_savings_plan_order_request(
    savings_plan_order_id: str,
    *,
    filter: Optional[str] = None,
    grain_parameter: Optional[Union[str, _models.GrainParameter]] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2022-10-01"))  # type: Literal["2022-10-01"]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/providers/Microsoft.BillingBenefits/savingsPlanOrders/{savingsPlanOrderId}/providers/Microsoft.CostManagement/benefitUtilizationSummaries",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "savingsPlanOrderId": _SERIALIZER.url("savings_plan_order_id", savings_plan_order_id, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if filter is not None:
        _params["$filter"] = _SERIALIZER.query("filter", filter, "str")
    if grain_parameter is not None:
        _params["grainParameter"] = _SERIALIZER.query("grain_parameter", grain_parameter, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_list_by_savings_plan_id_request(
    savings_plan_order_id: str,
    savings_plan_id: str,
    *,
    filter: Optional[str] = None,
    grain_parameter: Optional[Union[str, _models.GrainParameter]] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2022-10-01"))  # type: Literal["2022-10-01"]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/providers/Microsoft.BillingBenefits/savingsPlanOrders/{savingsPlanOrderId}/savingsPlans/{savingsPlanId}/providers/Microsoft.CostManagement/benefitUtilizationSummaries",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "savingsPlanOrderId": _SERIALIZER.url("savings_plan_order_id", savings_plan_order_id, "str"),
        "savingsPlanId": _SERIALIZER.url("savings_plan_id", savings_plan_id, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if filter is not None:
        _params["$filter"] = _SERIALIZER.query("filter", filter, "str")
    if grain_parameter is not None:
        _params["grainParameter"] = _SERIALIZER.query("grain_parameter", grain_parameter, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


class BenefitUtilizationSummariesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.costmanagement.CostManagementClient`'s
        :attr:`benefit_utilization_summaries` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list_by_billing_account_id(
        self,
        billing_account_id: str,
        grain_parameter: Optional[Union[str, _models.GrainParameter]] = None,
        filter: Optional[str] = None,
        **kwargs: Any
    ) -> Iterable["_models.BenefitUtilizationSummary"]:
        """Lists savings plan utilization summaries for the enterprise agreement scope. Supported at grain
        values: 'Daily' and 'Monthly'.

        :param billing_account_id: Billing account ID. Required.
        :type billing_account_id: str
        :param grain_parameter: Grain. Known values are: "Hourly", "Daily", and "Monthly". Default
         value is None.
        :type grain_parameter: str or ~azure.mgmt.costmanagement.models.GrainParameter
        :param filter: Supports filtering by properties/benefitId, properties/benefitOrderId and
         properties/usageDate. Default value is None.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either BenefitUtilizationSummary or the result of
         cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.costmanagement.models.BenefitUtilizationSummary]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )  # type: Literal["2022-10-01"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.BenefitUtilizationSummariesListResult]

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_by_billing_account_id_request(
                    billing_account_id=billing_account_id,
                    grain_parameter=grain_parameter,
                    filter=filter,
                    api_version=api_version,
                    template_url=self.list_by_billing_account_id.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("BenefitUtilizationSummariesListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    list_by_billing_account_id.metadata = {"url": "/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.CostManagement/benefitUtilizationSummaries"}  # type: ignore

    @distributed_trace
    def list_by_billing_profile_id(
        self,
        billing_account_id: str,
        billing_profile_id: str,
        grain_parameter: Optional[Union[str, _models.GrainParameter]] = None,
        filter: Optional[str] = None,
        **kwargs: Any
    ) -> Iterable["_models.BenefitUtilizationSummary"]:
        """Lists savings plan utilization summaries for billing profile. Supported at grain values:
        'Daily' and 'Monthly'.

        :param billing_account_id: Billing account ID. Required.
        :type billing_account_id: str
        :param billing_profile_id: Billing profile ID. Required.
        :type billing_profile_id: str
        :param grain_parameter: Grain. Known values are: "Hourly", "Daily", and "Monthly". Default
         value is None.
        :type grain_parameter: str or ~azure.mgmt.costmanagement.models.GrainParameter
        :param filter: Supports filtering by properties/benefitId, properties/benefitOrderId and
         properties/usageDate. Default value is None.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either BenefitUtilizationSummary or the result of
         cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.costmanagement.models.BenefitUtilizationSummary]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )  # type: Literal["2022-10-01"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.BenefitUtilizationSummariesListResult]

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_by_billing_profile_id_request(
                    billing_account_id=billing_account_id,
                    billing_profile_id=billing_profile_id,
                    grain_parameter=grain_parameter,
                    filter=filter,
                    api_version=api_version,
                    template_url=self.list_by_billing_profile_id.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("BenefitUtilizationSummariesListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    list_by_billing_profile_id.metadata = {"url": "/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/providers/Microsoft.CostManagement/benefitUtilizationSummaries"}  # type: ignore

    @distributed_trace
    def list_by_savings_plan_order(
        self,
        savings_plan_order_id: str,
        filter: Optional[str] = None,
        grain_parameter: Optional[Union[str, _models.GrainParameter]] = None,
        **kwargs: Any
    ) -> Iterable["_models.BenefitUtilizationSummary"]:
        """Lists the savings plan utilization summaries for daily or monthly grain.

        :param savings_plan_order_id: Savings plan order ID. Required.
        :type savings_plan_order_id: str
        :param filter: Supports filtering by properties/usageDate. Default value is None.
        :type filter: str
        :param grain_parameter: Grain. Known values are: "Hourly", "Daily", and "Monthly". Default
         value is None.
        :type grain_parameter: str or ~azure.mgmt.costmanagement.models.GrainParameter
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either BenefitUtilizationSummary or the result of
         cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.costmanagement.models.BenefitUtilizationSummary]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )  # type: Literal["2022-10-01"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.BenefitUtilizationSummariesListResult]

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_by_savings_plan_order_request(
                    savings_plan_order_id=savings_plan_order_id,
                    filter=filter,
                    grain_parameter=grain_parameter,
                    api_version=api_version,
                    template_url=self.list_by_savings_plan_order.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("BenefitUtilizationSummariesListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    list_by_savings_plan_order.metadata = {"url": "/providers/Microsoft.BillingBenefits/savingsPlanOrders/{savingsPlanOrderId}/providers/Microsoft.CostManagement/benefitUtilizationSummaries"}  # type: ignore

    @distributed_trace
    def list_by_savings_plan_id(
        self,
        savings_plan_order_id: str,
        savings_plan_id: str,
        filter: Optional[str] = None,
        grain_parameter: Optional[Union[str, _models.GrainParameter]] = None,
        **kwargs: Any
    ) -> Iterable["_models.BenefitUtilizationSummary"]:
        """Lists the savings plan utilization summaries for daily or monthly grain.

        :param savings_plan_order_id: Savings plan order ID. Required.
        :type savings_plan_order_id: str
        :param savings_plan_id: Savings plan ID. Required.
        :type savings_plan_id: str
        :param filter: Supports filtering by properties/usageDate. Default value is None.
        :type filter: str
        :param grain_parameter: Grain. Known values are: "Hourly", "Daily", and "Monthly". Default
         value is None.
        :type grain_parameter: str or ~azure.mgmt.costmanagement.models.GrainParameter
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either BenefitUtilizationSummary or the result of
         cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.costmanagement.models.BenefitUtilizationSummary]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )  # type: Literal["2022-10-01"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.BenefitUtilizationSummariesListResult]

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_by_savings_plan_id_request(
                    savings_plan_order_id=savings_plan_order_id,
                    savings_plan_id=savings_plan_id,
                    filter=filter,
                    grain_parameter=grain_parameter,
                    api_version=api_version,
                    template_url=self.list_by_savings_plan_id.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("BenefitUtilizationSummariesListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    list_by_savings_plan_id.metadata = {"url": "/providers/Microsoft.BillingBenefits/savingsPlanOrders/{savingsPlanOrderId}/savingsPlans/{savingsPlanId}/providers/Microsoft.CostManagement/benefitUtilizationSummaries"}  # type: ignore
