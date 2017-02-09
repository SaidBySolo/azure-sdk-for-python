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

from .resource import Resource


class Certificate(Resource):
    """SSL certificate for an app.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :param name: Resource Name.
    :type name: str
    :param kind: Kind of resource.
    :type kind: str
    :param location: Resource Location.
    :type location: str
    :param type: Resource type.
    :type type: str
    :param tags: Resource tags.
    :type tags: dict
    :ivar friendly_name: Friendly name of the certificate.
    :vartype friendly_name: str
    :ivar subject_name: Subject name of the certificate.
    :vartype subject_name: str
    :param host_names: Host names the certificate applies to.
    :type host_names: list of str
    :param pfx_blob: Pfx blob.
    :type pfx_blob: bytearray
    :ivar site_name: App name.
    :vartype site_name: str
    :ivar self_link: Self link.
    :vartype self_link: str
    :ivar issuer: Certificate issuer.
    :vartype issuer: str
    :ivar issue_date: Certificate issue Date.
    :vartype issue_date: datetime
    :ivar expiration_date: Certificate expriration date.
    :vartype expiration_date: datetime
    :param password: Certificate password.
    :type password: str
    :ivar thumbprint: Certificate thumbprint.
    :vartype thumbprint: str
    :ivar valid: Is the certificate valid?.
    :vartype valid: bool
    :param cer_blob: Raw bytes of .cer file
    :type cer_blob: str
    :ivar public_key_hash: Public key hash.
    :vartype public_key_hash: str
    :ivar hosting_environment_profile: Specification for the App Service
     Environment to use for the certificate.
    :vartype hosting_environment_profile: :class:`HostingEnvironmentProfile
     <azure.mgmt.web.models.HostingEnvironmentProfile>`
    :param key_vault_id: Key Vault Csm resource Id.
    :type key_vault_id: str
    :param key_vault_secret_name: Key Vault secret name.
    :type key_vault_secret_name: str
    :ivar key_vault_secret_status: Status of the Key Vault secret. Possible
     values include: 'Initialized', 'WaitingOnCertificateOrder', 'Succeeded',
     'CertificateOrderFailed', 'OperationNotPermittedOnKeyVault',
     'AzureServiceUnauthorizedToAccessKeyVault', 'KeyVaultDoesNotExist',
     'KeyVaultSecretDoesNotExist', 'UnknownError', 'ExternalPrivateKey',
     'Unknown'
    :vartype key_vault_secret_status: str or :class:`KeyVaultSecretStatus
     <azure.mgmt.web.models.KeyVaultSecretStatus>`
    :param server_farm_id: Resource ID of the associated App Service plan,
     formatted as:
     "/subscriptions/{subscriptionID}/resourceGroups/{groupName}/providers/Microsoft.Web/serverfarms/{appServicePlanName}".
    :type server_farm_id: str
    """

    _validation = {
        'id': {'readonly': True},
        'location': {'required': True},
        'friendly_name': {'readonly': True},
        'subject_name': {'readonly': True},
        'site_name': {'readonly': True},
        'self_link': {'readonly': True},
        'issuer': {'readonly': True},
        'issue_date': {'readonly': True},
        'expiration_date': {'readonly': True},
        'thumbprint': {'readonly': True},
        'valid': {'readonly': True},
        'public_key_hash': {'readonly': True},
        'hosting_environment_profile': {'readonly': True},
        'key_vault_secret_status': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'friendly_name': {'key': 'properties.friendlyName', 'type': 'str'},
        'subject_name': {'key': 'properties.subjectName', 'type': 'str'},
        'host_names': {'key': 'properties.hostNames', 'type': '[str]'},
        'pfx_blob': {'key': 'properties.pfxBlob', 'type': 'bytearray'},
        'site_name': {'key': 'properties.siteName', 'type': 'str'},
        'self_link': {'key': 'properties.selfLink', 'type': 'str'},
        'issuer': {'key': 'properties.issuer', 'type': 'str'},
        'issue_date': {'key': 'properties.issueDate', 'type': 'iso-8601'},
        'expiration_date': {'key': 'properties.expirationDate', 'type': 'iso-8601'},
        'password': {'key': 'properties.password', 'type': 'str'},
        'thumbprint': {'key': 'properties.thumbprint', 'type': 'str'},
        'valid': {'key': 'properties.valid', 'type': 'bool'},
        'cer_blob': {'key': 'properties.cerBlob', 'type': 'str'},
        'public_key_hash': {'key': 'properties.publicKeyHash', 'type': 'str'},
        'hosting_environment_profile': {'key': 'properties.hostingEnvironmentProfile', 'type': 'HostingEnvironmentProfile'},
        'key_vault_id': {'key': 'properties.keyVaultId', 'type': 'str'},
        'key_vault_secret_name': {'key': 'properties.keyVaultSecretName', 'type': 'str'},
        'key_vault_secret_status': {'key': 'properties.keyVaultSecretStatus', 'type': 'KeyVaultSecretStatus'},
        'server_farm_id': {'key': 'properties.serverFarmId', 'type': 'str'},
    }

    def __init__(self, location, name=None, kind=None, type=None, tags=None, host_names=None, pfx_blob=None, password=None, cer_blob=None, key_vault_id=None, key_vault_secret_name=None, server_farm_id=None):
        super(Certificate, self).__init__(name=name, kind=kind, location=location, type=type, tags=tags)
        self.friendly_name = None
        self.subject_name = None
        self.host_names = host_names
        self.pfx_blob = pfx_blob
        self.site_name = None
        self.self_link = None
        self.issuer = None
        self.issue_date = None
        self.expiration_date = None
        self.password = password
        self.thumbprint = None
        self.valid = None
        self.cer_blob = cer_blob
        self.public_key_hash = None
        self.hosting_environment_profile = None
        self.key_vault_id = key_vault_id
        self.key_vault_secret_name = key_vault_secret_name
        self.key_vault_secret_status = None
        self.server_farm_id = server_farm_id
