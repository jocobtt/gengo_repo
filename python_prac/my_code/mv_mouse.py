import pyautogui # so i can move my mouse every 30 minutes 
import numpy as np 
import time 
import helium  # so that I can hit refresh every hour 


# now just need to make this run via docker or kubernetes instead 


driver = start_chrome("sgf_website")
driver.write("login_credentials")

# move mouse every 31 minutes
pyautogui.drageTo(np.random.randit(0,150,1), np.random.randit(0,150,1))  # generate a random digit from 0 to 150 for both pixel values 
time.sleep(31)   # wait 31 minutes

# hit refresh every 1 hour 
time.sleep(100)
driver.refresh() 
