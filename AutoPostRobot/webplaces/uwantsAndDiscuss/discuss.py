from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoSuchAttributeException

from .uwantsAndDiscuss import UwantsAndDiscuss

TIMEOUT = 10

class Discuss(UwantsAndDiscuss):
    def post_comment(self, post_id:str, comment_content:str):
        print('Discuss.post_comment()')
        ### go to the sub page
        self.goto_sub_page()
        try:
            ### wait for sub page is ready
            ### for hkdiscuss
            element_present = EC.presence_of_element_located((By.CLASS_NAME, 'header-inner'))
            WebDriverWait(self.browser, TIMEOUT).until(element_present)
        except TimeoutException:
            print("Discuss: Timed out waiting for sub-page to load")
            ### stop here and return self
            return self

        try:
            ### get the link of the post that user want to post comment
            link = self.browser.find_element_by_id(post_id).find_element_by_tag_name('a').get_attribute('href')
            if link is None:
                raise NoSuchAttributeException
        except NoSuchElementException:
            print("Error: Discuss: Post with such post-ID was not found")
            ### stop here and return self
            return self
        except NoSuchAttributeException:
            print("Error: Discuss: href attribute was not found in the tag")
            ### stop here and return self
            return self
        else:
            ### go to the post that use want to reply
            self.browser.get(link.split('&')[0])
            print('Discuss: Complete getting Post-ID')

        try:
            element_present = EC.presence_of_element_located((By.CLASS_NAME, 'start_btn_small_reply'))
            WebDriverWait(self.browser, TIMEOUT).until(element_present)
        except TimeoutException:
            print("Error: Discuss: Timed out waiting for post page to load")
            ### stop here and return self
            return self
        else:
            ### click on reply button and go to reply page
            self.browser.find_element_by_class_name('start_btn_small_reply').click()
            print('Discuss: Complete finding reply button')

        try:
            element_present = EC.presence_of_element_located((By.ID, 'posteditor_iframe'))
            WebDriverWait(self.browser, TIMEOUT).until(element_present)
        except TimeoutException:
            print("Error: Discuss: Timed out waiting for reply page to load")
            ### stop here and return self
            return self
        else:
            self.browser.switch_to.frame(self.browser.find_element_by_id('posteditor_iframe'))
            self.browser.find_element_by_tag_name('body').send_keys(comment_content)
            self.browser.switch_to.default_content()
            print('Discuss: Complete filling reply comment')

        try:
            self.browser.execute_script('window.scrollTo(0,document.body.scrollHeight/5)')
            element_present = EC.presence_of_element_located((By.NAME, 'replysubmit'))
            WebDriverWait(self.browser, TIMEOUT).until(element_present)
        except TimeoutException:
            print('Error: Discuss: Timed out waiting for reply button to load')
            ### stop here and return self
            return self
        else:
            self.browser.find_element_by_name('replysubmit').click()
            print('Discuss: Complete clicking submit button')

        return self



# set sub page when calling the uwants browser in Flask web server
discuss_browser = Discuss()\
    .set_login_page('https://www.discuss.com.hk/logging.php?action=login')\
    .set_main_page('https://www.discuss.com.hk')\
    .set_sub_page('https://computer.discuss.com.hk/forumdisplay.php?fid=115')\
    .goto_main_page()