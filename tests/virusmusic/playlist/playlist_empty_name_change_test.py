from tests.virusmusic.playlist.default import PlaylistTest
from pages.virusmusic.playlist import PlaylistPage
from utils import wait_for_pop_up

class PlaylistEmptyNameChangeTest(PlaylistTest):
    def test(self):
        page = PlaylistPage(self.driver, self.playlistId)
        page.change_name('')
        wait_for_pop_up(self.driver, success=False)
