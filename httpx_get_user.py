import httpx

from tools.fakers import get_random_email

payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

response_create_user = httpx.post('http://127.0.0.1:8000/api/v1/users', json=payload)
create_user_data = response_create_user.json()
print(create_user_data)


payload_authentication = {
    "email": create_user_data['user']['email'],
    "password": create_user_data['user']['password']
}

response_authentication = httpx.post('http://127.0.0.1:8000/api/v1/authentication/login', json=payload_authentication)
authentication_data = response_authentication.json()
print(authentication_data)

headers = {"Authorization": f'Bearer {authentication_data["token"]["accessToken"]}'}
response_users = httpx.get(f'http://127.0.0.1:8000/api/v1/users/{create_user_data["user"]["id"]}', headers=headers)
user_data = response_users.json()
print(user_data)