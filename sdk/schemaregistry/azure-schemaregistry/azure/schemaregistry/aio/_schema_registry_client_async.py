# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------
from typing import Any, TYPE_CHECKING, Union, overload

from azure.core.tracing.decorator_async import distributed_trace_async
from .._utils import (
    build_get_schema_props_request,
    build_get_schema_request,
    build_register_schema_request,
)
from .._common._constants import SchemaFormat, DEFAULT_VERSION
from .._common._schema import Schema, SchemaProperties
from .._common._response_handlers import (
    _parse_response_schema,
    _parse_response_schema_properties,
)

from .._generated.aio._client import AzureSchemaRegistry

if TYPE_CHECKING:
    from azure.core.credentials_async import AsyncTokenCredential


class SchemaRegistryClient(object):
    """
    SchemaRegistryClient is a client for registering and retrieving schemas from the Azure Schema Registry service.

    :param str fully_qualified_namespace: The Schema Registry service fully qualified host name.
     For example: my-namespace.servicebus.windows.net.
    :param credential: To authenticate managing the entities of the SchemaRegistry namespace.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :keyword str api_version: The Schema Registry service API version to use for requests.
     Default value and only accepted value currently is "2021-10".

    .. admonition:: Example:

        .. literalinclude:: ../samples/async_samples/sample_code_schemaregistry_async.py
            :start-after: [START create_sr_client_async]
            :end-before: [END create_sr_client_async]
            :language: python
            :dedent: 4
            :caption: Create a new instance of the SchemaRegistryClient.

    """

    def __init__(
        self,
        fully_qualified_namespace: str,
        credential: "AsyncTokenCredential",
        **kwargs: Any,
    ) -> None:
        api_version = kwargs.pop("api_version", DEFAULT_VERSION)
        self._generated_client = AzureSchemaRegistry(
            credential=credential,
            endpoint=fully_qualified_namespace,
            api_version=api_version,
            **kwargs,
        )

    async def __aenter__(self):
        await self._generated_client.__aenter__()
        return self

    async def __aexit__(self, *args):
        await self._generated_client.__aexit__(*args)

    async def close(self) -> None:
        """This method is to close the sockets opened by the client.
        It need not be used when using with a context manager.
        """
        await self._generated_client.close()

    @distributed_trace_async
    async def register_schema(
        self,
        group_name: str,
        name: str,
        definition: str,
        format: Union[str, SchemaFormat],  # pylint:disable=redefined-builtin
        **kwargs: Any,
    ) -> SchemaProperties:
        """
        Register new schema. If schema of specified name does not exist in specified group,
        schema is created at version 1. If schema of specified name exists already in specified group,
        schema is created at latest version + 1.

        :param str group_name: Schema group under which schema should be registered.
        :param str name: Name of schema being registered.
        :param str definition: String representation of the schema being registered.
        :param format: Format for the schema being registered.
         For now Avro is the only supported schema format by the service.
        :type format: Union[str, ~azure.schemaregistry.SchemaFormat]
        :rtype: ~azure.schemaregistry.SchemaProperties
        :raises: :class:`~azure.core.exceptions.HttpResponseError`

        .. admonition:: Example:

            .. literalinclude:: ../samples/async_samples/sample_code_schemaregistry_async.py
                :start-after: [START register_schema_async]
                :end-before: [END register_schema_async]
                :language: python
                :dedent: 4
                :caption: Register a new schema.

        """
        request = build_register_schema_request(
            group_name, name, definition, format, kwargs
        )
        response = await self._generated_client.send_request(request, **kwargs)
        response.raise_for_status()
        return _parse_response_schema_properties(response, format)

    @overload
    async def get_schema(self, schema_id: str, **kwargs: Any) -> Schema:
        ...

    @overload
    async def get_schema(
        self, *, group_name: str, name: str, version: int, **kwargs
    ) -> Schema:
        ...

    @distributed_trace_async
    async def get_schema(self, *args: str, **kwargs: Any) -> Schema:
        """Gets a registered schema. There are two ways to call this method:

        1) To get a registered schema by its unique ID, pass the `schema_id` parameter and any optional
        keyword arguments. Azure Schema Registry guarantees that ID is unique within a namespace.

        2) To get a specific version of a schema within the specified schema group, pass in the required
        keyword arguments `group_name`, `name`, and `version` and any optional keyword arguments.

        :param str schema_id: References specific schema in registry namespace.
        :keyword str group_name: Name of schema group that contains the registered schema.
        :keyword str name: Name of schema which should be retrieved.
        :keyword int version: Version of schema which should be retrieved.
        :rtype: ~azure.schemaregistry.Schema
        :raises: :class:`~azure.core.exceptions.HttpResponseError`

        .. admonition:: Example:

            .. literalinclude:: ../samples/async_samples/sample_code_schemaregistry_async.py
                :start-after: [START get_schema_async]
                :end-before: [END get_schema_async]
                :language: python
                :dedent: 4
                :caption: Get schema by id.

            .. literalinclude:: ../samples/async_samples/sample_code_schemaregistry_async.py
                :start-after: [START get_schema_by_version_async]
                :end-before: [END get_schema_by_version_async]
                :language: python
                :dedent: 4
                :caption: Get schema by version.
        """
        request = build_get_schema_request(args, kwargs)
        response = await self._generated_client.send_request(request, **kwargs)
        response.raise_for_status()
        return _parse_response_schema(response)

    @distributed_trace_async
    async def get_schema_properties(
        self,
        group_name: str,
        name: str,
        definition: str,
        format: Union[str, SchemaFormat],  # pylint:disable=redefined-builtin
        **kwargs: Any,
    ) -> SchemaProperties:
        """
        Gets the schema properties corresponding to an existing schema within the specified schema group,
        as matched by schema defintion comparison.

        :param str group_name: Schema group under which schema should be registered.
        :param str name: Name of schema for which properties should be retrieved.
        :param str definition: String representation of the schema for which properties should be retrieved.
        :param format: Format for the schema for which properties should be retrieved.
        :type format: Union[str, SchemaFormat]
        :rtype: ~azure.schemaregistry.SchemaProperties
        :raises: :class:`~azure.core.exceptions.HttpResponseError`

        .. admonition:: Example:

            .. literalinclude:: ../samples/async_samples/sample_code_schemaregistry_async.py
                :start-after: [START get_schema_id_async]
                :end-before: [END get_schema_id_async]
                :language: python
                :dedent: 4
                :caption: Get schema by id.

        """
        request = build_get_schema_props_request(
            group_name, name, definition, format, kwargs
        )
        response = await self._generated_client.send_request(request, **kwargs)
        response.raise_for_status()
        return _parse_response_schema_properties(response, format)
