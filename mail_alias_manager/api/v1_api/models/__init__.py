"""Module containing all schemas of the API."""

import marshmallow as ma
from ...util import MaBaseSchema

from .recipient_alias import *
from .sender_alias import *


class RootSchema(MaBaseSchema):
    recipient_alias = ma.fields.Url(required=True, allow_none=False, dump_only=True)
    sender_alias = ma.fields.Url(required=True, allow_none=False, dump_only=True)
