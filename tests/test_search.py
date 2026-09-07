"""Tests für Phase 4 — Vector Search."""

# TODO: Similarity-Berechnung mit festen Beispiel-Vektoren testen

from search import calc_cosine_similarity
import numpy as np


def test_cosine_similarity_identical():
    assert np.isclose(calc_cosine_similarity([1, 2, 3], [1, 2, 3]), 1.0)

def test_cosine_similarity_orthogonal():
    assert np.isclose(calc_cosine_similarity([1, 0], [0, 1]), 0.0)

def test_cosine_similarity_opposite():
    assert np.isclose(calc_cosine_similarity([1, 1], [-1, -1]), -1.0)