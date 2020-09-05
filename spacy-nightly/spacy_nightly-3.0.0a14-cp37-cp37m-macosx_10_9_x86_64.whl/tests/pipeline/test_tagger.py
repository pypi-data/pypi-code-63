import pytest
from spacy import util
from spacy.gold import Example
from spacy.lang.en import English
from spacy.language import Language

from ..util import make_tempdir


def test_label_types():
    nlp = Language()
    tagger = nlp.add_pipe("tagger")
    tagger.add_label("A")
    with pytest.raises(ValueError):
        tagger.add_label(9)


def test_tagger_begin_training_tag_map():
    """Test that Tagger.begin_training() without gold tuples does not clobber
    the tag map."""
    nlp = Language()
    tagger = nlp.add_pipe("tagger")
    orig_tag_count = len(tagger.labels)
    tagger.add_label("A")
    nlp.begin_training()
    assert orig_tag_count + 1 == len(nlp.get_pipe("tagger").labels)


TAGS = ("N", "V", "J")

TRAIN_DATA = [
    ("I like green eggs", {"tags": ["N", "V", "J", "N"]}),
    ("Eat blue ham", {"tags": ["V", "J", "N"]}),
]


def test_overfitting_IO():
    # Simple test to try and quickly overfit the tagger - ensuring the ML models work correctly
    nlp = English()
    tagger = nlp.add_pipe("tagger")
    train_examples = []
    for t in TRAIN_DATA:
        train_examples.append(Example.from_dict(nlp.make_doc(t[0]), t[1]))
    for tag in TAGS:
        tagger.add_label(tag)
    optimizer = nlp.begin_training()

    for i in range(50):
        losses = {}
        nlp.update(train_examples, sgd=optimizer, losses=losses)
    assert losses["tagger"] < 0.00001

    # test the trained model
    test_text = "I like blue eggs"
    doc = nlp(test_text)
    assert doc[0].tag_ is "N"
    assert doc[1].tag_ is "V"
    assert doc[2].tag_ is "J"
    assert doc[3].tag_ is "N"

    # Also test the results are still the same after IO
    with make_tempdir() as tmp_dir:
        nlp.to_disk(tmp_dir)
        nlp2 = util.load_model_from_path(tmp_dir)
        doc2 = nlp2(test_text)
        assert doc2[0].tag_ is "N"
        assert doc2[1].tag_ is "V"
        assert doc2[2].tag_ is "J"
        assert doc2[3].tag_ is "N"


def test_tagger_requires_labels():
    nlp = English()
    nlp.add_pipe("tagger")
    with pytest.raises(ValueError):
        nlp.begin_training()
