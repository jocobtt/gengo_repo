# https://erikrood.com/Python_References/web_scrape.html
#https://linuxhint.com/python-beautifulsoup-tutorial-for-beginners/
# https://gist.github.com/ibnesayeed/b4b069b8007f68be91a179a099e35d71
#https://realpython.com/beautiful-soup-web-scraper-python/

import requests
import pandas as pd 
from bs4 import BeautifulSoup
import numpy as np 
import os 
from time import sleep

# this has all of the prefectures 
URL = "https://suumo.jp/jj/chintai/ichiran/FR301FC001/?ar=030&bs=040&pc=50&smk=&po1=25&po2=99&shkr1=03&shkr2=03&shkr3=03&shkr4=03&sc=13101&sc=13102&sc=13103&sc=13104&sc=13105&sc=13113&sc=13106&sc=13107&sc=13108&sc=13118&sc=13109&sc=13110&sc=13111&sc=13112&sc=13114&sc=13115&sc=13116&ta=13&cb=0.0&ct=9999999&md=02&md=03&md=04&md=05&md=06&et=9999999&mb=0&mt=9999999&cn=9999999&tc=0400301&fw2="

UL = [
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

cont = soup.find('div', class_="cassetteitem")

# info I need from apartment stuff - rent price, distance from places, general location/address, overall square feet, year made, story its at, rei amount, and name of the place, ku_name




# need to get the rest of these and then have it loop through all of the pages!!

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
floor = []
ku_name = []

''' for reference to find the objects I want 
for rent in rent_elems:
	rent_price = rent.find('span', class_='cassetteitem_other-emphasis ui-text--bold')
	address = rent.find('li', class_='cassettitem_detail-col1')
	sqr_m = rent.find('span', class_='cassettitem_menseki')
	name_place = rent.find('div', class_='cassetteitem_content_title')
	rei_price = rent.find('div', class_='cassetteitem_price cassetteitem_price--gratuity')
	eki = rent.find('li', class_='cassetteitem_detail-col2')
	aparment_type = rent.find('span', class_='cassetteitem_madori')
	print(rent_price.text)
'''

apartment_container = soup.find_all('div', class_ = "cassetteitem")

for container in apartment_container:

	sleep(np.random.randint(1,10))

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

	# nearest eki
	eki_ = container.find('div', class_='cassetteitem_detail-text')
	eki.apend(eki_)

	# house type
	house = container.find('span',class_='ui-pct ui-pct--util1').text 
	house_type.append(house)

	# floor - xpath == #//*[@id="js-bukkenList"]/ul[1]/li[1]/div/div[2]/table/tbody[1]/tr/td[3]
	#floo = container.
	#floor.append(floo)


	# ku name 
	ku = soup.find('div', class_='designateline-box-txt02').text  # will need to scrape some of this off 
	ku_name.append(ku)

	# year built 
	year = container.
	year_built.append(year)


	# apartment_type
	aprt = container.find("span", class_="cassetteitem_madori").text # will have to clean this later
	apartment_type.append(apart)

	# administration - span "cassetteitem_price cassetteitem_price--administration"
	admin = container.find('span', class_="cassetteitem_price cassetteitem_price--administration")
	maintenence_price.append(admin)


df_ = pr.DataFrame({'rent_price': rent_price, 
	'address' : address,
	'sqr_m' : sqr_m,
	'name_place' : name_place,
	'rei_price' : rei_price,
	'maintenence_price' : maintenence_price,
	'nearest_eki' : eki,
	'apartment_type' : apartment_type,
	'year_built' : year_built,
	'ku_name' : ku_name,
	'place_name' : place_name,
	'house_type': house_type})

os.chdir('~/Downloads/')

df_.to_csv('apartment.csv')

########################################
# Scrape multiple pages instead of one #
########################################

#import itertools 
#for index in itertools.count(start=1):
#	url = "https://suumo.jp/chintai/tokyo/sc_suginami/"+str(index)
#pages = np.arange(1,1001, 50) # 1001 == last page+ so may need to adjust that. 





###########################
# loop through pages test #
###########################
headers = {"Accept-Language": "jp-JP,jp;q=0.5"} # test if this is what we need??
pages = np.arange(1,10,50)
for page in pages:
	page = requests.get(URL + str(page) + "&ref_=adv_nxt", headers=headers)

	soup = BeautifulSoup(page.text, 'html.parser')

	apartment_container = soup.find_all('div', class_ = "cassetteitem")

	sleep(randint(2,10))

############################



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

pages = np.arange(1,1001,50)

page = requests.get(URL)

apartment_container = soup.find_all('div', class_ = "cassetteitem")
sleep(np.random.randint(3,10))

for container in apartment_container:
	if container.find('div', class_ = "cassetteitem")

	sleep(np.random.randint(1,10))

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

	# nearest eki
	eki_ = container.find('div', class_='cassetteitem_detail-text')
	eki.apend(eki_)

	# house type
	house = container.find('span',class_='ui-pct ui-pct--util1').text 
	house_type.append(house)

	# floor - xpath == #//*[@id="js-bukkenList"]/ul[1]/li[1]/div/div[2]/table/tbody[1]/tr/td[3]
	#floo = container.
	#floor.append(floo)


	# ku name 
	ku = soup.find('div', class_='designateline-box-txt02').text  # will need to scrape some of this off 
	ku_name.append(ku)

	# year built 
	year = container.
	year_built.append(year)


	# apartment_type
	aprt = container.find("span", class_="cassetteitem_madori").text # will have to clean this later
	apartment_type.append(apart)

	# administration - span "cassetteitem_price cassetteitem_price--administration"
	admin = container.find('span', class_="cassetteitem_price cassetteitem_price--administration")
	maintenence_price.append(admin)


df_ = pr.DataFrame({'rent_price': rent_price, 
	'address' : address,
	'sqr_m' : sqr_m,
	'name_place' : name_place,
	'rei_price' : rei_price,
	'maintenence_price' : maintenence_price,
	'nearest_eki' : eki,
	'apartment_type' : apartment_type,
	'year_built' : year_built,
	'ku_name' : ku_name,
	'place_name' : place_name,
	'house_type': house_type})
os.chdir('~/Downloads/')

df_.to_csv('apartment.csv')

