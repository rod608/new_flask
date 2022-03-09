"""This test the homepage"""


def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a href="/git" class="nav-link">Git</a>' in response.data
    assert b'<a href="/docker" class="nav-link">Docker</a>' in response.data
    assert b'<a href="/flask" class="nav-link">Flask</a>' in response.data


def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Rod's Mods" in response.data


def test_request_git(client):
    """This makes the git page"""
    response = client.get("/git")
    assert response.status_code == 200
    assert b"Git & GitHub" in response.data


def test_request_docker(client):
    """This makes the docker page"""
    response = client.get("/docker")
    assert response.status_code == 200
    assert b"Containerization vs Virtualization" in response.data


def test_request_flask(client):
    """This makes the flask page"""
    response = client.get("/flask")
    assert response.status_code == 200
    assert b"PyTests" in response.data


def test_request_cicd(client):
    """This makes the CICD page"""
    response = client.get("/cicd")
    assert response.status_code == 200
    assert b"Continuous Integration & Deployment" in response.data


def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 404
