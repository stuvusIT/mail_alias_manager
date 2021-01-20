"""
This type stub file was generated by pyright.
"""

"""Utils"""
def deepupdate(original, update):
    """Recursively update a dict.

    Subdict's won't be overwritten but also updated.
    """
    ...

def get_appcontext():
    """Return extension section from top of appcontext stack"""
    ...

def load_info_from_docstring(docstring, *, delimiter=...):
    """Load summary and description from docstring

    :param str delimiter: Summary and description information delimiter.
    If a line starts with this string, this line and the lines after are
    ignored. Defaults to "---".
    """
    ...

def unpack_tuple_response(rv):
    """Unpack a flask Response tuple"""
    ...

def set_status_and_headers_in_response(response, status, headers):
    """Set status and headers in flask Reponse object"""
    ...

def prepare_response(response, spec, default_response_content_type):
    """Rework response according to OAS version"""
    ...
