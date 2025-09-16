from httpx import Request, Response

from clients.api_client import APIClient
from typing import TypedDict



class LoginRequestDict(TypedDict):
    """Описание структуры запроса на аутентификацию."""
    email: str
    password: str

class RefreshRequestDict(TypedDict):
    """Описание структуры запроса для обновления токена."""
    refreshToken: str



class AuthenticationClient(APIClient):
    """
    Клиент для работы с /authentication

    """
    def login_api(self, request: LoginRequestDict) -> Response:
        """
        Метод выполняет аутентификацию пользователя.
        :param request: Словарь с email и password.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/authentication/login", json=request)

    def refresh_api(self, request: RefreshRequestDict) -> Response:
        """
        Метод обновляет токен авторизации.
        :param request: Словарь с refreshToken.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/authentication/refresh", json=request)