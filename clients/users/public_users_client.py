from httpx import Response
from typing import TypedDict

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client


class CreateUserRequestDict(TypedDict):
    """ Описание структуры запроса создания пользователя."""
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class User(TypedDict):
    """Описание структуры пользователя."""
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str

class CreateUserResponseDict(TypedDict):
    """Описание структуры ответа создания пользователя."""
    user: User

class PublicUsersClient(APIClient):
    """
    Клиент для работы с /users
    """

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Метод выполняет создание пользователя.
        :param request: Словарь с email, password, lastName, firstName, middleName.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url="/users", json=request)

    def create_user(self, request: CreateUserRequestDict) -> CreateUserResponseDict:
        """
        Метод выполняет формирование ланных о созданном пользователе
        :param request: Словарь с email, password, lastName, firstName, middleName.
        :return: Словарь CreateUserResponseDict
        """
        response = self.create_user_api(request)
        return response.json()


def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.
    :return: Готовый к использованию PublicUsersClient.
    """
    return PublicUsersClient(client=get_public_http_client())
