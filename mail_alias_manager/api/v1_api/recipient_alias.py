"""Module containing the recipient alias API of the v1 API."""

from flask import abort
from flask.views import MethodView

from .root import API_V1
from .models import RecipientAlias

from ...db import DB
from ...db.models.recipient_alias import RecipientAlias as RecipientAlias_DB


@API_V1.route("/recipient_alias/")
class RecipientAliasList(MethodView):
    """Root endpoint for all recipient alias resources."""

    @API_V1.response(RecipientAlias(many=True))
    def get(self):
        """Get all recipient aliases"""
        return RecipientAlias_DB.query.all()

    @API_V1.arguments(RecipientAlias, description="The alias to add")
    @API_V1.response(RecipientAlias, code=201)
    def post(self, new_data):
        """Add a new recipient aliases"""
        item = RecipientAlias_DB(**new_data)
        DB.session.add(item)
        DB.session.commit()
        return item


@API_V1.route("/recipient_alias/create_many")
class RecipientAliasCreateMany(MethodView):
    """Endpoint to create many aliases in one request."""

    @API_V1.arguments(RecipientAlias(many=True), description="The alias to add")
    @API_V1.response(RecipientAlias(many=True), code=201)
    def post(self, new_data):
        """Add a new recipient aliases"""
        items = []
        for data in new_data:
            item = RecipientAlias_DB(**data)
            DB.session.add(item)
            items.append(item)
        DB.session.commit()
        return items


@API_V1.route("/recipient_alias/<recipient_alias_id>/")
class RecipientAlias(MethodView):
    """Endpoint for a single recipient alias resource"""

    @API_V1.doc(responses={'404': {'description': 'When requested recipient alias is not found'}})
    @API_V1.response(RecipientAlias())
    def get(self, recipient_alias_id):
        """ Get a single recipient alias """
        item = RecipientAlias_DB.query.filter(RecipientAlias_DB.id == recipient_alias_id).first()
        if item is None:
            abort(404, "Requested recipient alias not found.")
        return item

    @API_V1.arguments(RecipientAlias, description="The new values for the alias")
    @API_V1.response(RecipientAlias())
    def put(self, recipient_alias_id, update_data):
        """ Update a single recipient alias """
        item = RecipientAlias_DB.query.filter(RecipientAlias_DB.id == recipient_alias_id).first()
        if item is None:
            abort(404, "Requested recipient alias not found.")
        item.update(update_data)
        DB.session.commit()
        return item

    @API_V1.response(code=204)
    def delete(self, recipient_alias_id):
        """ Delete a single recipient alias """
        item = RecipientAlias_DB.query.filter(RecipientAlias_DB.id == recipient_alias_id).first()
        if item is None:
            return
        DB.session.delete(item)
        DB.session.commit()
