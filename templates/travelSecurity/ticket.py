'''
import tensorflow as tf 
from tensorflow import keras 
from tensorflow.keras import datasets, layers, models
'''
import cgi #getting info from form
import sys
import numpy as np 
from numpy import NaN
import pandas as pd 
from flask import Flask, request, render_template
from webdriver_manager.chrome import ChromeDriverManager
from geopy.distance import geodesic 
#location
import geopandas as gpd 
import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime
import sys
from bs4 import BeautifulSoup as bs
import re
import smtplib
from email.mime.text import MIMEText
from subprocess import Popen, PIPE
import pickle
import argparse

print("Content-Type: text/html; charset = utf-8\n\n")

#loading in datsets
prices_domestic = pd.read_csv('templates/travelSecurity/Datasets/passengers/prices.csv') #app.py - 'templates/travelSecurity/Datasets/passengers/prices.csv'
#ages = pd.read_csv('Datasets/ticket/ages.csv') #app.py - templates/travelSecurity/Datasets/ticket/ages.csv
#iso_global = pd.read_csv('Datasets/ticket/iso.csv')  #app.py - templates/travelSecurity/Datasets/ticket/iso.csv

#getting avg price of domestic ticket over last 25 years
del prices_domestic['number']
avg_prices_domestic = np.arange(25)

for i in range(25):
	avg_prices_domestic[i] = prices_domestic['prices'].where(prices_domestic['id'] == i+1).dropna()
	#print(avg_prices_domestic)
	i += 1

prices_domestic_final = 0
for i in range(len(avg_prices_domestic)):
	prices_domestic_final += avg_prices_domestic[i]

#print(prices_domestic_final/(len(avg_prices_domestic)))
#print(prices_domestic['id'])
#print(prices_domestic['prices'])
#print(avg_prices_domestic)

#price of international ticket
price_international = 1200

#average ages of people with Covid

#see likelihood of sickness (corona)

def processTicket():
	class Expedia:
	    def __init__(self):
	        self.driver = webdriver.Chrome(ChromeDriverManager().install())
	    

	    def search(self, origin_city, destination_city, start_date, return_date):
	        data_storage = open('flight-price.txt', 'a')
	        data_storage.write('-'*30 + '\n' + datetime.date.today().strftime('%b %d %Y result:') + '\n')

	        url = "https://www.expedia.com/Flights-Search?trip=roundtrip&leg1=from:{org_city},to:{dest_city},departure:{origin_date}TANYT&leg2=from:{dest_city},to:{org_city},departure:{return_date}TTANYT&passengers=children:0,adults:1&mode=search" \
	                .format(org_city=origin_city, \
	                dest_city=destination_city, \
	                origin_date=start_date, \
	                return_date=return_date)

	        search = self.driver.get(url)
	        # print search
	        time.sleep(10)
	        content = None

	address_input = request.form['address']
	airline_input = request.form['airline']
	airport_from = request.form['airport_from']
	airplane_destination = request.form['destination']
	price = request.form['price_person']
	num_people = request.form['num_people']
	average_age = request.form['average']
	relationship = request.form['relationship']
	outcity = request.form['airport_one']
	incity = request.form['airport_two']
	out_date = request.form['date_one']
	in_date = request.form['date_two']

	print('address', address_input, 'airline', airline_input, 'from', airport_from, 'going', airplane_destination, 
	'price', price, 'number peeps', num_people, 'avg', average_age, 'relationship', relationship, file = sys.stderr)

	#starting evaluation - determining if domestic or international
	split_start = airport_from.split(',')
	split_landing = airplane_destination.split(',')

	#print(split_start, "  ", split_landing)
	if split_start[2].lower() == split_landing[2].lower():
		is_domestic = True
		points = 500
		price = 442.44
		recommended_score = 10251.55
		print('flight is domestic')
	else:
		is_domestic = False
		points = 5000
		price = 1200.82 #change back to 991 after scrape test
		recommended_score = 13500.33
		print('flight is international')

	#getting latitude and longitude coorondiantes from form
	locator = Nominatim(user_agent="myGeocoder")
	location = locator.geocode(airport_from)
	location_2 = locator.geocode(airplane_destination)

	''' "LatitudeFrom = {}, LongitudeFrom = {}".format, "LatitudeTo = {}, LongitudeTo = {}".format'''
	original_location = (location.latitude, location.longitude)
	destiantion_location = (location_2.latitude, location_2.longitude)

	#getting actual distance from coordiantes
	#original_location = (location.latitude, location.longitude)
	#desintation_location = (location_2.latitude, location_2.longitude)

	print('org_location', original_location)
	print('destination', destiantion_location)

	distance = geodesic(original_location, destiantion_location).km
	distance_miles = 0.621371 * distance
	print('Distance between both airports', distance_miles)

	#calculate time for flight (mins)
	time_flight_mins = (distance_miles / 9.41667) + 66 + 120
	time_flight_hours = time_flight_mins / 60

	print('time for flight in hours', time_flight_hours, 'time for flight in mins', time_flight_mins)

	#calculating how far airport is from address
	home = locator.geocode(address_input)
	home_coords = (home.latitude , home.longitude)

	home_distance_airport = geodesic(home_coords, original_location).km

	#calculating time from home to airport
	home_distance_miles = 0.621371 * home_distance_airport
	print('Distance between airport and home', home_distance_miles)

	home_to_aiport_mins = (home_distance_miles / 9.41667) + 20
	home_hours = home_to_aiport_mins / 60
	print('distance to airport in mins', home_to_aiport_mins, 'distance to airport hours', home_hours)

	#calculating total score
	total_airport_score = points + distance_miles + time_flight_hours + home_distance_miles + home_hours + price
	print('total airport score is: ', total_airport_score)

	if total_airport_score > recommended_score:
		print('Your airport score is too high by: ', total_airport_score - recommended_score, " Here are some options that may be better")
		expedia = Expedia()
		expedia.search(outcity,incity,out_date,in_date)	
		return False
	else :
		return True


	

