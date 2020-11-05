from tests.todo.list_change.default import ListChangeTest
from pages.todo.list import ListPage
from constants import LIST_LONG_DESCRIPTION, LIST_DESCRIPTION_PLACEHOLDER

class ListLongDescriptionChangeTest(ListChangeTest):
    def test(self):
        page = ListPage(self.driver)
        page.change_description_modal(LIST_LONG_DESCRIPTION)
        page.refresh()
        page.wait_for_description(LIST_DESCRIPTION_PLACEHOLDER)
