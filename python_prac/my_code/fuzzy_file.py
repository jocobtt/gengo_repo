import pandas as pd 
import os, json

# for right now I am trying to do this to play around with fuzzy matching, but there originally was a purpose for this script that I have since forgotten about.... I think it was a way for me to find certain files that I forgot the exact names for.. 

# import fuzzy matching library 
from fuzzywuzzy import fuzz, process

#https://towardsdatascience.com/natural-language-processing-for-fuzzy-string-matching-with-python-6632b7824c49
# https://towardsdatascience.com/fuzzy-string-matching-in-python-68f240d910fe



# loop through file system for files I input in 
for filename in os.listdir(directory):
	if filename.endswith(".py") or 

def get_file(desired_file, comp_file):
	os.

