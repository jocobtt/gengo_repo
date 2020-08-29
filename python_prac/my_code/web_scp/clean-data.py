import pandas as pd 
import numpy as np 
import os 
from bs4 import BeautifulSoup


os.chdir('~/Downloads')
df = pd.read_csv('apartment.csv')


# convert numeric values into proper numeric values etc. 