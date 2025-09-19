from httpx import Response
from typing import TypedDict

from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserDict
from clients.files.files_client import File
from clients.users.private_users_client import User


class GetCoursesQueryDict(TypedDict):
    """Описание структуры запроса на получение списка курсов."""
    userId: str

class CreateCourseRequestDict(TypedDict):
    """Описание структуры запроса на создание курса."""
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str
    previewFileId: str
    createdByUserId: str

class UpdateCoursesRequestDict(TypedDict):
    """Описание структуры запроса на обновление курса."""
    title: str
    maxScore: int
    minScore: int
    description: str
    description: str
    estimatedTime: str


class Course(TypedDict):
    """Описание структуры курса."""
    id: str
    title: str
    maxScore: int
    minScore: int
    description: str
    previewFile: File
    estimatedTime: str
    createdByUser: User


class CreateCourseResponseDict(TypedDict):
    """Описание структуры ответа создания курса"""
    course: Course


class CourseClient(APIClient):
    """
    Клиент для работы с /courses
    """

    def get_courses_api(self, query: GetCoursesQueryDict) -> Response:
        """
        Метод получения списка курсов.
        :param query: Словарь с userId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/courses", params=query)

    def get_course_api(self, course_id: str) -> Response:
        """
        Метод получения курса.
        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f'/courses/{course_id}')

    def create_courses_api(self, request: CreateCourseRequestDict) -> Response:
        """
        Метод создания курса.
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime,
        previewFileId, createdByUserId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/courses", json=request)

    def update_course_api(self, request: UpdateCoursesRequestDict, curse_id: str) -> Response:
        """
        Метод обновления курса.
        :param course_id: Идентификатор курса.
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f'/courses/{curse_id}', json=request)

    def delete_courses_api(self, curse_id: str) -> Response:
        """
        Метод удаления курса.
        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f'/courses/{curse_id}')

    def create_course(self, request: CreateCourseRequestDict)->CreateCourseResponseDict:
        """
        Метод создает курс.
        :param request:
        :return:
        """
        response = self.create_courses_api(request)
        return response.json()

def get_courses_client(user: AuthenticationUserDict) -> CourseClient:
    """
    Функция создаёт экземпляр CoursesClient с уже настроенным HTTP-клиентом.
    :return: Готовый к использованию CoursesClient.
    """
    return CourseClient(client=get_private_http_client(user))