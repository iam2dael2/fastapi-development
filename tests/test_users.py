import pytest
from app import schema
from jose import jwt
from app.config import settings

# def test_root(client):
#     response = client.get("/")
#     assert response.status_code == 200
#     assert response.json().get("message") == "Hello World!"

def test_create_user(client):
    response = client.post("/users", json={"email": "hello123@gmail.com", "password": "password123"})
    
    new_user = schema.User(**response.json())
    assert new_user.email == "hello123@gmail.com"
    assert response.status_code == 201

def test_login_user(test_user, client):
    res = client.post("/login", data={"username": test_user["email"], "password": test_user["password"]})
    login_res = schema.Token(**res.json())

    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=settings.algorithm)
    id  = payload.get("user_id")
    
    assert id == test_user["id"]
    assert login_res.token_type == "bearer"
    assert res.status_code == 200

@pytest.mark.parametrize("email, password, status_code", [
    ('wrongemail@gmail.com', 'password123', 403),
    ('darell@gmail.com', 'wrongpassword', 403),
    ('wrongemail@gmail.com', 'wrongpassword', 403),
    (None, 'password123', 403),
    ('darell@gmail.com', None, 403)
])
def test_incorrect_login(test_user, client, email, password, status_code):
    res = client.post("/login", data={"username": email, "password": password})
    assert res.status_code == status_code