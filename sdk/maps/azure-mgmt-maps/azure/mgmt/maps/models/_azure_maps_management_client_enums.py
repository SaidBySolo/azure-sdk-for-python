# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class KeyType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Whether the operation refers to the primary or secondary key."""

    PRIMARY = "primary"
    SECONDARY = "secondary"


class Kind(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The Kind of the Maps Account."""

    GEN1 = "Gen1"
    GEN2 = "Gen2"


class Name(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The name of the SKU, in standard format (such as S0)."""

    S0 = "S0"
    S1 = "S1"
    G2 = "G2"


class ResourceIdentityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The identity type."""

    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned, UserAssigned"
    NONE = "None"


class SigningKey(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The Map account key to use for signing."""

    PRIMARY_KEY = "primaryKey"
    SECONDARY_KEY = "secondaryKey"
