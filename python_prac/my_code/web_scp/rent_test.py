import pandas as pd 
import numpy as np
import requests
import os
from bs4 import BeautifulSoup
from time import sleep

# set url to search from and get it 
URL = "https://suumo.jp/jj/chintai/ichiran/FR301FC001/?ar=030&bs=040&pc=50&smk=&po1=25&po2=99&shkr1=03&shkr2=03&shkr3=03&shkr4=03&sc=13101&sc=13102&sc=13103&sc=13104&sc=13105&sc=13113&sc=13106&sc=13107&sc=13108&sc=13118&sc=13109&sc=13110&sc=13111&sc=13112&sc=13114&sc=13115&sc=13116&ta=13&cb=0.0&ct=9999999&md=02&md=03&md=04&md=05&md=06&et=9999999&mb=0&mt=9999999&cn=9999999&tc=0400301&fw2="

page = requests.get(URL)


###########################
# loop through pages test #   
###########################
rent_price = []
address = []
sqr_m = []
name_place = []
rei_price = []
eki = []
apartment_type = []
maintenence_price = []
house_type = [] # cont.span
year_built = []
ku_name = []

pages = np.arange(1,10,1) # this will 1-10 by 10
page = requests.get(URL + str(page) + "&ref_=adv_nxt")
soup = BeautifulSoup(page.text, 'html.parser')

apartment_container = soup.find_all('div', class_ = "cassetteitem")

for container in apartment_container:

	

	sleep(randint(2,4))

	renty = container.tbody.ul.span.text
	rent_price.append(renty)

	sleep(randint(2,10))

	addr = container.div.ul.li.text
	address.append(addr)






############################
