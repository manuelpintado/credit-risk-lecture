import logging

import json
import requests

from bs4 import BeautifulSoup


logger = logging.getLogger(__name__)


class SIC(object):
    level = "Standard Industry Classification"
