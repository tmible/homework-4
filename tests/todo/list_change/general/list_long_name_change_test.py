from tests.todo.list_change.default import ListChangeTest
from pages.todo.list import ListPage
from constants import LIST_LONG_NAME

class ListLongNameChangeTest(ListChangeTest):
    def test(self):
        page = ListPage(self.driver)
        page.change_name(LIST_LONG_NAME)
        page.refresh()
        page.wait_for_name(self.LIST_NAME)
