from tests.todo.default import Test
from pages.todo.main import MainPage
from constants import LIST_LONG_NAME

class ListLongNameCreationTest(Test):
    def test(self):
        page = MainPage(self.driver)
        page.create_list(LIST_LONG_NAME)
        page.wait_for_list_to_disappear(LIST_LONG_NAME)
