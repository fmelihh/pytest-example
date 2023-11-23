import pytest
import requests
import unittest.mock as mock
import source.service as service


@mock.patch("source.service.database")
def test_get_user_from_db(mock_db: mock.MagicMock):
    mock_db.get.return_value = "Mocked Alice"
    username = service.get_user_from_db(1)

    assert username == "Mocked Alice"


@mock.patch("requests.get")
def test_get_users(mock_get: mock.MagicMock):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "name": "Furki"}
    mock_get.return_value = mock_response
    data = service.get_users_from_api()
    assert data == {"id": 1, "name": "Furki"}


@mock.patch("requests.get")
def test_get_user_status_code_not_eq_200(mock_get: mock.MagicMock):
    mock_response = mock.Mock()
    mock_response.status_code = 500
    mock_get.return_value = mock_response

    with pytest.raises(requests.HTTPError):
        service.get_users_from_api()
