import pytest
from flask_taxonomies.proxies import current_flask_taxonomies
from flask_taxonomies.term_identification import TermIdentification
from invenio_records import Record

from oarepo_taxonomies.exceptions import DeleteAbortedError


def test_taxonomy_delete(app, db, taxonomy_tree, test_record):
    taxonomies = current_flask_taxonomies.list_taxonomies(session=None).all()
    assert len(taxonomies) == 1
    with pytest.raises(DeleteAbortedError):
        current_flask_taxonomies.delete_taxonomy(taxonomies[0])
    taxonomies = current_flask_taxonomies.list_taxonomies(session=None).all()
    assert len(taxonomies) == 1


def test_taxonomy_delete_2(app, db, taxonomy_tree):
    taxonomies = current_flask_taxonomies.list_taxonomies(session=None).all()
    assert len(taxonomies) == 1
    current_flask_taxonomies.delete_taxonomy(taxonomies[0])
    taxonomies = current_flask_taxonomies.list_taxonomies(session=None).all()
    assert len(taxonomies) == 0


def test_taxonomy_term_delete(app, db, taxonomy_tree):
    taxonomy = current_flask_taxonomies.get_taxonomy("test_taxonomy")
    terms = current_flask_taxonomies.list_taxonomy(taxonomy).all()
    term = terms[1]
    ti = TermIdentification(term=term)
    current_flask_taxonomies.delete_term(ti)


def test_taxonomy_term_delete_2(app, db, taxonomy_tree, test_record):
    taxonomy = current_flask_taxonomies.get_taxonomy("test_taxonomy")
    terms = current_flask_taxonomies.list_taxonomy(taxonomy).all()
    term = terms[1]
    ti = TermIdentification(term=term)
    with pytest.raises(DeleteAbortedError):
        current_flask_taxonomies.delete_term(ti)


def test_taxonomy_term_moved(app, db, taxonomy_tree, test_record):
    taxonomy = current_flask_taxonomies.get_taxonomy("test_taxonomy")
    terms = current_flask_taxonomies.list_taxonomy(taxonomy).all()
    old_record = Record.get_record(id_=test_record.id)
    old_taxonomy = old_record["taxonomy"]
    assert old_taxonomy == [{
        'is_ancestor': True,
        'links': {
            'self': 'http://127.0.0.1:5000/2.0/taxonomies/test_taxonomy/a'
        },
        'test': 'extra_data'
    },
        {
            'is_ancestor': True,
            'links': {
                'parent':
                    'http://127.0.0.1:5000/2.0/taxonomies/test_taxonomy/a',
                'self': 'http://127.0.0.1:5000/2.0/taxonomies/test_taxonomy/a/b'
            },
            'test': 'extra_data'
        },
        {
            'is_ancestor': False,
            'links': {
                'parent': 'http://127.0.0.1:5000/2.0/taxonomies/test_taxonomy/a/b',
                'self': 'http://127.0.0.1:5000/2.0/taxonomies/test_taxonomy/a/b/c'
            },
            'test': 'extra_data'
        }]
    ti = TermIdentification(term=terms[2])
    current_flask_taxonomies.move_term(ti, new_parent=terms[0], remove_after_delete=False)
    db.session.commit()
    new_record = Record.get_record(id_=test_record.id)
    new_taxonomy = new_record["taxonomy"]
    assert new_taxonomy == [{
        'is_ancestor': True,
        'links': {
            'self': 'http://127.0.0.1:5000/2.0/taxonomies/test_taxonomy/a'
        },
        'test': 'extra_data'
    },
        {
            'is_ancestor': False,
            'links': {
                'parent': 'http://127.0.0.1:5000/2.0/taxonomies/test_taxonomy/a',
                'self': 'http://127.0.0.1:5000/2.0/taxonomies/test_taxonomy/a/c'
            },
            'test': 'extra_data'
        }]


def test_taxonomy_term_update(app, db, taxonomy_tree, test_record):
    taxonomy = current_flask_taxonomies.get_taxonomy("test_taxonomy")
    terms = current_flask_taxonomies.list_taxonomy(taxonomy).all()
    old_record = Record.get_record(id_=test_record.id)
    assert old_record == {
        'pid': 1,
        'taxonomy': [{
                         'is_ancestor': True,
                         'links': {'self': 'http://127.0.0.1:5000/2.0/taxonomies/test_taxonomy/a'},
                         'test': 'extra_data'
                     },
                     {
                         'is_ancestor': True,
                         'links': {
                             'parent': 'http://127.0.0.1:5000/2.0/taxonomies/test_taxonomy/a',
                             'self': 'http://127.0.0.1:5000/2.0/taxonomies/test_taxonomy/a/b'
                         },
                         'test': 'extra_data'
                     },
                     {
                         'is_ancestor': False,
                         'links': {
                             'parent': 'http://127.0.0.1:5000/2.0/taxonomies/test_taxonomy/a/b',
                             'self': 'http://127.0.0.1:5000/2.0/taxonomies/test_taxonomy/a/b/c'
                         },
                         'test': 'extra_data'
                     }],
        'title': 'record 1'
    }
    term = terms[-1]
    current_flask_taxonomies.update_term(term, extra_data={"new_data": "changed extra data"})
    new_record = Record.get_record(id_=test_record.id)
    assert new_record == {
        'taxonomy': [{
            'test': 'extra_data', 'is_ancestor': True,
            'links': {'self': 'http://127.0.0.1:5000/2.0/taxonomies/test_taxonomy/a'}
        }, {
            'test': 'extra_data', 'is_ancestor': True, 'links': {
                'self': 'http://127.0.0.1:5000/2.0/taxonomies/test_taxonomy/a/b',
                'parent': 'http://127.0.0.1:5000/2.0/taxonomies/test_taxonomy/a'
            }
        }, {
            'new_data': 'changed extra data', 'is_ancestor': False, 'links': {
                'self': 'http://127.0.0.1:5000/2.0/taxonomies/test_taxonomy/a/b/c',
                'parent': 'http://127.0.0.1:5000/2.0/taxonomies/test_taxonomy/a/b'
            }
        }], 'pid': 1, 'title': 'record 1'
    }
