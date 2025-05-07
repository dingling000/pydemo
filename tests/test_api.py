from pathlib import Path
import pytest

def test_hello(client):
    response = client.get('/hello')
    assert response.status_code == 200

def test_text_translation(client):
    data = {
        "text": "how are you?",
        "from": "en",
        "to": "jp"
    }
    response = client.post('/text', json=data)
    assert response.status_code == 200

def test_image_translation(client):
    form = {
        "from": "en",
        "to": "zh",
        "image": (Path(__file__).parent / "test.png").open("rb")
    }
    response = client.post('/image', data=form)
    assert response.status_code == 200