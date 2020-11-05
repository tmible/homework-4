from tests.virusmusic.default import Test
from pages.virusmusic.profile.settings import SettingsPage
from utils import wait_for_element_value, wait_for_pop_up

class ValidEmailChangeTest(Test):
    VALID_EMAIL = 'lol@kek.ru'

    def test(self):
        page = SettingsPage(self.driver)
        self.email = page.get_email()
        page.change_email(self.VALID_EMAIL)
        wait_for_pop_up(self.driver)
        page.refresh()
        self.assertEqual(
            page.get_email(),
            self.VALID_EMAIL
        )

    def tearDown(self):
        page = SettingsPage(self.driver)
        page.change_email(self.email)
        wait_for_pop_up(self.driver)
        super().tearDown()
