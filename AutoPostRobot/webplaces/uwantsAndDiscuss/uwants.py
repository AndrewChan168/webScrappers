from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoSuchAttributeException

from .uwantsAndDiscuss import UwantsAndDiscuss

TIMEOUT = 10

class Uwants(UwantsAndDiscuss):
    def goto_main_page(self):
        ### Uwants always popup cookies agreement bar, so we have to click agree
        ### it may be different from discuss
        print('Uwants.goto_main_page()')
        super().goto_main_page()
        # Uwants structure has been changed
        #try:
        #    element_present = EC.presence_of_element_located((By.ID, 'cc-container'))
        #    WebDriverWait(self.browser, TIMEOUT).until(element_present)
        #except TimeoutException:
        #    print("Error: Uwants: Uwants Cookies Bar hasn't appeared")
        #    return self
        #else:
        #    cookie_bar_elements = self.browser.find_element_by_id('cc-container').find_elements_by_css_selector("*")
        #if len(cookie_bar_elements) >= 6:
        #    cookie_bar_elements[6].click()
        return self

    def post_comment(self, post_id:str, comment_content:str):
        ### go to the sub page
        print('Uwants.post_comment()')
        self.goto_sub_page()
        try:
            element_present = EC.presence_of_element_located((By.ID, 'home-top-bar-container'))
            WebDriverWait(self.browser, TIMEOUT).until(element_present)
        except TimeoutException:
            print("Error: Uwants: Timed out waiting for sub-page to load")
            ### stop here and return self
            return self

        try:
            link = self.browser.find_element_by_id(post_id).find_element_by_tag_name('a').get_attribute('href')
            if link is None:
                raise NoSuchAttributeException
        except NoSuchElementException:
            print("Error: Uwants: Post with such post-ID was not found")
            ### stop here and return self
            return self
        except NoSuchAttributeException:
            print("Error: Uwants: href attribute was not found in the tag")
            ### stop here and return self
            return self
        else:
            self.browser.get(link.split('&')[0])
            print('Uwants: Complete getting Post-ID')

        try:
            self.browser.execute_script('window.scrollTo(0,document.body.scrollHeight/10)')
            element_present = EC.presence_of_element_located((By.CLASS_NAME, 'postbtn'))
            WebDriverWait(self.browser, TIMEOUT).until(element_present)
        except TimeoutException:
            print("Error: Uwants: Timed out waiting for post page to load")
        else:
            self.browser.find_element_by_class_name('postbtn').find_elements_by_tag_name('a')[2].click()
            print('Uwants: Complete finding reply button')

        ### uwants will pop-up tips window
        ### deal with it before posting reply
        try:
            element_present = EC.presence_of_element_located((By.CLASS_NAME, 'tips_close'))
            WebDriverWait(self.browser, TIMEOUT).until(element_present)
        except TimeoutException:
            print("Error: Uwants: Timed out waiting for post page to load")
        else:
            self.browser.find_element_by_class_name('tips_close').click()
            print('Uwants: tips close completed')

        try:
            element_present = EC.presence_of_element_located((By.ID, 'posteditor_iframe'))
            WebDriverWait(self.browser, TIMEOUT).until(element_present)
        except TimeoutException:
            print("Error: Uwants: Timed out waiting for reply page to load")
        else:
            self.browser.switch_to.frame(self.browser.find_element_by_id('posteditor_iframe'))
            self.browser.find_element_by_tag_name('body').send_keys(comment_content)
            self.browser.switch_to.default_content()
            print('Uwants: Complete filling reply comment')

        try:
            self.browser.execute_script('window.scrollTo(0,document.body.scrollHeight/3)')
            element_present = EC.presence_of_element_located((By.NAME, 'replysubmit'))
            WebDriverWait(self.browser, TIMEOUT).until(element_present)
        except TimeoutException:
            print('Error: Uwants: Timed out waiting for reply button to load')
        else:
            self.browser.find_element_by_name('replysubmit').click()
            print('Uwants: Complete clicking submit button')
        return self



uwants_browser = Uwants()\
    .set_login_page('https://www.uwants.com/logging.php?action=login')\
    .set_main_page('https://www.uwants.com')\
    .set_sub_page('https://digital.uwants.com/forumdisplay.php?fid=681')\
    .goto_main_page()