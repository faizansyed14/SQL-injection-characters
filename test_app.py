import app
import pytest
import json

@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        yield client

def test_check_sanitization_sanitize(client):
    payload = json.dumps({"input": "This is a safe input"})
    response = client.post('/input', data=payload, content_type='application/json')
    data = json.loads(response.data.decode())
    assert response.status_code == 200
    assert data['result'] == "sanitized"

def test_check_sanitization_unsanitize(client):
    payload = json.dumps({"input": "This is an unsafe input DROP TABLE users"})
    response = client.post('/input', data=payload, content_type='application/json')
    data = json.loads(response.data.decode())
    assert response.status_code == 200
    assert data['result'] == "unsanitized"

def test_check_sanitization_missing_input(client):
    payload = json.dumps({"data": "This is a test"})
    response = client.post('/input', data=payload, content_type='application/json')
    data = json.loads(response.data.decode())
    assert response.status_code == 400
    assert "error" in data

if __name__ == '__main__':
    pytest.main()

