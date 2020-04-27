from selenium import webdriver
from selenium.common.exceptions import InvalidSessionIdException, WebDriverException


class BasicBrowser:
    def start(self):
        print('BasicBrowser.start()')
        self.browser = webdriver.Chrome(executable_path=r"public/chromedriver.exe")
        self.browser.maximize_window()
        # set driver an implicit wait for 1 second to poll DOM
        #self.browser.implicitly_wait(1)

    def terminate(self):
        print('BasicBrowser.terminate()')
        self.browser.close()

    def isOpen(self):
        print('BasicBrowser.isOpen()')
        not_open_msg = r'Unable to evaluate script: disconnected: not connected to DevTools\n'
        try:
            browser_log = self.browser.get_log('driver')
            if len(browser_log) == 0:
                return True
            elif browser_log[-1]['message'] == not_open_msg:
                return False
            else:
                return True
        except InvalidSessionIdException:
            return False
        except WebDriverException:
            return False

    def __init__(self):
        self.start()



class MainPageBrowser(BasicBrowser):
    def __init__(self):
        super().__init__()
        self.main_page_uri = ''

    def set_main_page(self, main_page_uri):
        print('MainPageBrowser.set_main_page()')
        self.main_page_uri = main_page_uri
        return self

    def goto_main_page(self):
        print('MainPageBrowser.goto_main_page()')
        assert self.main_page_uri != '', "Main Page URI could not be empty string"
        self.browser.get(self.main_page_uri)
        return self



class LoginPageBrowser(BasicBrowser):
    def __init__(self):
        super().__init__()
        self.login_page_uri = ''
        self.isLogin = False

    def set_login_page(self, login_page_uri):
        print('MainPageBrowser.set_login_page()')
        self.login_page_uri = login_page_uri
        return self

    def goto_login_page(self):
        print('MainPageBrowser.goto_login_page()')
        assert self.login_page_uri != '', "Login Page URI could not be empty string"
        self.browser.get(self.login_page_uri)
        return self

    def logout(self):
        print('MainPageBrowser.logout()')
        self.browser.delete_all_cookies()
        self.isLogin = False
        self.goto_login_page()
        return self

    def login(self):
        print('MainPageBrowser.login()')
        self.isLogin = True



class SubPageBrower(MainPageBrowser):
    def __init__(self):
        super().__init__()
        self.sub_page_uri = ''

    def set_sub_page(self, sub_page_uri):
        print('SubPageBrower.set_sub_page()')
        self.sub_page_uri = sub_page_uri
        return self

    def goto_sub_page(self):
        print('SubPageBrower.goto_sub_page()')
        assert self.sub_page_uri != '', "Sub Page URI could not be empty string"
        self.browser.get(self.sub_page_uri)
        return self
