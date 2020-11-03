import os

from tests.virusmusic.playlist.default import PlaylistTest
from pages.virusmusic.playlist import PlaylistPage
from utils import wait_for_pop_up

class SmallPlaylistImageLoadTest(PlaylistTest):
    SMALL_IMAGE_PATH = os.getcwd() + '/resources/small_avatar.png'

    def test(self):
        page = PlaylistPage(self.driver, self.playlistId)
        page.load_image(self.SMALL_IMAGE_PATH)
        wait_for_pop_up(self.driver)
