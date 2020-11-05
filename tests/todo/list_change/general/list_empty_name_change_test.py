from tests.todo.list_change.default import ListChangeTest
from pages.todo.list import ListPage
from constants import LIST_NAME_PLACEHOLDER

class ListEmptyNameChangeTest(ListChangeTest):
    NEW_LIST_NAME = ''

    def test(self):
        page = ListPage(self.driver)
        page.change_name(self.NEW_LIST_NAME)
        page.wait_for_name(LIST_NAME_PLACEHOLDER)
        self.LIST_NAME = self.NEW_LIST_NAME
