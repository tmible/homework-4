import os

from pages.todo.default import Page
from components.todo.auth_form import AuthForm
from utils import wait_for_element_by_selector, wait_for_url
from constants import TODO_AUTH_URL, TODO_MAIN_URL

class AuthPage(Page):
    URL = TODO_AUTH_URL
    NAVBAR_EMAIL = '#PH_user-email'

    def auth(self):
        self.open()
        form = AuthForm(self.driver)
        form.set_login(os.environ['LOGIN'])
        form.next()
        form.set_password(os.environ['PASSWORD'])
        form.submit()
        wait_for_url(self.driver, TODO_MAIN_URL)

    def get_navbar_email(self):
        return wait_for_element_by_selector(self.driver, self.NAVBAR_EMAIL).get_attribute('innerText')
