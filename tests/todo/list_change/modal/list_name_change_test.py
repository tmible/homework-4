from tests.todo.list_change.default import ListChangeTest
from pages.todo.list import ListPage

class ListNameChangeTest(ListChangeTest):
    NEW_LIST_NAME = 'kek'

    def test(self):
        page = ListPage(self.driver)
        page.change_name_modal(self.NEW_LIST_NAME)
        page.wait_for_name(self.NEW_LIST_NAME)
        self.LIST_NAME = self.NEW_LIST_NAME
