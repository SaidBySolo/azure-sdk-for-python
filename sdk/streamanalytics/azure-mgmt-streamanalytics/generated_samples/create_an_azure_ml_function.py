# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.streamanalytics import StreamAnalyticsManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-streamanalytics
# USAGE
    python create_an_azure_ml_function.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = StreamAnalyticsManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="56b5e0a9-b645-407d-99b0-c64f86013e3d",
    )

    response = client.functions.create_or_replace(
        resource_group_name="sjrg7",
        job_name="sj9093",
        function_name="function588",
        function={
            "properties": {
                "properties": {
                    "binding": {
                        "properties": {
                            "apiKey": "someApiKey==",
                            "batchSize": 1000,
                            "endpoint": "someAzureMLEndpointURL",
                            "inputs": {
                                "columnNames": [{"dataType": "string", "mapTo": 0, "name": "tweet"}],
                                "name": "input1",
                            },
                            "outputs": [{"dataType": "string", "name": "Sentiment"}],
                        },
                        "type": "Microsoft.MachineLearning/WebService",
                    },
                    "inputs": [{"dataType": "nvarchar(max)"}],
                    "output": {"dataType": "nvarchar(max)"},
                },
                "type": "Scalar",
            }
        },
    )
    print(response)


# x-ms-original-file: specification/streamanalytics/resource-manager/Microsoft.StreamAnalytics/preview/2021-10-01-preview/examples/Function_Create_AzureML.json
if __name__ == "__main__":
    main()
