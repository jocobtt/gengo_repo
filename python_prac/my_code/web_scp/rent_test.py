import pandas as pd 
import numpy as np
import requests
import os
from bs4 import BeautifulSoup
from time import sleep

# set url to search from and get it 
URL = "https://suumo.jp/jj/chintai/ichiran/FR301FC001/?ar=030&bs=040&pc=50&smk=&po1=25&po2=99&shkr1=03&shkr2=03&shkr3=03&shkr4=03&sc=13101&sc=13102&sc=13103&sc=13104&sc=13105&sc=13113&sc=13106&sc=13107&sc=13108&sc=13118&sc=13109&sc=13110&sc=13111&sc=13112&sc=13114&sc=13115&sc=13116&ta=13&cb=0.0&ct=9999999&md=02&md=03&md=04&md=05&md=06&et=9999999&mb=0&mt=9999999&cn=9999999&tc=0400301&fw2="



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

s = requests.session()
headers = {
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
}
s.headers.update(headers)

pages = np.arange(1,3,1)
for page in pages:
	page = requests.get(URL + str(pages) + "&ref_=adv_nxt", headers=headers)
	soup = BeautifulSoup(page.text, 'html.parser')
	apartment_container = soup.find_all('div', class_ = "cassetteitem")
	sleep(np.random.randint(10,30)) # 2-30 seconds between each page
	for container in apartment_container:
		sleep(np.random.randint(2,3)) # wait 2-5 seconds between each apartment container for testing 
		renty = container.tbody.ul.span.text
		rent_price.append(renty)
		sleep(np.random.randint(2,3))
		addy = container.div.ul.li.text
		address.append(addy)


rent_price 
address


# this will run in my container will need to create pvc for it to be mounted locally later on 
df_ = pd.DataFrame({'rent_price': rent_price, 
	'address' : address})

# it doesn't matter where it's saved for our purposes currently...

df_.to_csv('apartment.csv')






############################
