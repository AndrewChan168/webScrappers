from ..basic_virtual_browser import *

class UwantsAndDiscuss(LoginPageBrowser, SubPageBrower):
    def __init__(self):
        super().__init__()

    def login(self, login_uri, username:str, password:str):
        # go to login page
        self.goto_login_page()
        # input username & password
        self.browser.find_element_by_name('username').send_keys(username)
        self.browser.find_element_by_name('password').send_keys(password)
        # click on login button
        self.browser.find_element_by_name('loginsubmit').click()
        # go to main page when login is completed
        self.goto_main_page()
        return self

    def _post_comment(self, post_id:str, comment_content:str):
        # go to the sub page
        self.goto_sub_page()
        # get the link of the post that user want to post comment
        link = self.browser.find_element_by_id(post_id).find_element_by_tag_name('a').get_attribute('href')
        # go to post
        self.browser.get(link.split('&')[0])
        # click on `reply` button
        self.browser.find_element_by_class_name('postbtn').find_elements_by_tag_name('a')[2].click()
        # as the reply content field is textarea which is in iframe
        # then we have to switch browser to iframe
        self.browser.switch_to.frame(self.browser.find_element_by_id('posteditor_iframe'))
        # send user's comment to the textarea of replying
        self.browser.find_element_by_tag_name('body').send_keys(comment_content)
        # switch back to brower mode
        self.browser.switch_to.default_content()
        # click on submit button
        self.browser.find_element_by_name('replysubmit').click()

    def post_comment(self, post_id:str, comment_content:str):
        self._post_comment(post_id, comment_content)
        return self

    def post_comments_by_batch(self, post_ids:list, comment_contents:list):
        assert len(post_ids)==len(comment_contents), "Number of post-IDs is not equal to contents"
        for post_id, comment_content in zip(post_ids, comment_contents):
            self._post_comment(post_id, comment_content)
        return self