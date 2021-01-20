"""
This type stub file was generated by pyright.
"""

import yaml

"""YAML utilities"""
class YAMLDumper(yaml.Dumper):
    ...


def dict_to_yaml(dic):
    ...

def load_yaml_from_docstring(docstring):
    """Loads YAML from docstring."""
    ...

PATH_KEYS = "get", "put", "post", "delete", "options", "head", "patch"
def load_operations_from_docstring(docstring):
    """Return a dictionary of OpenAPI operations parsed from a
    a docstring.
    """
    ...

