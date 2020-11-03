from tests.virusmusic.playlist.default import PlaylistTest
from pages.virusmusic.playlist import PlaylistPage
from utils import wait_for_pop_up

class PlaylistNameChangeTest(PlaylistTest):
    NEW_PLAYLIST_NAME = 'kek'

    def test(self):
        page = PlaylistPage(self.driver, self.playlistId)
        page.change_name(self.NEW_PLAYLIST_NAME)
        wait_for_pop_up(self.driver)
        self.assertEqual(
            page.get_name(),
            self.NEW_PLAYLIST_NAME
        )
