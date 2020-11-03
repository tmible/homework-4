import os

from tests.default import Test
from pages.virusmusic.profile.settings import SettingsPage
from constants import NEW_PASSWORD_ERROR, NEW_PASSWORD_ERROR_LENGTH_MESSAGE
from utils import wait_for_element_attribute_change

class LengthPasswordChangeTest(Test):
    NEW_PASSWORD = 'l'
    NEW_PASSWORD_CONFIRM = 'l'
    PASSWORD = os.environ['PASSWORD']

    def test(self):
        page = SettingsPage(self.driver)
        page.change_password(
            self.NEW_PASSWORD,
            self.NEW_PASSWORD_CONFIRM,
            self.PASSWORD
        )
        wait_for_element_attribute_change(
            self.driver,
            NEW_PASSWORD_ERROR,
            'innerText',
            NEW_PASSWORD_ERROR_LENGTH_MESSAGE
        )
