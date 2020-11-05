import os

from tests.virusmusic.default import Test
from pages.virusmusic.profile.settings import SettingsPage
from utils import wait_for_pop_up

class ValidPasswordChangeTest(Test):
    NEW_PASSWORD = 'lolkek'
    NEW_PASSWORD_CONFIRM = 'lolkek'
    PASSWORD = os.environ['PASSWORD']

    def test(self):
        page = SettingsPage(self.driver)
        page.change_password(
            self.NEW_PASSWORD,
            self.NEW_PASSWORD_CONFIRM,
            self.PASSWORD
        )
        wait_for_pop_up(self.driver)

    def tearDown(self):
        page = SettingsPage(self.driver)
        page.change_password(
            self.PASSWORD,
            self.PASSWORD,
            self.NEW_PASSWORD
        )
        wait_for_pop_up(self.driver)
        super().tearDown()
