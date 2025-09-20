from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from clients.courses.courses_schema import GetCoursesQuerySchema, CreateCourseRequestSchema, UpdateCoursesRequestSchema, CreateCourseResponseSchema

class CourseClient(APIClient):
    """
    Клиент для работы с /courses
    """

    def get_courses_api(self, query: GetCoursesQuerySchema) -> Response:
        """
        Метод получения списка курсов.
        :param query: Словарь с userId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/courses", params=query.model_dump(by_alias=True))

    def get_course_api(self, course_id: str) -> Response:
        """
        Метод получения курса.
        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f'/courses/{course_id}')

    def create_courses_api(self, request: CreateCourseRequestSchema) -> Response:
        """
        Метод создания курса.
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime,
        previewFileId, createdByUserId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/courses", json=request.model_dump(by_alias=True))

    def update_course_api(self, request: UpdateCoursesRequestSchema, curse_id: str) -> Response:
        """
        Метод обновления курса.
        :param course_id: Идентификатор курса.
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f'/courses/{curse_id}', json=request.model_dump(by_alias=True))

    def delete_courses_api(self, curse_id: str) -> Response:
        """
        Метод удаления курса.
        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f'/courses/{curse_id}')

    def create_course(self, request: CreateCourseRequestSchema)->CreateCourseResponseSchema:
        """
        Метод создает курс.
        :param request:
        :return:
        """
        response = self.create_courses_api(request)
        return CreateCourseResponseSchema.model_validate_json(response.text)

def get_courses_client(user: AuthenticationUserSchema) -> CourseClient:
    """
    Функция создаёт экземпляр CoursesClient с уже настроенным HTTP-клиентом.
    :return: Готовый к использованию CoursesClient.
    """
    return CourseClient(client=get_private_http_client(user))