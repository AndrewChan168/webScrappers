from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoSuchAttributeException

from ..basic_virtual_browser import *

TIMEOUT = 10


class UwantsAndDiscuss(LoginPageBrowser, SubPageBrower):
    def __init__(self):
        super().__init__()

    def login(self, username:str, password:str):
        print('UwantsAndDiscuss.login()')
        ### go to login page
        self.goto_login_page()
        try:
            ### wait for login page is ready
            element_present = EC.presence_of_element_located((By.NAME, 'username'))
            WebDriverWait(self.browser, TIMEOUT).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")
        else:
            # input username & password
            self.browser.find_element_by_name('username').send_keys(username)
            self.browser.find_element_by_name('password').send_keys(password)
            # click on login button
            self.browser.find_element_by_name('loginsubmit').click()
            super().login()
        finally:
            # go to main page no matter login succeed or not
            self.goto_main_page()
        return self

    def post_comment(self, post_id:str, comment_content:str):
        print('UwantsAndDiscuss.post_comment()')
        ### let child class to implement as there are some differences between discuss and uwants
        return self

    def post_comments_by_batch(self, post_ids:list, comment_contents:list):
        print('UwantsAndDiscuss.post_comments_by_batch()')
        assert len(post_ids)==len(comment_contents), "Number of post-IDs is not equal to contents"
        for post_id, comment_content in zip(post_ids, comment_contents):
            _ = self.post_comment(post_id, comment_content)
        return self