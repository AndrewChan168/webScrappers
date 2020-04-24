from selenium import webdriver



class BasicBrowser:
    def start(self):
        self.browser = webdriver.Chrome(executable_path=r"public/chromedriver.exe")
        # set driver an implicit wait for 1 second to poll DOM
        #self.browser.implicitly_wait(1)


    def terminate(self):
        self.browser.close()

    def __init__(self):
        self.start()



class MainPageBrowser(BasicBrowser):
    def __init__(self):
        super().__init__()
        self.main_page_uri = ''

    def set_main_page(self, main_page_uri):
        self.main_page_uri = main_page_uri
        return self

    def goto_main_page(self):
        assert self.main_page_uri != '', "Main Page URI could not be empty string"
        self.browser.get(self.main_page_uri)
        return self



class LoginPageBrowser(BasicBrowser):
    def __init__(self):
        super().__init__()
        self.login_page_uri = ''

    def set_login_page(self, login_page_uri):
        self.login_page_uri = login_page_uri
        return self

    def goto_login_page(self):
        assert self.login_page_uri != '', "Login Page URI could not be empty string"
        self.browser.get(self.login_page_uri)
        return self



class SubPageBrower(MainPageBrowser):
    def __init__(self):
        super().__init__()
        self.sub_page_uri = ''

    def set_sub_page(self, sub_page_uri):
        self.sub_page_uri = sub_page_uri
        return self

    def goto_sub_page(self):
        assert self.sub_page_uri != '', "Sub Page URI could not be empty string"
        self.browser.get(self.sub_page_uri)
        return self
