from httpx import Response
from typing import TypedDict

from clients.api_client import APIClient

class UpdateUserRequestDict(TypedDict):
    """ Описание структуры запроса редактирования пользователя."""
    email: str | None
    lastName: str | None
    firstName: str | None
    middleName: str | None

class PrivateUsersClient(APIClient):
    """
    Клиент для работы с /users требующие аутентификации
    """
    def get_get_user_me_api(self) -> Response:
        """
        Метод возвращает сведения о пользователе.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/users/me")

    def get_get_user_api(self, user_id: str) -> Response:
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
        :param user_id:
        :return:Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/users/{user_id}")
