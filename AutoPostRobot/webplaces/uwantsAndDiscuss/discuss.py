from .uwantsAndDiscuss import UwantsAndDiscuss

# set sub page when calling the uwants browser in Flask web server
discuss_browser = UwantsAndDiscuss()\
    .set_login_page('https://www.discuss.com.hk/logging.php?action=login')\
    .set_main_page('https://www.discuss.com.hk')