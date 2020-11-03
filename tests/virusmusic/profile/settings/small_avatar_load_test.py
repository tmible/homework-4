import os

from tests.default import Test
from pages.virusmusic.profile.settings import SettingsPage
from utils import wait_for_pop_up

class SmallAvatarLoadTest(Test):
    SMALL_AVATAR_PATH = os.getcwd() + '/resources/small_avatar.png'

    def test(self):
        page = SettingsPage(self.driver)
        page.load_avatar(self.SMALL_AVATAR_PATH)
        wait_for_pop_up(self.driver)
