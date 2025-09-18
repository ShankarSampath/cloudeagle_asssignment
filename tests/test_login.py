import allure
import pytest
from allure_commons.types import AttachmentType
from seleniumbase import BaseCase
from seleniumbase.config.settings import EXTREME_TIMEOUT

from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage

class TestLoginPage(BaseCase):

    @pytest.mark.regression
    @pytest.mark.loginFeature
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('Login as Support User')
    def test_verify_that_user_is_able_to_login(self):

        LoginPage.login(self, 'support_user')
        self.wait_for_element_visible(DashboardPage.dashboard_nugget)
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name='Support User is able to Login Successfully',
            attachment_type=AttachmentType.PNG
        )
