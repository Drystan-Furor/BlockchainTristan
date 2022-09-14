from blockchain import create_app

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

def test_healthz(client):
    response = client.get('/healthz')
    assert response.data == b'healthy'