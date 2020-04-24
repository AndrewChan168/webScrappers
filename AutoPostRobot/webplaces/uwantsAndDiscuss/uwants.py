from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoSuchAttributeException

from .uwantsAndDiscuss import UwantsAndDiscuss

TIMEOUT = 3

class Uwants(UwantsAndDiscuss):
    def goto_main_page(self):
        ### Uwants always popup cookies agreement bar, so we have to click agree
        ### it may be different from discuss
        super().goto_main_page()
        try:
            element_present = EC.presence_of_element_located((By.ID, 'cc-container'))
            WebDriverWait(self.browser, TIMEOUT).until(element_present)
        except TimeoutException:
            print("Uwants Cookies Bar hasn't appeared")
            return self
        else:
            cookie_bar_elements = self.browser.find_element_by_id('cc-container').find_elements_by_css_selector("*")
        if len(cookie_bar_elements) >= 6:
            cookie_bar_elements[6].click()
        return self

    def post_comment(self, post_id:str, comment_content:str):
        ### go to the sub page
        self.goto_sub_page()
        try:
            element_present = EC.presence_of_element_located((By.ID, 'home-top-bar-container'))
            WebDriverWait(self.browser, TIMEOUT).until(element_present)
        except TimeoutException:
            print("Timed out waiting for sub-page to load")
            ### stop here and return self
            return self

        try:
            link = self.browser.find_element_by_id(post_id).find_element_by_tag_name('a').get_attribute('href')
            if link is None:
                raise NoSuchAttributeException
        except NoSuchElementException:
            print("Post with such post-ID was not found")
            ### stop here and return self
            return self
        except NoSuchAttributeException:
            print("href attribute was not found in the tag")
            ### stop here and return self
            return self
        else:
            self.browser.get(link.split('&')[0])

        try:
            element_present = EC.presence_of_element_located((By.CLASS_NAME, 'postbtn'))
            WebDriverWait(self.browser, TIMEOUT).until(element_present)
        except TimeoutException:
            print("Timed out waiting for post page to load")
        else:
            self.browser.find_element_by_class_name('postbtn').find_elements_by_tag_name('a')[2].click()

        ### uwants will pop-up tips window
        ### deal with it before posting reply
        try:
            element_present = EC.presence_of_element_located((By.CLASS_NAME, 'tips_close'))
            WebDriverWait(self.browser, TIMEOUT).until(element_present)
        except TimeoutException:
            print("Timed out waiting for post page to load")
        else:
            self.browser.find_element_by_class_name('tips_close').click()

        try:
            element_present = EC.presence_of_element_located((By.ID, 'posteditor_iframe'))
            WebDriverWait(self.browser, TIMEOUT).until(element_present)
        except TimeoutException:
            print("Timed out waiting for reply page to load")
        else:
            self.browser.switch_to.frame(self.browser.find_element_by_id('posteditor_iframe'))
            self.browser.find_element_by_tag_name('body').send_keys(comment_content)
            self.browser.switch_to.default_content()

        try:
            element_present = EC.presence_of_element_located((By.NAME, 'replysubmit'))
            WebDriverWait(self.browser, TIMEOUT).until(element_present)
        except TimeoutException:
            print('Timed out waiting for reply button to load')
        else:
            self.browser.find_element_by_name('replysubmit').click()
        return self



uwants_browser = Uwants()\
    .set_login_page('https://www.uwants.com/logging.php?action=login')\
    .set_main_page('https://www.uwants.com')\
    .goto_main_page()