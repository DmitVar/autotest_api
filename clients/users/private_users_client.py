from httpx import Response
from typing import TypedDict

from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserDict


class UpdateUserRequestDict(TypedDict):
    """ Описание структуры запроса редактирования пользователя."""
    email: str | None
    lastName: str | None
    firstName: str | None
    middleName: str | None

class User(TypedDict):
    """Описание структуры пользователя."""
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str

class GetUserResponseDict(TypedDict):
    """Описание структуры ответа создания пользователя."""
    user: User

class PrivateUsersClient(APIClient):
    """
    Клиент для работы с /users требующие аутентификации
    """
    def get_user_me_api(self) -> Response:
        """
        Метод возвращает сведения о пользователе.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/users/me")

    def get_user_api(self, user_id: str) -> Response:
        """
        Метод возвращает сведения о пользователе по id.
        :param user_id:
        :return:Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/users/{user_id}")

    def update_user_api(self, user_id: str, request) -> Response:
        """
        Метод именяет сведения о пользователе.
        :param user_id: идентификатор пользователя
        :param request: Словарь с одним или несколькими корректируемыми параметрами из: email, lastName, firstName, middleName
        :return:Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/users/{user_id}", json=request)

    def delete_user_api(self, user_id: str) -> Response:
        """
        Метод удаляет пользователя по id.
        :param user_id: идентификатор пользователя
        :return:Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/users/{user_id}")

    def get_user(self, user_id: str) -> GetUserResponseDict:
        """
        Метод возвращает данные о пользователе
        :param user_id: идентификатор пользователя
        :return: Словарь GetUserResponseDict
        """
        response = self.get_user_api(user_id)
        return response.json()

def get_private_users_client(user: AuthenticationUserDict) -> PrivateUsersClient:
    """
    Функция создаёт экземпляр PrivateUsersClient с уже настроенным HTTP-клиентом.
    :return: Готовый к использованию PrivateUsersClient.
    """
    return PrivateUsersClient(client=get_private_http_client(user))