import logging
import ssl
import os, sys, re, StringIO, csv

import requests 
import helium
# or maybe try and do this in scrapy
import requests 
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager
from bankscrap.scraper import unescape_html

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARN)
