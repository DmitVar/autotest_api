import allure
import pytest
from http import HTTPStatus
from allure_commons.types import Severity

from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_schema import CreateExerciseRequestShema, CreateExerciseResponseShema, \
    GetExerciseResponseSchema, UpdateExerciseRequestSchema, UpdateExerciseResponseShema, GetExercisesQuerySchema, \
    GetExercisesResponseSchema
from fixtures.courses import CourseFixture
from fixtures.exercises import ExerciseFixture
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTags
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import assert_create_exercise_response, assert_get_exercise_response, \
    assert_update_exercise_response, assert_exercise_not_found_response, assert_get_exercises_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.exercises
@pytest.mark.regression
@allure.tag(AllureTags.EXERCISES, AllureTags.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.parent_suite(AllureEpic.LMS)
@allure.feature(AllureFeature.EXERCISES)
@allure.suite(AllureFeature.EXERCISES)
class TestExercises:
    @allure.title('Create exercise')
    @allure.tag(AllureTags.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.sub_suite(AllureStory.CREATE_ENTITY)
    @allure.severity(Severity.BLOCKER)
    def test_create_exercise(
            self,
            exercises_client: ExercisesClient,
            function_course: CourseFixture
    ):
        request = CreateExerciseRequestShema(course_id=function_course.response.course.id)
        response = exercises_client.create_exercise_api(request)
        response_data = CreateExerciseResponseShema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_exercise_response(request, response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.title('Get exercise')
    @allure.tag(AllureTags.GET_ENTITY)
    @allure.story(AllureStory.GET_ENTITY)
    @allure.sub_suite(AllureStory.GET_ENTITY)
    @allure.severity(Severity.BLOCKER)
    def test_get_exercise(
            self,
            exercises_client: ExercisesClient,
            function_exercises: ExerciseFixture
    ):
        response = exercises_client.get_exercise_api(function_exercises.response.exercise.id)
        response_data = GetExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_exercise_response(response_data, function_exercises.response)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.title('Update exercise')
    @allure.tag(AllureTags.UPDATE_ENTITY)
    @allure.story(AllureStory.UPDATE_ENTITY)
    @allure.sub_suite(AllureStory.UPDATE_ENTITY)
    @allure.severity(Severity.CRITICAL)
    def test_update_exercise(
            self,
            exercises_client: ExercisesClient,
            function_exercises: ExerciseFixture
    ):
        request = UpdateExerciseRequestSchema()
        response = exercises_client.update_exercise_api(function_exercises.response.exercise.id, request)
        response_data = UpdateExerciseResponseShema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_exercise_response(response_data, request)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.title('Delete exercise')
    @allure.tag(AllureTags.DELETE_ENTITY)
    @allure.story(AllureStory.DELETE_ENTITY)
    @allure.sub_suite(AllureStory.DELETE_ENTITY)
    @allure.severity(Severity.NORMAL)
    def test_delete_exercise(
            self,
            exercises_client: ExercisesClient,
            function_exercises: ExerciseFixture
    ):
        exercise_id = function_exercises.response.exercise.id
        delete_response = exercises_client.delete_exercise_api(exercise_id)
        assert_status_code(delete_response.status_code, HTTPStatus.OK)

        get_response = exercises_client.get_exercise_api(exercise_id)
        assert_status_code(get_response.status_code, HTTPStatus.NOT_FOUND)
        get_response_data = InternalErrorResponseSchema.model_validate_json(get_response.text)
        assert_exercise_not_found_response(get_response_data)
        validate_json_schema(get_response.json(), get_response_data.model_json_schema())

    @allure.title('Get exercises by course id')
    @allure.tag(AllureTags.GET_ENTITY)
    @allure.story(AllureStory.GET_ENTITY)
    @allure.sub_suite(AllureStory.GET_ENTITY)
    @allure.severity(Severity.BLOCKER)
    def test_get_exercises(
            self,
            exercises_client: ExercisesClient,
            function_course: CourseFixture,
            function_exercises: ExerciseFixture,
    ):
        query = GetExercisesQuerySchema(course_id=function_course.response.course.id)
        response = exercises_client.get_exercises_api(query)
        response_data = GetExercisesResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_exercises_response(response_data, [function_exercises.response])
        validate_json_schema(response.json(), response_data.model_json_schema())
