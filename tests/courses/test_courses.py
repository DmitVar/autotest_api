import pytest
import allure
from http import HTTPStatus
from allure_commons.types import Severity

from clients.courses.courses_client import CourseClient
from clients.courses.courses_schema import UpdateCoursesRequestSchema, UpdateCourseResponseSchema, \
    GetCoursesQuerySchema, GetCoursesResponseSchema, CreateCourseRequestSchema, CreateCourseResponseSchema
from fixtures.courses import CourseFixture
from fixtures.files import FileFixture
from fixtures.users import function_user, UserFixture
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTags
from tools.assertions.base import assert_status_code
from tools.assertions.courses import assert_update_course_response, assert_get_courses_response, \
    assert_create_course_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTags.COURSES, AllureTags.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.parent_suite(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.suite(AllureFeature.COURSES)
class TestCourses:
    @allure.title('Create course')
    @allure.tag(AllureTags.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.sub_suite(AllureStory.CREATE_ENTITY)
    @allure.severity(Severity.BLOCKER)
    def test_create_course(
            self,
            courses_client: CourseClient,
            function_user: UserFixture,
            function_file: FileFixture
    ):
        request = CreateCourseRequestSchema(
            created_by_user_id=function_user.response.user.id,
            preview_file_id=function_file.response.file.id
        )
        response = courses_client.create_courses_api(request)
        response_data = CreateCourseResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_course_response(response_data, request)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.title('Get courses by user id')
    @allure.tag(AllureTags.GET_ENTITY)
    @allure.story(AllureStory.GET_ENTITY)
    @allure.sub_suite(AllureStory.GET_ENTITY)
    @allure.severity(Severity.BLOCKER)
    def test_get_courses(
            self,
            courses_client: CourseClient,
            function_user: UserFixture,
            function_course: CourseFixture,
    ):
        query = GetCoursesQuerySchema(user_id=function_user.response.user.id)
        response = courses_client.get_courses_api(query)
        response_data = GetCoursesResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_courses_response(response_data, [function_course.response])
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.title('Update course')
    @allure.tag(AllureTags.UPDATE_ENTITY)
    @allure.story(AllureStory.UPDATE_ENTITY)
    @allure.sub_suite(AllureStory.UPDATE_ENTITY)
    @allure.severity(Severity.CRITICAL)
    def test_update_course(self, courses_client: CourseClient, function_course: CourseFixture):
        request = UpdateCoursesRequestSchema()
        response = courses_client.update_course_api(request, function_course.response.course.id)
        response_data = UpdateCourseResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_course_response(request, response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())
