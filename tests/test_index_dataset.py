import pytest
from unittest.mock import patch
from dataset.index_dataset import process_batch


@patch("dataset.index_dataset.get_client")
@patch("dataset.index_dataset.embed_batch")
@patch("dataset.index_dataset.text_splitter.split_text")
def test_process_batch(mock_split_text, mock_embed_batch, mock_get_client):
    # Mock input batch
    batch = {
        "id": [1, 2, 3],
        "text": ["text1", "text2", "text3"],
        "url": ["url1", "url2", "url3"],
    }

    # Mock return values
    mock_split_text.return_value = [
        "text1",
        "text2",
        "text3",
    ]
    mock_embed_batch.return_value = [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]]
    mock_client = mock_get_client.return_value

    # Call the function
    result = process_batch(batch)

    # Assertions
    assert result == batch

    mock_client.insert.assert_called_once_with(
        collection_name="wikipedia",
        data=[
            {
                "article_id": 1,
                "url": "url1",
                "vector": [0.1, 0.2, 0.3],
                "text": "passage: text1",
            },
            {
                "article_id": 1,
                "url": "url1",
                "vector": [0.4, 0.5, 0.6],
                "text": "passage: text2",
            },
            {
                "article_id": 1,
                "url": "url1",
                "vector": [0.7, 0.8, 0.9],
                "text": "passage: text3",
            },
            {
                "article_id": 2,
                "url": "url2",
                "vector": [0.1, 0.2, 0.3],
                "text": "passage: text1",
            },
            {
                "article_id": 2,
                "url": "url2",
                "vector": [0.4, 0.5, 0.6],
                "text": "passage: text2",
            },
            {
                "article_id": 2,
                "url": "url2",
                "vector": [0.7, 0.8, 0.9],
                "text": "passage: text3",
            },
            {
                "article_id": 3,
                "url": "url3",
                "vector": [0.1, 0.2, 0.3],
                "text": "passage: text1",
            },
            {
                "article_id": 3,
                "url": "url3",
                "vector": [0.4, 0.5, 0.6],
                "text": "passage: text2",
            },
            {
                "article_id": 3,
                "url": "url3",
                "vector": [0.7, 0.8, 0.9],
                "text": "passage: text3",
            },
        ],
    )
