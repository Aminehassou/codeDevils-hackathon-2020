import os
# Use the package we installed
import logging
from slack_bolt import App, BoltContext
from slack_sdk import WebClient
from dotenv import load_dotenv
from api import get_country_info
logging.basicConfig(level=logging.DEBUG)
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)
