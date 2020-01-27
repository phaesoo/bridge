def test_connect(client):
    assert client.is_connected() is True
    print (client.get_received())