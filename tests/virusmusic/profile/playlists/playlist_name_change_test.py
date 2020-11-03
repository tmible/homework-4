from tests.virusmusic.profile.playlists.default import PlaylistTest
from pages.virusmusic.profile.playlists import ProfilePlaylistsPage
from utils import wait_for_pop_up
from constants import PLAYLIST_NAME

class PlaylistNameChangeTest(PlaylistTest):
    NEW_PLAYLIST_NAME = 'kek'

    def test(self):
        page = ProfilePlaylistsPage(self.driver)
        page.change_name(PLAYLIST_NAME, self.NEW_PLAYLIST_NAME)
        wait_for_pop_up(self.driver)
