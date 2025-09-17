from httpx import Response
from typing import TypedDict

from clients.api_client import APIClient

class GetCoursesQueryDict(TypedDict):
    """Описание структуры запроса на получение списка курсов."""
    userId: str

class CreateCoursesRequestDict(TypedDict):
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

    def create_courses_api(self, request: CreateCoursesRequestDict) -> Response:
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