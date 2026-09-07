"""Tests für Phase 5 — RAG-Antwort."""

# TODO: Prompt-Aufbau testen (API-Call mocken)

from rag import build_prompt, get_answer
from unittest.mock import MagicMock


def test_build_prompt():

    jobs = [
        {"title": "Werkstudent Data", "description": "Testbeschreibung", "link": "https://example.com/job1"}
    ]

    query_text = "Jobs mit Python"

    prompt = build_prompt(jobs, query_text)

    assert "Werkstudent Data" in prompt
    assert "Testbeschreibung" in prompt
    assert "https://example.com/job1" in prompt
    assert "Jobs mit Python" in prompt


def test_get_answer_mock(mocker):

    mock_client = mocker.patch("rag.client")

    fake_message = MagicMock()
    fake_message.content = "Das ist eine Antwort"

    fake_choices = MagicMock()
    fake_choices.message = fake_message

    fake_response = MagicMock()
    fake_response.choices = [fake_choices]

    mock_client.chat.completions.create.return_value = fake_response

    result = get_answer("Test Prompt")

    assert result == "Das ist eine Antwort"
        



