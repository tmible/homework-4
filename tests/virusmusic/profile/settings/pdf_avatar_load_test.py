import os

from tests.default import Test
from pages.virusmusic.profile.settings import SettingsPage
from constants import AVATAR_ERROR_ID, AVATAR_ERROR_EXTENSION_MESSAGE

class PdfAvatarLoadTest(Test):
    PDF_AVATAR_PATH = os.getcwd() + '/resources/RK-3.pdf'

    def test(self):
        page = SettingsPage(self.driver)
        page.load_avatar(self.PDF_AVATAR_PATH)
        self.assertEqual(
            self.driver.find_element_by_id(AVATAR_ERROR_ID).get_attribute('innerText'),
            AVATAR_ERROR_EXTENSION_MESSAGE
        )
