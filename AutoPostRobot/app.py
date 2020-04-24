from flask import Flask

from webplaces.uwantsAndDiscuss.uwants import uwants_browser
from webplaces.uwantsAndDiscuss.discuss import discuss_browser

# terminate browsers when the flask server is terminated
import atexit
def exit_hadler():
    uwants_browser.terminate()
    discuss_browser.terminate()

atexit.register(exit_hadler)

app = Flask(__name__)

app.listen(300)