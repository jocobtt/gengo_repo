import requests 
import googlemaps 
import pandas 
import os 
import numpy as np 

# test apartment 
apart_address = "4-chome-8 Togoshi, Shinagawa City, Tokyo-to 142-0041, Japan"

# make a list of local church addresses to loop through 
church addresses = ['1 Chome-8-14 Eharacho, Nakano City, Tokyo 165-0023, Japan', '1 Chome-7-7 Kichijoji Higashicho, Musashino, Tokyo 180-0002, Japan']

gmaps = googlemaps.Client(key="my-keyfile")


def church_dist(apart_address, church_addresses, mode):
	dist = []
	#apart_address =
	for addy in church_addresses:
		dist = gmaps.distance_matrix(origins = apart_address, 
			destination = addy,
			mode = mode,
			transit_routing_preference = "fewer_transfers",
			transit_mode = ["subway", "train", "bus"])

		return dist[1] 

