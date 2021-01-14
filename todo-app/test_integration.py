import pytest
import requests
from dotenv import find_dotenv, load_dotenv
from app import create_app

class mockup(object):
    def __init__(self,json):
        self.responseJSON = json
    def json(self):
        return self.responseJSON

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('todo-app/.env.test')
    load_dotenv(file_path, override=True)
    # Create the new app.
    test_app = create_app()
    # Use the app to create a test_client that can be used in our tests.
    
    with test_app.test_client() as client:
        yield client


def test_index_page(monkeypatch, client):
    # Arrange
    def mockget(url, params):
        return mockup(
            [
                {
                    "name": "Durnan",
                    "id": "001",
                    "desc": "desc1",
                    "due": "2021-01-14T16:00:00.000000Z",
                    "dateLastActivity": "2020-12-01T09:00:00.000000Z",
                    "idList": "todo"
                }
            ])
    monkeypatch.setattr(requests, "get", mockget)
    # Act
    response = client.get('/')
    # Assert
    assert response.status_code == 200
    # assert "Durnan" in response.data
    

