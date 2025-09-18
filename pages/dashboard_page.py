from seleniumbase import BaseCase


class DashboardPage(BaseCase):

    dashboard_nugget = "//h2[text()='Dashboard']"
    get_managed_application_count = "(//*[contains(@class,'manageApplications')]//h1[contains(@class,'countText')])[1]"
    #get_managed_application_count= "((//*[contains(@class,'cardTitleWrapper')])[1]/following::*[contains(@class,'style_textTransform')])[1]"

    def managed_applications(self):
        self.click(DashboardPage.get_managed_application_count)
        