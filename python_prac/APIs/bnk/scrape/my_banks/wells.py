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


class TLSv1Adapter(HTTPAdapter):
    """Force TLSv1
    Wells Fargo hangs with requests' default SSL setup so hard-set
    TLSv1 here.
    http://lukasa.co.uk/2013/01/Choosing_SSL_Version_In_Requests/
    """

    def init_poolmanager(self, connections, maxsize, **kwargs):
        self.poolmanager = PoolManager(num_pools=connections,
                                       maxsize=maxsize,
                                       ssl_version=ssl.PROTOCOL_TLSv1)


SCRAPER = requests.Session()
SCRAPER.mount('https://', TLSv1Adapter())

def login(user, pswrd):
    SCRAPER.get('https://www.wellsfargo.com/')
    login_data = {
        'user': username,
        'pswrd': password,
        'screenid': 'SIGNON',
        'origination': 'WebCons',
        'LOB': 'Cons',
    }
    SCRAPER.post('https://online.wellsfargo.com/signon', login_data)
    response = SCRAPER.get('https://online.wellsfargo.com/das/cgi-bin/session.cgi?screenid=SIGNON_PORTAL_PAUSE')
    return response.text