"""Module containing all API schemas for the recipient alias API."""

import marshmallow as ma
from ...util import MaBaseSchema

__all__ = [
    "RecipientAlias"
]


class RecipientAlias(MaBaseSchema):
    id = ma.fields.Int(required=True, allow_none=False, dump_only=True)
    alias = ma.fields.String(required=True, allow_none=False,
                             metadata={"description": 'The "To" address that should be redirected'})
    recipient = ma.fields.String(required=True, allow_none=False,
                                 metadata={"description": 'The "To" address to redirect to'})
