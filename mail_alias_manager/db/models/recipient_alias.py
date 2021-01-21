from sqlalchemy.sql.schema import Column
from sqlalchemy_utils.types.email import EmailType

from ..db import DB, MODEL


class RecipientAlias(MODEL):
    id: Column = DB.Column(DB.Integer, primary_key=True)
    alias: Column = DB.Column(EmailType, comment='The "To" address that should be redirected')
    recipient: Column = DB.Column(EmailType, comment='The "To" address to redirect to')

    def update(self, alias: str, recipient: str):
        self.alias = alias
        self.recipient = recipient
