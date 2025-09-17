import httpx

from tools.fakers import get_random_email

create_user_payload = {
    "email": get_random_email(),
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

create_files_headers = {"Authorization": f"Bearer {authentication_user_data['token']['accessToken']}"}
crete_file_response = client.post(
    "/files",
    data={"filename": "butterfly.png", "directory": "images"},
    files={"upload_file": open("./testdata/files/butterfly.png", "rb")},
    headers=create_files_headers
)
crete_file_data = crete_file_response.json()
print(crete_file_data)