"""This test the homepage"""


def test_request_example(client):
    """This tests the index page"""
    response = client.get("/")
    assert b"Rod's Mods" in response.data
