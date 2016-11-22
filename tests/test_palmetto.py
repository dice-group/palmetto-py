"""Test Palmetto."""

import pytest

from palmettopy.palmetto import Palmetto
from palmettopy.exceptions import CoherenceTypeNotAvailable, EndpointDown


@pytest.fixture
def words():
    """Load test data fixture."""
    words = ["cake", "apple", "banana", "cherry", "chocolate"]
    return words


def test_get_coherence(capsys, words):
    palmetto = Palmetto()
    coherence = palmetto.get_coherence(words)
    assert(coherence == 0.5678879445677241)

def test_get_coherence_fast(capsys, words):
    palmetto = Palmetto()
    coherence = palmetto.get_coherence_fast(words)
    assert(coherence == 50)

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
