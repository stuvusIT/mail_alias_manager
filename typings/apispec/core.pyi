"""
This type stub file was generated by pyright.
"""

"""Core apispec classes and functions."""
from typing import Any, Dict, Sequence, Union

from apispec.utils import OpenAPIVersion


VALID_METHODS_OPENAPI_V2 = ["get", "post", "put", "patch", "delete", "head", "options"]
VALID_METHODS_OPENAPI_V3 = VALID_METHODS_OPENAPI_V2 + ["trace"]
VALID_METHODS = {2: VALID_METHODS_OPENAPI_V2, 3: VALID_METHODS_OPENAPI_V3}


class Components:
    """Stores OpenAPI components

    Components are top-level fields in OAS v2.
    They became sub-fields of "components" top-level field in OAS v3.
    """

    def __init__(self, plugins, openapi_version) -> None:
        ...

    def to_dict(self):
        ...

    def schema(self, name, component=..., **kwargs):
        """Add a new schema to the spec.

        :param str name: identifier by which schema may be referenced.
        :param dict component: schema definition.

        .. note::

            If you are using `apispec.ext.marshmallow`, you can pass fields' metadata as
            additional keyword arguments.

            For example, to add ``enum`` and ``description`` to your field: ::

                status = fields.String(
                    required=True,
                    enum=['open', 'closed'],
                    description='Status (open or closed)',
                )

        https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.2.md#schemaObject
        """
        ...

    def response(self, component_id, component=..., **kwargs):
        """Add a response which can be referenced.

        :param str component_id: ref_id to use as reference
        :param dict component: response fields
        :param dict kwargs: plugin-specific arguments
        """
        ...

    def parameter(self, component_id, location, component=..., **kwargs):
        """Add a parameter which can be referenced.

        :param str param_id: identifier by which parameter may be referenced.
        :param str location: location of the parameter.
        :param dict component: parameter fields.
        :param dict kwargs: plugin-specific arguments
        """
        ...

    def example(self, name, component, **kwargs):
        """Add an example which can be referenced

        :param str name: identifier by which example may be referenced.
        :param dict component: example fields.

        https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.1.md#exampleObject
        """
        ...

    def security_scheme(self, component_id: str, component: Dict[str, Any]) -> Components:
        """Add a security scheme which can be referenced.

        :param str component_id: component_id to use as reference
        :param dict kwargs: security scheme fields
        """
        ...


class APISpec:
    """Stores metadata that describes a RESTful API using the OpenAPI specification.

    :param str title: API title
    :param str version: API version
    :param list|tuple plugins: Plugin instances.
        See https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.2.md#infoObject
    :param str|OpenAPIVersion openapi_version: OpenAPI Specification version.
        Should be in the form '2.x' or '3.x.x' to comply with the OpenAPI standard.
    :param dict options: Optional top-level keys
        See https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.2.md#openapi-object
    """

    title: str = ...
    version: str = ...
    openapi_version: OpenAPIVersion = ...
    options: Dict[Any, Any] = ...
    plugins: Sequence[Any] = ...
    components: Components = ...

    def __init__(
        self,
        title: str,
        version: str,
        openapi_version: Union[str, OpenAPIVersion],
        plugins: Sequence[Any] = ...,
        **options
    ) -> None:
        ...

    def to_dict(self):
        ...

    def to_yaml(self):
        """Render the spec to YAML. Requires PyYAML to be installed."""
        ...

    def tag(self, tag):
        """Store information about a tag.

        :param dict tag: the dictionary storing information about the tag.
        """
        ...

    def path(
        self,
        path=...,
        *,
        operations=...,
        summary=...,
        description=...,
        parameters=...,
        **kwargs
    ):
        """Add a new path object to the spec.

        https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.2.md#path-item-object

        :param str|None path: URL path component
        :param dict|None operations: describes the http methods and options for `path`
        :param str summary: short summary relevant to all operations in this path
        :param str description: long description relevant to all operations in this path
        :param list|None parameters: list of parameters relevant to all operations in this path
        :param dict kwargs: parameters used by any path helpers see :meth:`register_path_helper`
        """
        ...

    def get_ref(self, obj_type, obj):
        """Return object or reference

        If obj is a dict, it is assumed to be a complete description and it is returned as is.
        Otherwise, it is assumed to be a reference name as string and the corresponding $ref
        string is returned.

        :param str obj_type: "schema", "parameter", "response" or "security_scheme"
        :param dict|str obj: object in dict form or as ref_id string
        """
        ...

    def clean_parameters(self, parameters):
        """Ensure that all parameters with "in" equal to "path" are also required
        as required by the OpenAPI specification, as well as normalizing any
        references to global parameters and checking for duplicates parameters

        See https ://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.2.md#parameterObject.

        :param list parameters: List of parameters mapping
        """
        ...

    def clean_operations(self, operations):
        """Ensure that all parameters with "in" equal to "path" are also required
        as required by the OpenAPI specification, as well as normalizing any
        references to global parameters. Also checks for invalid HTTP methods.

        See https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.2.md#parameterObject.

        :param dict operations: Dict mapping status codes to operations
        """
        ...
