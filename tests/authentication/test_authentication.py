import pytest
import allure
from http import HTTPStatus
from allure_commons.types import Severity

from clients.authentication.authentication_client import AuthenticationClient
from clients.authentication.aunthentication_schema import LoginRequestSchema, LoginResponseSchema
from fixtures.users import UserFixture
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTags
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from clients.authentication.authentication import assert_login_response


@pytest.mark.regression
@pytest.mark.authentication
@allure.tag(AllureTags.AUTHENTICATION, AllureTags.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.parent_suite(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.suite(AllureFeature.AUTHENTICATION)
class TestAuthentication:
    @allure.title('Login')
    @allure.story(AllureStory.LOGIN)
    @allure.sub_suite(AllureStory.LOGIN)
    @allure.severity(Severity.BLOCKER)
    def test_login(self, function_user: UserFixture, authentication_client: AuthenticationClient):
        request = LoginRequestSchema(
            email=function_user.email,
            password=function_user.password
        )
        response = authentication_client.login_api(request)
        response_data = LoginResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_login_response(response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())
