from bs4 import BeautifulSoup 
import pandas as pd 
import numpy as np 
import os 
import requests 
from time import sleep 
from datetime import datetime 
import googlemaps 

# may need to just do this all in selenium though... 
# use apartments.com api to pull down comments - https://api.apartments.com/v1

url = "https://www.apartments.com/"

arl_url = "https://www.apartments.com/arlington-va/"

####################
#    start loop    #
####################

print("starting loop")

rent_low = []
rent_high = []
special_offer = [] # yes or no 
apt_type = []
avail_date = []
sqr_ft = []


