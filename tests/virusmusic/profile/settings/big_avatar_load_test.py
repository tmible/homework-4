import os

from tests.virusmusic.default import Test
from pages.virusmusic.profile.settings import SettingsPage
from constants import AVATAR_ERROR_ID, AVATAR_ERROR_SIZE_MESSAGE

class BigAvatarLoadTest(Test):
    BIG_AVATAR_PATH = os.getcwd() + '/resources/iiL9jsEie_w.jpg'

    def test(self):
        page = SettingsPage(self.driver)
        page.load_avatar(self.BIG_AVATAR_PATH)
        self.assertEqual(
            self.driver.find_element_by_id(AVATAR_ERROR_ID).get_attribute('innerText'),
            AVATAR_ERROR_SIZE_MESSAGE
        )
