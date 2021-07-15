# Using BeatifulSoup to extract the same
from bs4 import BeautifulSoup as bs4
import requests
response = requests.request('GET','https://www.google.com/maps/d/viewer?mid=1Z1dI8hoBZSJNWFx2xr_MMxSxSxY&ll=10.602124500000008%2C-66.9955364&z=8')
soup = bs4(response.text,'html.parser') 
text = soup.find("div")
str(text).split(',0,')