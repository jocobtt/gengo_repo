# https://erikrood.com/Python_References/web_scrape.html
#https://linuxhint.com/python-beautifulsoup-tutorial-for-beginners/
# https://gist.github.com/ibnesayeed/b4b069b8007f68be91a179a099e35d71
#https://realpython.com/beautiful-soup-web-scraper-python/

import requests
import pandas as pd 
from bs4 import BeautifulSoup
import numpy as np 
import os 

URL = [
"https://suumo.jp/chintai/tokyo/sc_setagaya/"
"https://suumo.jp/chintai/tokyo/"
"https://suumo.jp/chintai/tokyo/sc_shinagawa/"
"https://suumo.jp/chintai/tokyo/sc_shinjuku/"
"https://suumo.jp/chintai/tokyo/sc_meguro/"
"https://suumo.jp/chintai/tokyo/sc_taito/"
"https://suumo.jp/chintai/tokyo/ek_27280/"
"https://suumo.jp/chintai/tokyo/sc_nakano/"
"https://suumo.jp/chintai/tokyo/sc_minato/"
"https://suumo.jp/chintai/tokyo/sc_suginami/"

# other urls?  
]

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

rent = soup.find_all('span', class_='cassetteitem_other-emphasis ui-text--bold')

# info I need from apartment stuff - rent price, distance from places, general location/address, overall square feet, year made, story its at, rei amount, and name of the place, ku_name




# need to get the rest of these and then have it loop through all of the pages!!

rent_price = []
address = []
sqr_m = []
name_place = []
rei_price = []
distance = []
apartment_type = []
maintenence_price = []
house_type = [] # cont.span
year_built = []
floor = []
ku_name = []

for rent in rent_elems:
	rent_price = rent.find('span', class_='cassetteitem_other-emphasis ui-text--bold')
	address = rent.find('li', class_='cassettitem_detail-col1')
	sqr_m = rent.find('span', class_='cassettitem_menseki')
	name_place = rent.find('div', class_='cassetteitem_content_title')
	rei_price = rent.find('div', class_='cassetteitem_price cassetteitem_price--gratuity')
	distance = rent.find('li', class_='cassetteitem_detail-col2')
	aparment_type = rent.find('span', class_='cassetteitem_madori')
	print(rent_price.text)



for container in apartment_container:
	if container.find('div', class_ = "cassetteitem")

	# the address 
	addr = container.div.ul.li.text
	address.append(addr)

	# rent price 
	renty = container.tbody.ul.span.text
	rent_price.append(renty)

	# sqr_m 
	sqr = container.find('span', class_="cassetteitem_menseki").text # will have to clean this later
	sqr_m.appen(sqr)

	# name place 
	name = container.div.li.text
	name_place.append(name)

	# rei_price 
	rei = container.find('span', class_="cassetteitem_price cassetteitem_price--gratuity").text # will have to clean this later
	rei_price.append(rei)

	# distance?

	# apartment_type
	aprt = container.find("span", class_="cassetteitem_madori").text # will have to clean this later
	apartment_type.append(apart)

	# administration - span "cassetteitem_price cassetteitem_price--administration"


df_ = pr.DataFrame({'rent_price': rent_price, 
	'address' : address,
	'sqr_m' : sqr_m,
	'name_place' : name_place,
	'rei_price' : rei_price,
	'distance' : distance,
	'apartment_type' : apartment_type,
	'ku_name' : ku_name})

os.chdir('~/Downloads/')

df_.to_csv('apartment.csv')



