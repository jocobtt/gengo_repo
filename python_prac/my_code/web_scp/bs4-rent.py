# https://erikrood.com/Python_References/web_scrape.html
#https://linuxhint.com/python-beautifulsoup-tutorial-for-beginners/
# https://gist.github.com/ibnesayeed/b4b069b8007f68be91a179a099e35d71
#https://realpython.com/beautiful-soup-web-scraper-python/

import requests
import pandas as pd 
from bs4 import BeautifulSoup
import numpy as np 

URL = [
"https://suumo.jp/chintai/tokyo/"
# other urls 

]

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='')

# info I need from apartment stuff - rent price, distance from places, general location/address, overall square feet, year made, story its at, rei amount, and name of the place

"""loop through things version
"""

for b in URL:
	html = requests.get(b).text
	soup = BeautifulSoup(html, "html.parser")
	# grab table we want to scrape

rent_vals = []
for rent in rent_elems:
	rent_price = rent.find('span', class='cassetteitem_price_cassetteitem_price--rent')
	address = rent.find('li', class='cassettitem_detail-col1')
	sqr_m = rent.find('span', class='cassettitem_menseki')
	name_place = rent.find('div', class='cassetteitem_content_title')
	rei_price = rent.find('div', class='cassetteitem_price cassetteitem_price--gratuity')
	distance = rent.find('li', class='cassetteitem_detail-col2')
	aparment_type = rent.find('span', class='cassetteitem_madori')
	print(rent_price.text)

boar_arr = np.asarray(rent_vals)
df = pd.DataFrame(boar_arr)

df.columns = [names]



