import json
from seleniumbase import BaseCase
from data.config import BASE_URL


class LoginPage(BaseCase):
    email_textbox = "//*[@name ='emailField']"
    password_textbox = "//*[@name ='passField']"
    signin_button = "//*[contains(@class,'signInButton')]//*[text()='Sign in']"
    validation_alert = "//*[text()='Wrong username or password']"
    existing_user_alert = "//*[contains(@class,'MuiBox-root')]//*[text()='User lofad49377@mustbeit.com already exists']"

    def login(self, privilege):
        """
            page:
            privilege:
        """
        with open("data/login_data.json",
                  encoding='utf-8') as f:
            data = json.loads(f.read())

        if privilege not in data:
            return False

        self.open(BASE_URL)
        self.maximize_window()
        self.send_keys(LoginPage.email_textbox, data[privilege]["username"])
        self.send_keys(LoginPage.password_textbox, data[privilege]["password"])
        self.click(LoginPage.signin_button)
        self.wait(10)
        return True
