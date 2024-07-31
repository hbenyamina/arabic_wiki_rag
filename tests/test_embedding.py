import pytest
from unittest.mock import patch
from utils.embedding import embed_batch


@patch("utils.embedding.requests.post")
def test_embed_batch(mock_post):
    # Mock response from the API
    mock_response = {"embeddings": [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]]}

    # Configure the mock response
    mock_post.return_value.json.return_value = mock_response

    # Test case
    text_batch = ["text1", "text2", "text3"]
    result = embed_batch(text_batch)

    # Assertions
    assert result == mock_response
    mock_post.assert_called_once_with(
        "http://127.0.0.1:8080/embed",
        headers={"Content-Type": "application/json"},
        json={"inputs": text_batch},
    )
