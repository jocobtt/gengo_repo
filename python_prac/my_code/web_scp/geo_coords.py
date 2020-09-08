import os 
import requests 
import googlemaps 

def geo_coord(address):
	geo_code = []
	if len(address) > 1000:
		for adresses in address:
			geo_code = gmaps.geocode(address)

			return geo_code
	else:
		print("need a smaller dataset to pull from")