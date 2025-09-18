import allure
import pytest
from allure_commons.types import AttachmentType
from seleniumbase import BaseCase
from seleniumbase.config.settings import EXTREME_TIMEOUT

from pages.application_page import ApplicationPage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage

class TestDashboard(BaseCase):

    @pytest.mark.regression
    @pytest.mark.dashboardFeature
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('Login as Support User')
    def test_verify_that_user_is_able_verify_dashboard_page(self):
        LoginPage.login(self, 'support_user')
        get_app_count_from_dashboard = int(self.get_text(DashboardPage.get_managed_application_count))
        self.click(DashboardPage.get_managed_application_count)
        self.wait(5)
        app_count = self.get_text(ApplicationPage.application_count)
        app_count_application_page = int(''.join(filter(str.isdigit, app_count)))
        self.assert_equal(get_app_count_from_dashboard,app_count_application_page)
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name='Dashboard Page & Application Page Count Validated Successfully',
            attachment_type=AttachmentType.PNG
        )
