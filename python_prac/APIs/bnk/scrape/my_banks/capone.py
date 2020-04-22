import logging
import ssl
import os, sys, re, StringIO, csv

import requests
import helium 
# or maybe even try scrapy once I get the hang of it
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager
from bankscrape.scraper import unescape_html

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARN)


