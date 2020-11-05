from tests.virusmusic.default import Test
from pages.virusmusic.profile.playlists import ProfilePlaylistsPage
from utils import wait_for_pop_up

class PlaylistWithEmptyNameCreationTest(Test):
    def test(self):
        page = ProfilePlaylistsPage(self.driver)
        page.create_playlist('')
        wait_for_pop_up(self.driver, success=False)
