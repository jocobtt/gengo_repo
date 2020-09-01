import pandas as pd 
import numpy as np 
import requests 
import os
from bs4 import BeautifulSoup

URL = "https://www.asahi.com/"


page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')



art_text = []
author = []
title = []
subject = []
date_written = []


# figure out what websites to grab from - either asahi or https://www.sankei.com/

# will have to loop from mainpage on each article and pull the text 
# will have to be set with a cronjob 
# then feed it to a runtime for analysis etc. 
