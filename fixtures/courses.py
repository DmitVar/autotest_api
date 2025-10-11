import pytest
from pydantic import BaseModel

from clients.courses.courses_client import CourseClient, get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema, CreateCourseResponseSchema
from fixtures.files import FileFixture
from fixtures.users import UserFixture


class CourseFixture(BaseModel):
    request: CreateCourseRequestSchema
    response: CreateCourseResponseSchema

@pytest.fixture
def courses_client(function_user: UserFixture) -> CourseClient:
    return get_courses_client(function_user.authentication_user)

def function_course(
        courses_client: CourseClient,
        function_user: UserFixture,
        function_file: FileFixture
) -> CourseFixture:
    request = CreateCourseRequestSchema()
    response = courses_client.create_course(request)
    return CourseFixture(request=request, response=response)

