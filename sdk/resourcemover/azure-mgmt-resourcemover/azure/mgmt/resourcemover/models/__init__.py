# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AffectedMoveResource
from ._models_py3 import AutomaticResolutionProperties
from ._models_py3 import AvailabilitySetResourceSettings
from ._models_py3 import AzureResourceReference
from ._models_py3 import BulkRemoveRequest
from ._models_py3 import CloudErrorBody
from ._models_py3 import CommitRequest
from ._models_py3 import DiscardRequest
from ._models_py3 import DiskEncryptionSetResourceSettings
from ._models_py3 import Display
from ._models_py3 import Identity
from ._models_py3 import JobStatus
from ._models_py3 import KeyVaultResourceSettings
from ._models_py3 import LBBackendAddressPoolResourceSettings
from ._models_py3 import LBFrontendIPConfigurationResourceSettings
from ._models_py3 import LoadBalancerBackendAddressPoolReference
from ._models_py3 import LoadBalancerNatRuleReference
from ._models_py3 import LoadBalancerResourceSettings
from ._models_py3 import ManualResolutionProperties
from ._models_py3 import MoveCollection
from ._models_py3 import MoveCollectionProperties
from ._models_py3 import MoveCollectionPropertiesErrors
from ._models_py3 import MoveCollectionResultList
from ._models_py3 import MoveErrorInfo
from ._models_py3 import MoveResource
from ._models_py3 import MoveResourceCollection
from ._models_py3 import MoveResourceDependency
from ._models_py3 import MoveResourceDependencyOverride
from ._models_py3 import MoveResourceError
from ._models_py3 import MoveResourceErrorBody
from ._models_py3 import MoveResourceFilter
from ._models_py3 import MoveResourceFilterProperties
from ._models_py3 import MoveResourceProperties
from ._models_py3 import MoveResourcePropertiesErrors
from ._models_py3 import MoveResourcePropertiesMoveStatus
from ._models_py3 import MoveResourceStatus
from ._models_py3 import NetworkInterfaceResourceSettings
from ._models_py3 import NetworkSecurityGroupResourceSettings
from ._models_py3 import NicIpConfigurationResourceSettings
from ._models_py3 import NsgReference
from ._models_py3 import NsgSecurityRule
from ._models_py3 import OperationErrorAdditionalInfo
from ._models_py3 import OperationStatus
from ._models_py3 import OperationStatusError
from ._models_py3 import OperationsDiscovery
from ._models_py3 import OperationsDiscoveryCollection
from ._models_py3 import PrepareRequest
from ._models_py3 import ProxyResourceReference
from ._models_py3 import PublicIPAddressResourceSettings
from ._models_py3 import PublicIpReference
from ._models_py3 import RequiredForResourcesCollection
from ._models_py3 import ResourceGroupResourceSettings
from ._models_py3 import ResourceMoveRequest
from ._models_py3 import ResourceSettings
from ._models_py3 import SqlDatabaseResourceSettings
from ._models_py3 import SqlElasticPoolResourceSettings
from ._models_py3 import SqlServerResourceSettings
from ._models_py3 import SubnetReference
from ._models_py3 import SubnetResourceSettings
from ._models_py3 import Summary
from ._models_py3 import SummaryCollection
from ._models_py3 import SystemData
from ._models_py3 import UnresolvedDependenciesFilter
from ._models_py3 import UnresolvedDependenciesFilterProperties
from ._models_py3 import UnresolvedDependency
from ._models_py3 import UnresolvedDependencyCollection
from ._models_py3 import UpdateMoveCollectionRequest
from ._models_py3 import VirtualMachineResourceSettings
from ._models_py3 import VirtualNetworkResourceSettings

from ._resource_mover_service_api_enums import CreatedByType
from ._resource_mover_service_api_enums import DependencyLevel
from ._resource_mover_service_api_enums import DependencyType
from ._resource_mover_service_api_enums import JobName
from ._resource_mover_service_api_enums import MoveResourceInputType
from ._resource_mover_service_api_enums import MoveState
from ._resource_mover_service_api_enums import ProvisioningState
from ._resource_mover_service_api_enums import ResolutionType
from ._resource_mover_service_api_enums import ResourceIdentityType
from ._resource_mover_service_api_enums import TargetAvailabilityZone
from ._resource_mover_service_api_enums import ZoneRedundant
from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AffectedMoveResource",
    "AutomaticResolutionProperties",
    "AvailabilitySetResourceSettings",
    "AzureResourceReference",
    "BulkRemoveRequest",
    "CloudErrorBody",
    "CommitRequest",
    "DiscardRequest",
    "DiskEncryptionSetResourceSettings",
    "Display",
    "Identity",
    "JobStatus",
    "KeyVaultResourceSettings",
    "LBBackendAddressPoolResourceSettings",
    "LBFrontendIPConfigurationResourceSettings",
    "LoadBalancerBackendAddressPoolReference",
    "LoadBalancerNatRuleReference",
    "LoadBalancerResourceSettings",
    "ManualResolutionProperties",
    "MoveCollection",
    "MoveCollectionProperties",
    "MoveCollectionPropertiesErrors",
    "MoveCollectionResultList",
    "MoveErrorInfo",
    "MoveResource",
    "MoveResourceCollection",
    "MoveResourceDependency",
    "MoveResourceDependencyOverride",
    "MoveResourceError",
    "MoveResourceErrorBody",
    "MoveResourceFilter",
    "MoveResourceFilterProperties",
    "MoveResourceProperties",
    "MoveResourcePropertiesErrors",
    "MoveResourcePropertiesMoveStatus",
    "MoveResourceStatus",
    "NetworkInterfaceResourceSettings",
    "NetworkSecurityGroupResourceSettings",
    "NicIpConfigurationResourceSettings",
    "NsgReference",
    "NsgSecurityRule",
    "OperationErrorAdditionalInfo",
    "OperationStatus",
    "OperationStatusError",
    "OperationsDiscovery",
    "OperationsDiscoveryCollection",
    "PrepareRequest",
    "ProxyResourceReference",
    "PublicIPAddressResourceSettings",
    "PublicIpReference",
    "RequiredForResourcesCollection",
    "ResourceGroupResourceSettings",
    "ResourceMoveRequest",
    "ResourceSettings",
    "SqlDatabaseResourceSettings",
    "SqlElasticPoolResourceSettings",
    "SqlServerResourceSettings",
    "SubnetReference",
    "SubnetResourceSettings",
    "Summary",
    "SummaryCollection",
    "SystemData",
    "UnresolvedDependenciesFilter",
    "UnresolvedDependenciesFilterProperties",
    "UnresolvedDependency",
    "UnresolvedDependencyCollection",
    "UpdateMoveCollectionRequest",
    "VirtualMachineResourceSettings",
    "VirtualNetworkResourceSettings",
    "CreatedByType",
    "DependencyLevel",
    "DependencyType",
    "JobName",
    "MoveResourceInputType",
    "MoveState",
    "ProvisioningState",
    "ResolutionType",
    "ResourceIdentityType",
    "TargetAvailabilityZone",
    "ZoneRedundant",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
