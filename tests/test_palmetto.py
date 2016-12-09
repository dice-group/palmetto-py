"""Test Palmetto."""

import pytest

from palmettopy.palmetto import Palmetto
from palmettopy.exceptions import CoherenceTypeNotAvailable, EndpointDown, WrongContentType


@pytest.fixture
def words():
    """Load test data fixture."""
    words = ["cake", "apple", "banana", "cherry", "chocolate"]
    return words


@pytest.fixture
def words_underscore():
    """Load test data fixture."""
    words = ['label', 'type', 'character', 'foundation_garment']
    return words


@pytest.fixture
def words_no_results():
    """Load test data fixture."""
    words = ['label', 'type', 'character', 'subject', 'discipline', 'topic', 'national', 'familycolor', 'fam', 'glotto', 'isoexception']
    return words


def test_get_coherence(capsys, words):
    palmetto = Palmetto()
    coherence = palmetto.get_coherence(words)
    assert(coherence == 0.5678879445677241)


def test_get_coherence_fast(capsys, words):
    palmetto = Palmetto()
    coherence = palmetto.get_coherence_fast(words)
    assert(coherence == 1779.6591356383024)


def test_wrong_endpoint(words):
    palmetto = Palmetto("http://example.com/nothinghere/")
    with pytest.raises(EndpointDown):
        coherence = palmetto.get_coherence(words)


def test_wrong_coherence_type(words):
    palmetto = Palmetto()
    with pytest.raises(CoherenceTypeNotAvailable):
        coherence = palmetto.get_coherence(words, coherence_type="asdf")


def test_all_coherence_types(words):
    palmetto = Palmetto()
    for coherence_type in palmetto.all_coherence_types:
        palmetto.get_coherence(words, coherence_type=coherence_type)


def test_wrong_content_type(words):
    palmetto = Palmetto()
    with pytest.raises(WrongContentType):
        palmetto._request_by_service(words, "cv", "bla")


def test_all_content_types(words):
    palmetto = Palmetto()
    for content_type in ["text", "bytes"]:
        palmetto._request_by_service(words, "umass", content_type)


def test_get_df_for_words(words):
    palmetto = Palmetto()
    doc_ids = palmetto.get_df_for_words(words)
    for i in range(0, len(words)):
        assert(doc_ids[i][0] == words[i])


def test_get_df_for_words_underscore(words_underscore):
    """
        This test case fails for some unknown reason

        Fails. Palmetto can not handle underscores.
    """
    palmetto = Palmetto()
    doc_ids = palmetto.get_df_for_words(words_underscore)
    for i in range(0, len(words_underscore)):
        assert(doc_ids[i][0] == words_underscore[i])


def test_get_df_for_words_with_no_results(words_no_results):
    """
        This test case fails for some unknown reason

        Fails. Palmetto can not handle underscores.
    """
    palmetto = Palmetto()
    doc_ids = palmetto.get_df_for_words(words_no_results)
    for i in range(0, len(words_no_results)):
        assert(doc_ids[i][0] == words_no_results[i])

