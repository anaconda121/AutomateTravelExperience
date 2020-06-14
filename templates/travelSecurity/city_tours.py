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
from templates.travelSecurity import hotels
def city_tours_planning():
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

	print('location', trip_location, 'length', 'trip_length', 'start date', trip_start_date, 'end date', trip_end_date, 'num going',
		num_people, 'purpose_trip', purpose_trip, 'living', living_accomdations, 'place 1', attractions_one, 'place 2', attractions_two, 'activity 2', attractions_two_activity,
		'place 3', attractions_three, 'place 4', attractions_four, 'timeline 1', vacation_timeline_one,'price part 1', vacation_timline_one_price)

	PATH = "C:\Program Files (x86)\chromedriver.exe"

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
		def city(raw_string):
			city_name = raw_string.split(', ')
			city_name_final = city_name[0]
			print(city_name_final)
			return (city_name_final)

		#attractions work
		@staticmethod
		def calc_custom_id(custom_activity):
			if attractions_one_activity == 'All':
				custom_id = ""
			elif attractions_one_activity == 'Architecture':
				custom_id = "1"
			elif attractions_one_activity == 'Art':
				custom_id = "2"
			elif attractions_one_activity == 'Food':
				custom_id = "3"
			elif attractions_one_activity == 'Family':
				custom_id = "4"
			elif attractions_one_activity == "History":
				custom_id = "5"
			elif attractions_one_activity == "Orientation":
				custom_id = "6"
			elif attractions_one_activity == 'Jewish Heritage':
				custom_id = "7"
			elif attractions_one_activity == 'Excursions':
				custom_id = "8"
			elif attractions_one_activity == 'Custom':
				custom_id = "10"
			elif attractions_one_activity == 'Vatican':
				custom_id = "11"
			elif attractions_one_activity == 'Colossuem':
				custom_id = "12"
			elif attractions_one_activity == 'Cruise Experiences':
				custom_id = "13"
			elif attractions_one_activity == 'Private Guides':
				custom_id = "15"
			else:
				custom_id = "0"
			return custom_id

		def city_tours_walking(self, vacation_timeline, num_people, custom_activity):
			check_in_day = Planner.date_cleaner_start(vacation_timeline)
			check_out_day = Planner.date_cleaner_end(vacation_timeline)
			tour_size = num_people + 1
			custom_id = Planner.calc_custom_id(custom_activity)
			city_name = Planner.city(vacation_timeline)

			url_city = "https://www.contexttravel.com/cities/{city}/tours?utf8=%E2%9C%93&start_date={start_date}&end_date={end_date}&pax={num_people}&interest_id={custom_id}&tour_type=&button="\
			.format(city = city_name, \
					start_date = check_in_day, \
					end_date = check_out_day, \
					num_people = tour_size, \
					custom_id = custom_id)

			search_city = self.driver.get(url_city)
			content = None
			self.driver.implicitly_wait(5)
			time.sleep(10)
		'''
		#sports game
		@staticmethod
		def sport_city_clean (org_str):
			city_name = org_str.split(', ')
			city_name_final = city_name[0]
			bad_chars = [',']

			for i in range(len(city_name_final)):
				if city_name_final[i] == bad_chars:
					city_name_final[i].replace(city_name_final[i],'')
		  
			return city_name_final

		@staticmethod
		def clean_dates_start_sports(org_str):
			dates_one_start_two = org_str.split('-')
			dates_one_start_final = dates_one_start_two[2] +"0"+dates_one_start_two[0]+ dates_one_start_two[1]+"00"
			return (dates_one_start_final)

		@staticmethod
		def clean_dates_end_sports(org_str):
			dates_one_end_two = org_str.split('-')
			dates_one_end_final = dates_one_end_two[2] +"0"+dates_one_end_two[0]+ dates_one_end_two[1]+"23"
			return ( dates_one_end_final)

		def sports_game(self, dates, vacation_timeline, sport):
			date_one = Planner.clean_dates_start_sports(dates)
			date_two = Planner.clean_dates_end_sports(dates)
			city = Planner.sport_city_clean(vacation_timeline)
			sport = sport

			url_sport = "https://eventful.com/{city}/events?q={sport}&ga_search={sport}&ga_type=events&t={start_date}-{end_date}"\
			.format(city = city, \
					sport = sport, \
					start_date = date_one, \
					end_date = date_two)
			search_sport = self.driver.get(url_sport)
			content = None
			self.driver.implicitly_wait(5)
			time.sleep(10)

		#sightseeing work
		@staticmethod
		def calc_url_extension_sightsee(sightsee_subjects):
			if sightsee_subjects == 'All':
				url_extension = '&ct=1-27-35-54-123-239&p=1'
			elif sightsee_subjects == 'Tours':
				url_extension = '&ct=1&p=1'
			elif sightsee_subjects == 'Culture and History':
				url_extension = '&ct=27'
			elif sightsee_subjects == 'Nature and Adventure':
				url_extension = '&ct=35&p=1'
			elif sightsee_subjects == 'Activities that are wheelchair accessible':
				url_extension = '&ct=239&p=1'
			return url_extension

		def sight_seeing(self, vacation_timeline, subjects):
			date_from = Planner.date_cleaner_start(vacation_timeline)
			date_end = Planner.date_cleaner_end(vacation_timeline)
			city = location_sightsee
			sightsee_subjs = Planner.calc_url_extension_sightsee(subjects)
			url_sightsee = "https://www.getyourguide.com/s/?q={city}&date_from={start_date}&date_to={end_date}&sort=rating&order=desc{extension}"\
			.format(city = city, \
					start_date = date_from, \
					end_date = date_end, \
					extension = sightsee_subjs)

			search_sights = self.driver.get(url_sightsee)
			content = None
			self.driver.implicitly_wait(5)
			time.sleep(10)
		'''
	planner = Planner()
	if attractions_one == 'City Tours':
		planner.city_tours_walking(vacation_timeline_one, int(num_people), attractions_one_activity)
	'''
	elif attractions_two == 'Sports Game':
		planner.sports_game(attractions_location, vacation_timeline_one ,attractions_two_activity)
	elif attractions_three == 'Sight-Seeing':
		planner.sight_seeing(vacation_timeline_one, sightsee_subjects)
	'''
