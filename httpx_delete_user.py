import httpx

from tools.fakers import fake

create_user_payload = {
    "email": fake.email(),
    "password": "password",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
client = httpx.Client(base_url="http://127.0.0.1:8000/api/v1") #

create_user_response = client.post("/users", json=create_user_payload)
create_user_data = create_user_response.json()

authentication_user_payload = {
    "email": create_user_payload["email"],
    "password": create_user_payload["password"]
}
authentication_user_response = client.post("/authentication/login", json=authentication_user_payload)
authentication_user_data = authentication_user_response.json()

headers = {"Authorization": f'Bearer {authentication_user_data["token"]["accessToken"]}'}
delete_user_response = client.delete(f"/users/{create_user_data['user']['id']}", headers=headers)

print(delete_user_response.status_code)
