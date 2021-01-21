from sqlalchemy.sql.schema import Column
from sqlalchemy_utils.types.email import EmailType

from ..db import DB, MODEL


class SenderAlias(MODEL):
    id: Column = DB.Column(DB.Integer, primary_key=True)
    sender: Column = DB.Column(DB.String(120), comment="The username of the sender who has this alias")
    alias: Column = DB.Column(EmailType, comment="The email address for which the sender is allowed to send as")

    def update(self, sender: str, alias: str):
        self.sender = sender
        self.alias = alias
