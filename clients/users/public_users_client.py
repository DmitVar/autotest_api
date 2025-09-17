from httpx import Response
from typing import TypedDict

from clients.api_client import APIClient



class CreateUserMeRequestDict(TypedDict):
    """ Описание структуры запроса создания пользователя."""
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class UsersClient(APIClient):
    """
    Клиент для работы с /users
    """

    def create_user_api(self, request: CreateUserMeRequestDict) -> Response:
        """
        Метод выполняет создание пользователя.
        :param request: Словарь с email, password, lastName, firstName, middleName.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url="/users", json=request)

