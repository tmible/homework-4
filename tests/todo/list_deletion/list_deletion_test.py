from tests.todo.default import Test
from pages.todo.main import MainPage
from pages.todo.list import ListPage
from utils import wait_for_url
from constants import TODO_MAIN_URL

class ListDeletionTest(Test):
    LIST_NAME = 'lol'

    def setUp(self):
        super().setUp()
        page = MainPage(self.driver)
        page.create_list(self.LIST_NAME)
        page.wait_for_list(self.LIST_NAME)
        self.lists = page.count_lists()
        page.open_list(self.LIST_NAME)

    def test(self):
        page = ListPage(self.driver)
        page.delete()
        wait_for_url(self.driver, TODO_MAIN_URL)
        page = MainPage(self.driver)
        self.assertEqual(
            self.lists - 1,
            page.count_lists()
        )
