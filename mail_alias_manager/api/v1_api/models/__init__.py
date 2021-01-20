"""Module containing all schemas of the API."""

import marshmallow as ma
from ...util import MaBaseSchema

class RootSchema(MaBaseSchema):
    auth = ma.fields.Url(required=True, allow_none=False, dump_only=True)
