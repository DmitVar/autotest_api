from httpx import Client
from pydantic import BaseModel
from typing import TypedDict

from clients.autheentication.authentication_client import AuthenticationClient, get_authenticated_client
from clients.autheentication.aunthentication_schema import LoginRequestSchema


class AuthenticationUserSchema(BaseModel):
    email: str
    password: str

def get_private_http_client(user: AuthenticationUserSchema) -> Client:
    """
    Функция создаёт экземпляр httpx.Client с аутентификацией пользователя.
    :param user: Объект AuthenticationUserSchema с email и паролем пользователя.
    :return: Готовый к использованию объект httpx.Client с установленным заголовком Authorization.
    """
    authenticated_client = get_authenticated_client()
    login_request = LoginRequestSchema(email=user.email, password=user.password)

    login_response = authenticated_client.login(login_request)
    access_token = login_response.token.access_token

    return Client(
        timeout=10,
        base_url="http://127.0.0.1:8000/api/v1",
        headers={"Authorization": f"Bearer {access_token}"},
    )