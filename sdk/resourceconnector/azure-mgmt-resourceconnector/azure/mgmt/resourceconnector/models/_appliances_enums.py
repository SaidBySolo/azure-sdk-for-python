# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class AccessProfileType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Name which contains the role of the kubeconfig."""

    CLUSTER_USER = "clusterUser"
    CLUSTER_CUSTOMER_USER = "clusterCustomerUser"


class ArtifactType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Appliance ArtifactType definition."""

    LOGS_ARTIFACT_TYPE = "LogsArtifactType"


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class Distro(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Represents a supported Fabric/Infra. (AKSEdge etc...)."""

    AKS_EDGE = "AKSEdge"


class Provider(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Information about the connected appliance."""

    VM_WARE = "VMWare"
    HCI = "HCI"
    SCVMM = "SCVMM"
    KUBE_VIRT = "KubeVirt"
    OPEN_STACK = "OpenStack"


class ResourceIdentityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The identity type."""

    SYSTEM_ASSIGNED = "SystemAssigned"
    NONE = "None"


class SSHKeyType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Appliance SSHKeyType definition."""

    SSH_CUSTOMER_USER = "SSHCustomerUser"
    MANAGEMENT_CA_KEY = "ManagementCAKey"
    LOGS_KEY = "LogsKey"
    SCOPED_ACCESS_KEY = "ScopedAccessKey"


class Status(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Appliance’s health and state of connection to on-prem."""

    WAITING_FOR_HEARTBEAT = "WaitingForHeartbeat"
    VALIDATING = "Validating"
    CONNECTING = "Connecting"
    CONNECTED = "Connected"
    RUNNING = "Running"
    PREPARING_FOR_UPGRADE = "PreparingForUpgrade"
    UPGRADE_PREREQUISITES_COMPLETED = "UpgradePrerequisitesCompleted"
    PRE_UPGRADE = "PreUpgrade"
    UPGRADING_KVAIO = "UpgradingKVAIO"
    WAITING_FOR_KVAIO = "WaitingForKVAIO"
    IMAGE_PENDING = "ImagePending"
    IMAGE_PROVISIONING = "ImageProvisioning"
    IMAGE_PROVISIONED = "ImageProvisioned"
    IMAGE_DOWNLOADING = "ImageDownloading"
    IMAGE_DOWNLOADED = "ImageDownloaded"
    IMAGE_DEPROVISIONING = "ImageDeprovisioning"
    IMAGE_UNKNOWN = "ImageUnknown"
    UPDATING_CLOUD_OPERATOR = "UpdatingCloudOperator"
    WAITING_FOR_CLOUD_OPERATOR = "WaitingForCloudOperator"
    UPDATING_CAPI = "UpdatingCAPI"
    UPDATING_CLUSTER = "UpdatingCluster"
    POST_UPGRADE = "PostUpgrade"
    UPGRADE_COMPLETE = "UpgradeComplete"
    UPGRADE_CLUSTER_EXTENSION_FAILED_TO_DELETE = "UpgradeClusterExtensionFailedToDelete"
    UPGRADE_FAILED = "UpgradeFailed"
    OFFLINE = "Offline"
    NONE = "None"
