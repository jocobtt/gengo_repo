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
""
# other urls?  

]

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

rent = soup.find_all('span', class_='cassetteitem_other-emphasis ui-text--bold')

# info I need from apartment stuff - rent price, distance from places, general location/address, overall square feet, year made, story its at, rei amount, and name of the place

"""loop through things version
"""

for b in URL:
	html = requests.get(b).text
	soup = BeautifulSoup(html, "html.parser")
	# grab table we want to scrape

rent_price = []
address = []
sqr_m = []
name_place = []
rei_price = []
distance = []
apartment_type = []

for rent in rent_elems:
	rent_price = rent.find('span', class_='cassetteitem_other-emphasis ui-text--bold')
	address = rent.find('li', class_='cassettitem_detail-col1')
	sqr_m = rent.find('span', class_='cassettitem_menseki')
	name_place = rent.find('div', class_='cassetteitem_content_title')
	rei_price = rent.find('div', class_='cassetteitem_price cassetteitem_price--gratuity')
	distance = rent.find('li', class_='cassetteitem_detail-col2')
	aparment_type = rent.find('span', class_='cassetteitem_madori')
	print(rent_price.text)



df_ = pr.DataFrame({'rent_price': rent_price, 
	'address' : address,
	'sqr_m' : sqr_m,
	'name_place' : name_place,
	'rei_price' : rei_price,
	'distance' : distance,
	'apartment_type' : apartment_type})

os.chdir('~/Downloads/')

df_.to_csv('apartment.csv')



