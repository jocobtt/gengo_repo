# transit 
import requests 
import pandas as pd
import numpy as np 
import os 
import googlemaps 

print("beginning googlemaps loop/function for time to get to work")
# get time of to get to work via transit from potential apartment's nearest station via the googlemaps python api https://github.com/googlemaps/google-maps-services-python
gmaps = googlemaps.Client(key="my-keyfile")
# should this instead be a function? 

# try this as a function - still need to figure out what is wrong with getting transit info - will probably have to instead get info from eki to work instead 
def get_distance_(station, work, mode, transi_mode, address):  # should I include time I am going to commute at? 
# also put in how many address to do at a time clause? 
	time_to_work = []
	work = '6 Chome-10-1 Roppongi, Minato City, Tokyo 106-0032, Japan'
	
	# will instead have to look it up from closest station instead of actual address maybe?
	example_address = "4-chome-8 Togoshi, Shinagawa City, Tokyo-to 142-0041, Japan"

	# test out function first 
	geocode_result = gmaps.geocode(address[1])
	geocode_result

	# look to see how limited I am with the API, may have to break this up 
	#if transit_mode == "transit":



	if len(apartment) > 100000:
		for  in address:
			addy = gmaps.geocode(address)  # will have to check this whole thing 
			addy = addy[0]["geometry"]["location"]
			lon = addy[]
			lat = 
			now = datetime.now()
			distance_result = gmaps.directions(origins = station, 
				destination = work, 
				mode = mode, 
				transit_routing_preference = "fewer_transfers",
				transit_mode = ["subway", "train", "bus"]
				)
			time_to_work = distance_result['rows'][0]['elements'][0]['distance']['text'] # filter from output  
			time_result = distance_result['rows'][0]['elements'][0]['duration']['text']

	else:
		print("too many apartment listings in this dataset to do at once! Need to break it up")


# https://github.com/Zeletochoy/navitime/blob/master/navitime/cli.py

def get_bikes(station, work, mode, transi_mode, address):  # should I include time I am going to commute at? 
# also put in how many address to do at a time clause? 
	bike_to_work = []
	work = '6 Chome-10-1 Roppongi, Minato City, Tokyo 106-0032, Japan'
	
	# will instead have to look it up from closest station instead of actual address maybe?
	example_address = "4-chome-8 Togoshi, Shinagawa City, Tokyo-to 142-0041, Japan"

	# test out function first 
	geocode_result = gmaps.geocode(address[1])
	geocode_result

	# look to see how limited I am with the API, may have to break this up 
	#if transit_mode == "transit":



	if len(apartment) > 100000:
		for  in address:
			addy = gmaps.geocode(address)  # will have to check this whole thing 
			addy = addy[0]["geometry"]["location"]
			lon = addy[]
			lat = addy[]
			now = datetime.now()
			distance_result = gmaps.directions(origins = station, 
				destination = work, 
				mode = mode
				)
			time_to_work = distance_result['rows'][0]['elements'][0]['distance']['text'] # filter from output  
			time_result = distance_result['rows'][0]['elements'][0]['duration']['text']
			

	else:
		print("too many apartment listings in this dataset to do at once! Need to break it up")


# https://github.com/Zeletochoy/navitime/blob/master/navitime/cli.py



