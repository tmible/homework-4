from tests.virusmusic.default import Test
from pages.virusmusic.profile.settings import SettingsPage
from constants import PASSWORD_ERROR, PASSWORD_ERROR_NO_OLD_MESSAGE
from utils import wait_for_element_attribute_change

class NoOldPasswordChangeTest(Test):
    NEW_PASSWORD = 'lol'
    NEW_PASSWORD_CONFIRM = 'lol'
    PASSWORD = ''

    def test(self):
        page = SettingsPage(self.driver)
        page.change_password(
            self.NEW_PASSWORD,
            self.NEW_PASSWORD_CONFIRM,
            self.PASSWORD
        )
        wait_for_element_attribute_change(
            self.driver,
            PASSWORD_ERROR,
            'innerText',
            PASSWORD_ERROR_NO_OLD_MESSAGE
        )
