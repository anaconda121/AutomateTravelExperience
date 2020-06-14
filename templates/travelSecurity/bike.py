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

def bike():

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

	if bike_medium == 'Bike':
		class Planner():
			def __init__(self):
				self.driver = webdriver.Chrome(ChromeDriverManager().install()) #using chrome browser

			@staticmethod
			def city_from(raw_string):
				city_name = raw_string.split(', ')
				city_name_final = city_name[0]
				print(city_name_final)
				return (city_name_final)

			@staticmethod
			def calc_month(vacation_str):
				vacation_str_split = vacation_str.split(", ")
				vacation_str_iso = vacation_str_split[1]
				vacation_str_dash = vacation_str_iso.split("-")
				vacation_str_dash_two = vacation_str_dash[0]
				vacation_str_dash_three = vacation_str_dash_two.split('/')
				month = vacation_str_dash_three[0]

				if int(month) == 1:
					month = "Jan"
				elif int(month) == 2:
					month = "Feb"
				elif int(month) == 3:
					month = "Mar"
				elif int(month) == 4:
					month = "Apr"
				elif int(month) == 5:
					month = "May"
				elif int(month) == 6:
					month = "Jun"
				elif int(month) == 7:
					month = "Jul"
				elif int(month) == 8:
					month = "Aug"
				elif int(month) == 9:
					month = "Sep"
				elif int(month) == 10:
					month = "Oct"
				elif int(month) == 11:
					month = "Nov"
				elif int(month) == 12:
					month = "Dec"
				  
				return month

			@staticmethod
			def calc_month_end(vacation_str):
				vacation_str_split = vacation_str.split(", ")
				vacation_str_iso = vacation_str_split[1]
				vacation_str_dash = vacation_str_iso.split(":")
				print('str dash', vacation_str_dash)
				vacation_str_dash_two = vacation_str_dash[1]
				print('dash 22', vacation_str_dash_two)
				vacation_str_dash_three = vacation_str_dash_two.split('-')
				month = vacation_str_dash_three[0]

				if int(month) == 1:
					month = "Jan"
				elif int(month) == 2:
					month = "Feb"
				elif int(month) == 3:
					month = "Mar"
				elif int(month) == 4:
					month = "Apr"
				elif int(month) == 5:
					month = "May"
				elif int(month) == 6:
					month = "Jun"
				elif int(month) == 7:
					month = "Jul"
				elif int(month) == 8:
					month = "Aug"
				elif int(month) == 9:
					month = "Sep"
				elif int(month) == 10:
					month = "Oct"
				elif int(month) == 11:
					month = "Nov"
				elif int(month) == 12:
					month = "Dec"
				  
				return month				

			@staticmethod
			def format_month_start(vacation_str, month):
				vacation_str_split = vacation_str.split(", ")
				vacation_str_iso = vacation_str_split[1]
				vacation_str_dash = vacation_str_iso.split(":")
				vacation_str_dash_two = vacation_str_dash[0]
				vacation_str_dash_three = vacation_str_dash_two.split('-')
				print('v2',vacation_str_dash_two)
				print('v3',vacation_str_dash_three)
				start_month = month+"%20"+vacation_str_dash_three[1]+"%20"+vacation_str_dash_three[2]
				return start_month

			@staticmethod
			def format_month_end(vacation_str, month):
				vacation_str_split = vacation_str.split(", ")
				vacation_str_iso = vacation_str_split[1]
				print('iso', vacation_str_iso)				
				vacation_str_dash = vacation_str_iso.split(":")
				vacation_str_dash_two = vacation_str_dash[1]
				vacation_str_dash_three = vacation_str_dash_two.split('-')
				print('dashes', vacation_str_dash_three)

				start_month = month+"%20"+vacation_str_dash_three[1]+"%20"+vacation_str_dash_three[2]
				return start_month

			def search_bike(self, vacation_str, city):
				city = Planner.city_from(city)
				month_pre = Planner.calc_month(vacation_str)
				print('month pre', month_pre)
				start_date = Planner.format_month_start(vacation_str, month_pre)
				month_post = Planner.calc_month_end(vacation_str)
				print('month post', month_post)
				end_date = Planner.format_month_end(vacation_str, month_post)

				url_bike = "https://www.spinlister.com/search?utf8=%E2%9C%93&q={city}&avail_start={start_date}%2002:06:49%20GMT-0400%20(Eastern%20Daylight%20Time)&avail_end={end_date}%2002:06:51%20GMT-0400%20(Eastern%20Daylight%20Time)"\
				.format(city = city, \
						start_date = start_date, \
						end_date = end_date)

				search_bike = self.driver.get(url_bike)
				content = None
				self.driver.implicitly_wait(5)
				time.sleep(10)

		planner = Planner()
		planner.search_bike(vacation_timeline_one, city)

