"""Module containing all API schemas for the sender alias API."""

import marshmallow as ma
from ...util import MaBaseSchema

__all__ = [
    "SenderAlias"
]


class SenderAlias(MaBaseSchema):
    id = ma.fields.Int(required=True, allow_none=False, dump_only=True)
    sender = ma.fields.String(required=True, allow_none=False,
                              metadata={"description": "The username of the sender who has this alias"})
    alias = ma.fields.String(required=True, allow_none=False,
                             metadata={"description": "The email address for which the sender is allowed to use"})
