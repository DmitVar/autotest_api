from httpx import Client
from typing import TypedDict

from clients.autheentication.authentication_client import AuthenticationClient, LoginRequestDict, \
    get_authenticated_client


class AuthenticationUserDict(TypedDict):
    email: str
    password: str

def get_private_http_client(user: AuthenticationUserDict) -> Client:
    """
    Функция создаёт экземпляр httpx.Client с аутентификацией пользователя.
    :param user: Объект AuthenticationUserSchema с email и паролем пользователя.
    :return: Готовый к использованию объект httpx.Client с установленным заголовком Authorization.
    """
    authenticated_client = get_authenticated_client()
    login_request = LoginRequestDict(email=user['email'], password=user['password'])

    login_response = authenticated_client.login(login_request)
    access_token = login_response['token']['accessToken']

    return Client(
        timeout=10,
        base_url="http://127.0.0.1:8000/api/v1",
        headers={"Authorization": f"Bearer {access_token}"},
    )