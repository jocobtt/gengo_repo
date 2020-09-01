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
import googlemaps
from datetime import datetime

# this has all of the ku's I want - so use this instead of multiple URLs
URL = "https://suumo.jp/jj/chintai/ichiran/FR301FC001/?ar=030&bs=040&pc=50&smk=&po1=25&po2=99&shkr1=03&shkr2=03&shkr3=03&shkr4=03&sc=13101&sc=13102&sc=13103&sc=13104&sc=13105&sc=13113&sc=13106&sc=13107&sc=13108&sc=13118&sc=13109&sc=13110&sc=13111&sc=13112&sc=13114&sc=13115&sc=13116&ta=13&cb=0.0&ct=9999999&md=02&md=03&md=04&md=05&md=06&et=9999999&mb=0&mt=9999999&cn=9999999&tc=0400301&fw2="


########################################
####      final code solution       ####
########################################

# print off that it is starting the loop 
print("Starting Loop...")

print("for ")


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
time_to_work = []

s = requests.session()
headers = {
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
}
s.headers.update(headers)

pages = np.arange(1,100,1) # first test out on 100 then go from there 
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
		sqr = container.find('span', class_="cassetteitem_menseki").text 
		sqr_m.appen(sqr)
		name = container.div.li.text
		name_place.append(name)
		sleep(np.random.randint(2,3))
		rei = container.find('span', class_="cassetteitem_price cassetteitem_price--gratuity").text # will have to clean this later
		rei_price.append(rei)
		eki_ = container.find('div', class_='cassetteitem_detail-text')
		eki.apend(eki_)
		house = container.find('span',class_='ui-pct ui-pct--util1').text 
		house_type.append(house)
		sleep(np.random.randint(2,3))
		floo = container.find('li', class_='cassetteitem_detail-col3').div.text
		floor.append(floo)
		ku = soup.find('div', class_='designateline-box-txt02').text  
		ku_name.append(ku)
		sleep(np.random.randint(2,3))
		year = container.find('li', class_='cassetteitem_detail-col3').text[5:] # will have to drop stuff from this 
		year_built.append(year)
		aprt = container.find("span", class_="cassetteitem_madori").text # will have to clean this later
		apartment_type.append(apart)
		admin = container.find('span', class_="cassetteitem_price cassetteitem_price--administration").text
		maintenence_price.append(admin)

# print that loop has completed 
print("Loop finished.... Converting to csv now.")

print("beginning googlemaps loop for time to get to work")
# get time of to get to work via transit from potential apartment via the googlemaps python api https://github.com/googlemaps/google-maps-services-python
gmaps = googlemaps.Client(key="my-keyfile")

# test out function first 
geocode_result = gmaps.geocode(address[1])

# look to see how limited I am with the API, may have to break this up 
if len(apartment) > 100000:
	for  in address:
		addy = gmaps.geocode(address)  # will have to check this whole thing 
		now = datetime.now()
		distance_result = gmaps.distance_matrix(origins = address, 
			destination = '6 Chome-10-1 Roppongi, Minato City, Tokyo 106-0032, Japan', 
			mode="transit", 
			transit_routing_preference = "fewer_transfers",
			transit_mode = ["subway", "train", "bus"]
			)
		time_to_work = distance_result #?

else:
	print("too many apartment listings in this dataset to do at once! Need to break it up")





# save to data frame
df_ = pd.DataFrame({'rent_price': rent_price, 
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
	'floor' : floor,
	'house_type': house_type, 
	'time_to_work': ttw})

# os.chdir('~/Downloads/') -- don't need this yet
# save as csv
df_.to_csv('apartment.csv')

print("All done! Go checkout apartment.csv file now and run model and data cleaning file!")

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


df_ = pd.DataFrame({'rent_price': rent_price, 
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

# Initiate a session and update the headers. Still need to work through this logic 
# - from https://stackoverflow.com/questions/57983718/could-not-scrape-a-japanese-website-using-beautifulsoup
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
		sleep(np.random.randint(2,15)) # wait 2-15 seconds between each apartment container
		renty = container.tbody.ul.span.text
		rent_price.append(renty)

rent_price 




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
floor = []

pages = np.arange(1,251,1)

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

	# floor 
	floo = container.find('li', class_='cassetteitem_detail-col3').div.text
	floor.append(floo)


	# ku name 
	ku = soup.find('div', class_='designateline-box-txt02').text  
	ku_name.append(ku)

	# year built 
	year = container.find('li', class_='cassetteitem_detail-col3').text[5:] # will have to drop stuff from this 
	year_built.append(year)


	# apartment_type
	aprt = container.find("span", class_="cassetteitem_madori").text # will have to clean this later
	apartment_type.append(apart)

	# administration 
	admin = container.find('span', class_="cassetteitem_price cassetteitem_price--administration").text
	maintenence_price.append(admin)



# will still have to clean data it looks like 

df_ = pd.DataFrame({'rent_price': rent_price, 
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
	'floor' : floor,
	'house_type': house_type})
os.chdir('~/Downloads/')

df_.to_csv('apartment.csv')

