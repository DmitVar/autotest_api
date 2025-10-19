import allure
from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from clients.users.users_schema import UpdateUserRequestSchema, GetUserResponseSchema


class PrivateUsersClient(APIClient):
    """
    Клиент для работы с /users требующие аутентификации
    """

    @allure.step('Get user me')
    def get_user_me_api(self) -> Response:
        """
        Метод возвращает сведения о пользователе.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/users/me")

    @allure.step('Get user by id {user_id}')
    def get_user_api(self, user_id: str) -> Response:
        """
        Метод возвращает сведения о пользователе по id.
        :param user_id:
        :return:Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/users/{user_id}")

    @allure.step('Update user by id {user_id}')
    def update_user_api(self, user_id: str, request: UpdateUserRequestSchema) -> Response:
        """
        Метод именяет сведения о пользователе.
        :param user_id: идентификатор пользователя
        :param request: Словарь с одним или несколькими корректируемыми параметрами из: email, lastName, firstName, middleName
        :return:Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/users/{user_id}", json=request.model_dump(by_alias=True))

    @allure.step('Delete user by id {user_id}')
    def delete_user_api(self, user_id: str) -> Response:
        """
        Метод удаляет пользователя по id.
        :param user_id: идентификатор пользователя
        :return:Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/users/{user_id}")

    def get_user(self, user_id: str) -> GetUserResponseSchema:
        """
        Метод возвращает данные о пользователе
        :param user_id: идентификатор пользователя
        :return: Словарь GetUserResponseDict
        """
        response = self.get_user_api(user_id)
        return GetUserResponseSchema.model_validate_json(response.text)


def get_private_users_client(user: AuthenticationUserSchema) -> PrivateUsersClient:
    """
    Функция создаёт экземпляр PrivateUsersClient с уже настроенным HTTP-клиентом.
    :return: Готовый к использованию PrivateUsersClient.
    """
    return PrivateUsersClient(client=get_private_http_client(user))
