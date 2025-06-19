import pytest
from unittest.mock import patch, MagicMock
from src import inference


@pytest.fixture
def mock_llm():
    with patch("src.inference.llm") as mock:
        mock.return_value = {"choices": [{"text": "mocked"}]}
        yield mock


def test_run_prompt(mock_llm: MagicMock):
    result = inference.run_prompt("Hello", 5)
    assert result == "mocked"
