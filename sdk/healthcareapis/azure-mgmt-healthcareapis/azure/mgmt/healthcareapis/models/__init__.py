# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import CheckNameAvailabilityParameters
from ._models_py3 import CorsConfiguration
from ._models_py3 import DicomService
from ._models_py3 import DicomServiceAuthenticationConfiguration
from ._models_py3 import DicomServiceCollection
from ._models_py3 import DicomServicePatchResource
from ._models_py3 import Error
from ._models_py3 import ErrorDetails
from ._models_py3 import ErrorDetailsInternal
from ._models_py3 import FhirService
from ._models_py3 import FhirServiceAccessPolicyEntry
from ._models_py3 import FhirServiceAcrConfiguration
from ._models_py3 import FhirServiceAuthenticationConfiguration
from ._models_py3 import FhirServiceCollection
from ._models_py3 import FhirServiceCorsConfiguration
from ._models_py3 import FhirServiceExportConfiguration
from ._models_py3 import FhirServiceImportConfiguration
from ._models_py3 import FhirServicePatchResource
from ._models_py3 import IotConnector
from ._models_py3 import IotConnectorCollection
from ._models_py3 import IotConnectorPatchResource
from ._models_py3 import IotDestinationProperties
from ._models_py3 import IotEventHubIngestionEndpointConfiguration
from ._models_py3 import IotFhirDestination
from ._models_py3 import IotFhirDestinationCollection
from ._models_py3 import IotFhirDestinationProperties
from ._models_py3 import IotMappingProperties
from ._models_py3 import ListOperations
from ._models_py3 import LocationBasedResource
from ._models_py3 import LogSpecification
from ._models_py3 import MetricDimension
from ._models_py3 import MetricSpecification
from ._models_py3 import OperationDetail
from ._models_py3 import OperationDisplay
from ._models_py3 import OperationProperties
from ._models_py3 import OperationResultsDescription
from ._models_py3 import PrivateEndpoint
from ._models_py3 import PrivateEndpointConnection
from ._models_py3 import PrivateEndpointConnectionDescription
from ._models_py3 import PrivateEndpointConnectionListResult
from ._models_py3 import PrivateEndpointConnectionListResultDescription
from ._models_py3 import PrivateLinkResource
from ._models_py3 import PrivateLinkResourceDescription
from ._models_py3 import PrivateLinkResourceListResultDescription
from ._models_py3 import PrivateLinkServiceConnectionState
from ._models_py3 import Resource
from ._models_py3 import ResourceCore
from ._models_py3 import ResourceTags
from ._models_py3 import ResourceVersionPolicyConfiguration
from ._models_py3 import ServiceAccessPolicyEntry
from ._models_py3 import ServiceAcrConfigurationInfo
from ._models_py3 import ServiceAuthenticationConfigurationInfo
from ._models_py3 import ServiceCorsConfigurationInfo
from ._models_py3 import ServiceCosmosDbConfigurationInfo
from ._models_py3 import ServiceExportConfigurationInfo
from ._models_py3 import ServiceImportConfigurationInfo
from ._models_py3 import ServiceManagedIdentity
from ._models_py3 import ServiceManagedIdentityIdentity
from ._models_py3 import ServiceOciArtifactEntry
from ._models_py3 import ServiceSpecification
from ._models_py3 import ServicesDescription
from ._models_py3 import ServicesDescriptionListResult
from ._models_py3 import ServicesNameAvailabilityInfo
from ._models_py3 import ServicesPatchDescription
from ._models_py3 import ServicesProperties
from ._models_py3 import ServicesResource
from ._models_py3 import ServicesResourceIdentity
from ._models_py3 import SystemData
from ._models_py3 import TaggedResource
from ._models_py3 import UserAssignedIdentity
from ._models_py3 import Workspace
from ._models_py3 import WorkspaceList
from ._models_py3 import WorkspacePatchResource
from ._models_py3 import WorkspaceProperties

from ._healthcare_apis_management_client_enums import ActionType
from ._healthcare_apis_management_client_enums import CreatedByType
from ._healthcare_apis_management_client_enums import FhirResourceVersionPolicy
from ._healthcare_apis_management_client_enums import FhirServiceKind
from ._healthcare_apis_management_client_enums import IotIdentityResolutionType
from ._healthcare_apis_management_client_enums import Kind
from ._healthcare_apis_management_client_enums import ManagedServiceIdentityType
from ._healthcare_apis_management_client_enums import OperationResultStatus
from ._healthcare_apis_management_client_enums import PrivateEndpointConnectionProvisioningState
from ._healthcare_apis_management_client_enums import PrivateEndpointServiceConnectionStatus
from ._healthcare_apis_management_client_enums import ProvisioningState
from ._healthcare_apis_management_client_enums import PublicNetworkAccess
from ._healthcare_apis_management_client_enums import ServiceEventState
from ._healthcare_apis_management_client_enums import ServiceManagedIdentityType
from ._healthcare_apis_management_client_enums import ServiceNameUnavailabilityReason
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "CheckNameAvailabilityParameters",
    "CorsConfiguration",
    "DicomService",
    "DicomServiceAuthenticationConfiguration",
    "DicomServiceCollection",
    "DicomServicePatchResource",
    "Error",
    "ErrorDetails",
    "ErrorDetailsInternal",
    "FhirService",
    "FhirServiceAccessPolicyEntry",
    "FhirServiceAcrConfiguration",
    "FhirServiceAuthenticationConfiguration",
    "FhirServiceCollection",
    "FhirServiceCorsConfiguration",
    "FhirServiceExportConfiguration",
    "FhirServiceImportConfiguration",
    "FhirServicePatchResource",
    "IotConnector",
    "IotConnectorCollection",
    "IotConnectorPatchResource",
    "IotDestinationProperties",
    "IotEventHubIngestionEndpointConfiguration",
    "IotFhirDestination",
    "IotFhirDestinationCollection",
    "IotFhirDestinationProperties",
    "IotMappingProperties",
    "ListOperations",
    "LocationBasedResource",
    "LogSpecification",
    "MetricDimension",
    "MetricSpecification",
    "OperationDetail",
    "OperationDisplay",
    "OperationProperties",
    "OperationResultsDescription",
    "PrivateEndpoint",
    "PrivateEndpointConnection",
    "PrivateEndpointConnectionDescription",
    "PrivateEndpointConnectionListResult",
    "PrivateEndpointConnectionListResultDescription",
    "PrivateLinkResource",
    "PrivateLinkResourceDescription",
    "PrivateLinkResourceListResultDescription",
    "PrivateLinkServiceConnectionState",
    "Resource",
    "ResourceCore",
    "ResourceTags",
    "ResourceVersionPolicyConfiguration",
    "ServiceAccessPolicyEntry",
    "ServiceAcrConfigurationInfo",
    "ServiceAuthenticationConfigurationInfo",
    "ServiceCorsConfigurationInfo",
    "ServiceCosmosDbConfigurationInfo",
    "ServiceExportConfigurationInfo",
    "ServiceImportConfigurationInfo",
    "ServiceManagedIdentity",
    "ServiceManagedIdentityIdentity",
    "ServiceOciArtifactEntry",
    "ServiceSpecification",
    "ServicesDescription",
    "ServicesDescriptionListResult",
    "ServicesNameAvailabilityInfo",
    "ServicesPatchDescription",
    "ServicesProperties",
    "ServicesResource",
    "ServicesResourceIdentity",
    "SystemData",
    "TaggedResource",
    "UserAssignedIdentity",
    "Workspace",
    "WorkspaceList",
    "WorkspacePatchResource",
    "WorkspaceProperties",
    "ActionType",
    "CreatedByType",
    "FhirResourceVersionPolicy",
    "FhirServiceKind",
    "IotIdentityResolutionType",
    "Kind",
    "ManagedServiceIdentityType",
    "OperationResultStatus",
    "PrivateEndpointConnectionProvisioningState",
    "PrivateEndpointServiceConnectionStatus",
    "ProvisioningState",
    "PublicNetworkAccess",
    "ServiceEventState",
    "ServiceManagedIdentityType",
    "ServiceNameUnavailabilityReason",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
