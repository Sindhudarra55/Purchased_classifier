from purchase_classify import app
import pytest
import json

@pytest.fixture
def client():
    return app.test_client()

def test_pinger(client):
    resp = client.get('/ping')
    assert resp.status_code == 200
    assert resp.json == {"MESSAGE": "Hi I am pinging V2...."}

def test_predictions(client):
    test_data = {
        "Gender":"Male",
        "Age":"26",
        "Income":50000
        }
    resp = client.post('/predict', json= test_data)
    assert resp.status_code == 200
    assert resp.json == {"purchase_status": 'no'}