# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.batch import BatchManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-batch
# USAGE
    python batch_account_create_byos.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = BatchManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="subid",
    )

    response = client.batch_account.begin_create(
        resource_group_name="default-azurebatch-japaneast",
        account_name="sampleacct",
        parameters={
            "location": "japaneast",
            "properties": {
                "autoStorage": {
                    "storageAccountId": "/subscriptions/subid/resourceGroups/default-azurebatch-japaneast/providers/Microsoft.Storage/storageAccounts/samplestorage"
                },
                "keyVaultReference": {
                    "id": "/subscriptions/subid/resourceGroups/default-azurebatch-japaneast/providers/Microsoft.KeyVault/vaults/sample",
                    "url": "http://sample.vault.azure.net/",
                },
                "poolAllocationMode": "UserSubscription",
            },
        },
    ).result()
    print(response)


# x-ms-original-file: specification/batch/resource-manager/Microsoft.Batch/stable/2022-10-01/examples/BatchAccountCreate_BYOS.json
if __name__ == "__main__":
    main()
