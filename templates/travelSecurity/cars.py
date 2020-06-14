from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys #allows bot to type things into search field
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from flask import Flask, request, render_template
import numpy as np
from numpy import NaN
import pandas as pd
from geopy.distance import geodesic
import geopandas as gpd
import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from bs4 import BeautifulSoup as bs
import datetime
import time

def cars():

	#getting input from form
	trip_location = request.form['place']
	trip_start_date = request.form['start']
	trip_end_date = request.form['end']
	num_people = request.form['num_people']

	if num_people == 0:
		avg_age = 0
		relationship = ""
	else:
		avg_age = request.form.get('average')
		relationship = request.form.get('relationship')

	purpose_trip = request.form['purpose']
	living_accomdations = request.form['room']
	attractions_one = request.form.get('attractions1')
	attractions_one_activity = request.form['custom']
	attractions_two = request.form.get('attractions2')
	attractions_two_activity = request.form['game_type']
	sightsee_subjects = request.form['sightsee']
	location_sightsee = request.form['location_sightsee']
	attractions_three = request.form.get('attractions3')
	attractions_four = request.form.get('attractions4')
	attractions_location = request.form['game_location']
	vacation_timeline_one = request.form['first_part']
	vacation_timline_one_price = request.form['first_part_price']

	train_medium = request.form.get('medium1')
	#subway_medium = request.form.get('medium2')
	car_medium = request.form.get('medium3')
	bus_medium = request.form.get('medium4')
	bike_medium = request.form.get('medium5')
	city = request.form['city']
	city_to = request.form['city_to']
	city_total = city + "," + city_to

	if car_medium == 'Cars':
		class Planner():
			def __init__(self):
				self.driver = webdriver.Chrome(ChromeDriverManager().install()) #using chrome browser

			@staticmethod
			def date_cleaner_start(org_str):
				vacation_timeline_one_split = org_str.split(', ')
				dates_one = vacation_timeline_one_split[1].split(' : ')
				dates_one_start = dates_one[0]
				dates_one_start_two = dates_one_start.split('-')
				dates_one_start_final = dates_one_start_two[2] +"-" + dates_one_start_two[0] +"-" + dates_one_start_two[1]
				return (dates_one_start_final)

			@staticmethod
			def date_cleaner_end(org_str):
				vacation_timeline_one_split = org_str.split(', ')
				dates_one = vacation_timeline_one_split[1].split(' : ')
				dates_one_end = dates_one[1]
				dates_one_end_two = dates_one_end.split('-')
				dates_one_end_final = dates_one_end_two[2] +"-" + dates_one_end_two[0] +"-" + dates_one_end_two[1]
				return (dates_one_end_final)

			@staticmethod
			def city_from(raw_string):
				city_name = raw_string.split(', ')
				city_name_final = city_name[0]
				print(city_name_final)
				return (city_name_final)

			@staticmethod
			def city_to(raw_string):
				city_name = raw_string.split(', ')
				city_name_final = city_name[1]
				print(city_name_final)
				return (city_name_final)

			def search_for_cars(self, vacation_str, city):
				start_date = Planner.date_cleaner_start(vacation_str)
				end_date = Planner.date_cleaner_end(vacation_str)
				age = avg_age
				start_city = Planner.city_from(city)
				end_city = Planner.city_to(city)

				locator = Nominatim(user_agent="myGeocoder")
				start_coords = locator.geocode(start_city)
				start_coords_final = (start_coords.latitude, start_coords.longitude)

				end_coords = locator.geocode(end_city)
				end_coords_final = (end_coords.latitude, end_coords.longitude)

				url_car = "https://go.easycar.com/en/book?pickupDateTime={pickup_date}T10%3A30&returnDateTime={return_date}T10%3A30&age={age}&clientID=874329&residenceID=US&currency=USD&elID=1031591800399268&pickupLat={pickup_lat}&pickupLng={pickup_long}&pickupName=Metropolitan%20City%20of%20{start_city}%2C%20&dropoffName=Metropolitan%20City%20of%20{return_city}&dropoffLat={dropoff_lat}&dropoffLng={dropoff_long}&%2C%20#/vehicles"\
				.format(pickup_date = start_date, \
						return_date = end_date, \
						age = age, \
						pickup_lat = start_coords.latitude, \
						pickup_long = start_coords.longitude, \
						start_city = start_city, \
						return_city = end_city, \
						dropoff_lat = end_coords.latitude, \
						dropoff_long = end_coords.longitude)

				search_car = self.driver.get(url_car)
				content = None
				self.driver.implicitly_wait(5)
				time.sleep(10)

		planner = Planner()
		planner.search_for_cars(vacation_timeline_one, city_total)