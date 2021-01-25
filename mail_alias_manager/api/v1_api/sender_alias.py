"""Module containing the sender alias API of the v1 API."""

from flask import abort
from flask.views import MethodView

from .root import API_V1
from .models import SenderAlias

from ...db import DB
from ...db.models.sender_alias import SenderAlias as SenderAlias_DB


@API_V1.route("/sender_alias/")
class SenderAliasList(MethodView):
    """Root endpoint for all sender alias resources."""

    @API_V1.response(SenderAlias(many=True))
    def get(self):
        """Get all sender aliases"""
        return SenderAlias_DB.query.all()

    @API_V1.arguments(SenderAlias, description="The alias to add")
    @API_V1.response(SenderAlias, code=201)
    def post(self, new_data):
        """Add a new sender alias"""
        item = SenderAlias_DB(**new_data)
        DB.session.add(item)
        DB.session.commit()
        return item


@API_V1.route("/sender_alias/create_many")
class SenderAliasCreateMany(MethodView):
    """Endpoint to create many aliases in one request."""

    @API_V1.arguments(SenderAlias(many=True), description="The aliases to add")
    @API_V1.response(SenderAlias(many=True), code=201)
    def post(self, new_data):
        """Add new sender aliases"""
        items = []
        for data in new_data:
            item = SenderAlias_DB(**data)
            DB.session.add(item)
            items.append(item)
        DB.session.commit()
        return items


@API_V1.route("/sender_alias/replace")
class SenderAliasReplace(MethodView):
    """Endpoint to replace all sender aliases."""

    @API_V1.arguments(SenderAlias(many=True), description="The new list which should be set")
    @API_V1.response(code=204)
    def post(self, new_data):
        """Replace all sender aliases with the given list."""
        SenderAlias_DB.query.delete()

        for data in new_data:
            item = SenderAlias_DB(**data)
            DB.session.add(item)
        DB.session.commit()


@API_V1.route("/sender_alias/<sender_alias_id>/")
class SenderAlias(MethodView):
    """Endpoint for a single sender alias resource"""

    @API_V1.doc(responses={'404': {'description': 'When requested sender alias is not found'}})
    @API_V1.response(SenderAlias())
    def get(self, sender_alias_id):
        """ Get a single sender alias """
        item = SenderAlias_DB.query.filter(SenderAlias_DB.id == sender_alias_id).first()
        if item is None:
            abort(404, "Requested sender alias not found.")
        return item

    @API_V1.arguments(SenderAlias, description="The new values for the alias")
    @API_V1.response(SenderAlias())
    def put(self, sender_alias_id, update_data):
        """ Update a single sender alias """
        item = SenderAlias_DB.query.filter(SenderAlias_DB.id == sender_alias_id).first()
        if item is None:
            abort(404, "Requested sender alias not found.")
        item.update(update_data)
        DB.session.commit()
        return item

    @API_V1.response(code=204)
    def delete(self, sender_alias_id):
        """ Delete a single sender alias """
        item = SenderAlias_DB.query.filter(SenderAlias_DB.id == sender_alias_id).first()
        if item is None:
            return
        DB.session.delete(item)
        DB.session.commit()
