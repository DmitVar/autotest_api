from http import HTTPStatus

from clients.autheentication.authentication_client import get_authenticated_client
from clients.users.public_users_client import get_public_users_client
from clients.autheentication.aunthentication_schema import LoginRequestSchema, LoginResponseSchema
from clients.users.users_schema import CreateUserRequestSchema
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from clients.autheentication.authentication import assert_login_response


def test_login():
    public_users_client = get_public_users_client()
    user_authentication_client = get_authenticated_client()

    create_user_request = CreateUserRequestSchema()
    public_users_client.create_user(create_user_request)

    login_request = LoginRequestSchema(
        email=create_user_request.email,
        password=create_user_request.password
    )
    login_response = user_authentication_client.login_api(login_request)
    login_response_data = LoginResponseSchema.model_validate_json(login_response.text)

    assert_status_code(login_response.status_code, HTTPStatus.OK)
    assert_login_response(login_response_data)

    validate_json_schema(login_response.json(), login_response_data.model_json_schema())
