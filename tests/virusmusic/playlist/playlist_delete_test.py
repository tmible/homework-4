from tests.virusmusic.default import Test
from pages.virusmusic.profile.playlists import ProfilePlaylistsPage
from pages.virusmusic.playlist import PlaylistPage
from utils import wait_for_pop_up, wait_for_url
from constants import VIRUSMUSIC_BASE_URL, PLAYLIST_NAME

class PlaylistDeleteTest(Test):
    def setUp(self):
        super().setUp()
        page = ProfilePlaylistsPage(self.driver)
        page.create_playlist(PLAYLIST_NAME)
        wait_for_pop_up(self.driver)
        page.wait_for_playlist(PLAYLIST_NAME)
        self.playlistId = page.get_playlist_id(PLAYLIST_NAME)

    def test(self):
        page = PlaylistPage(self.driver, self.playlistId)
        page.delete()
        wait_for_pop_up(self.driver)
        wait_for_url(self.driver, VIRUSMUSIC_BASE_URL + 'profile/playlists')
