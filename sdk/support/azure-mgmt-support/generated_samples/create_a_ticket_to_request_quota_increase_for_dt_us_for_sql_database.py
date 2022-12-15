# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.support import MicrosoftSupport

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-support
# USAGE
    python create_a_ticket_to_request_quota_increase_for_dt_us_for_sql_database.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = MicrosoftSupport(
        credential=DefaultAzureCredential(),
        subscription_id="subid",
    )

    response = client.support_tickets.begin_create(
        support_ticket_name="testticket",
        create_support_ticket_parameters={
            "properties": {
                "contactDetails": {
                    "country": "usa",
                    "firstName": "abc",
                    "lastName": "xyz",
                    "preferredContactMethod": "email",
                    "preferredSupportLanguage": "en-US",
                    "preferredTimeZone": "Pacific Standard Time",
                    "primaryEmailAddress": "abc@contoso.com",
                },
                "description": "my description",
                "problemClassificationId": "/providers/Microsoft.Support/services/quota_service_guid/problemClassifications/sql_database_problemClassification_guid",
                "quotaTicketDetails": {
                    "quotaChangeRequestSubType": "DTUs",
                    "quotaChangeRequestVersion": "1.0",
                    "quotaChangeRequests": [
                        {"payload": '{"ServerName":"testserver","NewLimit":54000}', "region": "EastUS"}
                    ],
                },
                "serviceId": "/providers/Microsoft.Support/services/quota_service_guid",
                "severity": "moderate",
                "title": "my title",
            }
        },
    ).result()
    print(response)


# x-ms-original-file: specification/support/resource-manager/Microsoft.Support/stable/2020-04-01/examples/CreateSqlDatabaseQuotaTicketForDTUs.json
if __name__ == "__main__":
    main()
