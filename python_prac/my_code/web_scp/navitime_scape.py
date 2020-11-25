import requests
import re
import pandas as pd 
from bs4 import BeautifulSoup
import numpy as np 
import os 
from time import sleep

navi = "https://www.navitime.co.jp/"
POI_RE = re.compile(r"setPOI\(([^)]+)\);")

ex_addr = "東京都中野区中野２"

work_addr = "東京都港区六本木６"

# want to pull long, lat, time to location, number of stops

# input search for location 

from navitime import api


def test_address_search():
    results = api.address_search("六本木グランドタワー")
    assert results
