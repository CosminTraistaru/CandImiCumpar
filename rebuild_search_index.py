import flask.ext.whooshalchemy

from app import models, app


def rebuild_index(model):
    """Rebuild search index of Flask-SQLAlchemy model"""
    primary_field = 'idProdus'
    searchables = model.__searchable__
    index_writer = flask.ext.whooshalchemy.whoosh_index(app, model)

    # Fetch all data
    entries = model.query.all()

    entry_count = 0
    with index_writer.writer() as writer:
        for entry in entries:
            index_attrs = {}
            for field in searchables:
                index_attrs[field] = unicode(getattr(entry, field))

            index_attrs[primary_field] = unicode(getattr(entry, primary_field))
            writer.update_document(**index_attrs)
            entry_count += 1
    print "rebuild model complete"


rebuild_index(models.Produs)