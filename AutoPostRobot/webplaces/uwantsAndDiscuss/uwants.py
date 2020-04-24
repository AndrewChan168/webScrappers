from .uwantsAndDiscuss import UwantsAndDiscuss

# set sub page when calling the uwants browser in Flask web server
uwants_browser = UwantsAndDiscuss()\
    .set_login_page('https://www.uwants.com/logging.php?action=login')\
    .set_main_page('https://www.uwants.com')