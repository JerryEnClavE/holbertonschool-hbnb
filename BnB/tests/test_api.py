def test_create_place(client):
    response = client.post('/places', json={"name": "Test Place", "location": "Test Location", "capacity": 4})
    assert response.status_code == 201
    assert 'id' in response.json
