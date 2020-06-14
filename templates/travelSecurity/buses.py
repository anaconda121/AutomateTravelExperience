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

def buses():

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

	print('avg' ,avg_age,'num', num_people, 'rel', relationship)

	if bus_medium ==  'Buses':
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

			@staticmethod
			def count_people_type(num, avg_age):
				if avg_age > 0 and avg_age <= 18:
					result = "youths=", avg_age
				elif avg_age > 18 and avg_age <= 70:
					result = "adults=", avg_age
				elif avg_age > 70:
					result = "seniors=", avg_age
				return result

			def search_for_buses(self, vacation_str, city, num, avg_age):
				start_date = Planner.date_cleaner_start(vacation_str)
				end_date = Planner.date_cleaner_end(vacation_str)
				city_origin = Planner.city_from(city)
				city_end = Planner.city_to(city)
				count_people_type = Planner.count_people_type(num, avg_age)

				url_buses = "https://www.rome2rio.com/redirects/omio/?oDateTime={start_date}&iDateTime={end_date}&{type}&ages=&checkoutExitLabel=fe1:mlp:ts:nv:na&origin={city_origin}&destination={city_end}&mode=&lang=en&currency=USD&requestId=178-20200614-053907-7373694"\
				.format(start_date = start_date, \
						end_date = end_date, \
						type = count_people_type, \
						city_origin = city_origin, \
						city_end = city_end)

				search_buses = self.driver.get(url_buses)
				content = None
				self.driver.implicitly_wait(5)
				time.sleep(10)

		planner = Planner()
		planner.search_for_buses(vacation_timeline_one, city_total, int(num_people), int(avg_age))