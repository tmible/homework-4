import os

from tests.virusmusic.profile.playlists.default import PlaylistTest
from pages.virusmusic.profile.playlists import ProfilePlaylistsPage
from utils import wait_for_pop_up
from constants import PLAYLIST_NAME

class SmallPlaylistImageLoadTest(PlaylistTest):
    SMALL_IMAGE_PATH = os.getcwd() + '/resources/small_avatar.png'

    def test(self):
        page = ProfilePlaylistsPage(self.driver)
        page.load_image(PLAYLIST_NAME, self.SMALL_IMAGE_PATH)
        wait_for_pop_up(self.driver)
