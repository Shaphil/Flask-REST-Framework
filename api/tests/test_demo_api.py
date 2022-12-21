"""
Demo API tests
"""


def test_demo_api_returns_demo_text(client):
    response = client.get('/api/demo')
    data = b'Welcome to Flask-REST-Framework'
    assert data in response.data
