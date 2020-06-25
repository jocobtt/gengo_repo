import pandas as pd 
import numpy as np 
import helium 


start_chrome('linkedin.com/login',headless=True)
write('jacob.braswell@sas.com',into="Email or Phone")
write(password.paz, into="Password")  # find way to make this be more secure 
click('Sign in')

# get to page I want
write("person", into="Search)
press(ENTER)

# click on person's page

# scroll down 


def scrape_from(url, username, password, person):
	start_chrome(url, headless=True)
	
	write(username, into='Email or Phone')
	write(password, into='Password')
	click('Sign in')

	# go to page we want
	write(person, into="Search")
	press(ENTER)

	# click on persons page 

	# scroll down 

	# endorse on a random skill?

	# pull some data
	
	print("job ran successfully")
