"""Tests für Phase 3 — Embeddings."""

# TODO: API-Call mocken, Rückgabeform testen


from embeddings import get_embedding

from unittest.mock import MagicMock

def test_get_embedding(mocker):

   mock_client = mocker.patch ("embeddings.client")

   fake_vector = [0.2, 0.3, 0.4]

   fake_data_item = MagicMock()
   fake_data_item.embedding = fake_vector

   fake_response = MagicMock()
   fake_response.data = [fake_data_item]

   mock_client.embeddings.create.return_value = fake_response

   result = get_embedding("Testtext")

   assert result == fake_vector

   
