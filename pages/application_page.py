from seleniumbase import BaseCase


class ApplicationPage(BaseCase):

    application_count = "//*[contains(@class,'pageNumberFooter')]//*[contains(@class,'pageOptionWrapper')]//p[2]"