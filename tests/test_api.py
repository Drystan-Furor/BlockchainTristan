def test_blocks(client, app):
    assert client.get('/api/v1/blocks').status_code == 200