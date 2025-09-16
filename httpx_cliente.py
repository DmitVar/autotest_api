import httpx


authentication_user_payload = {
    "email": "user@example.com",
    "password": "string"
}

authentication_user_response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login", json=authentication_user_payload)
authentication_user_data = authentication_user_response.json()

#Настройка httpx клиента
client = httpx.Client(
    base_url="http://127.0.0.1:8000/api/v1",
    timeout=10,
    headers={"Authorization": f"Bearer {authentication_user_data['token']['accessToken']}"}
)
#использование httpx клиента

user_me_response = client.get("/users/me")
users_me_data = user_me_response.json()
print(users_me_data)

