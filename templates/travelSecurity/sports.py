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

def sports():
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


	planner = Planner()

	if attractions_two == 'Sports Game':
		planner.sports_game(attractions_location, vacation_timeline_one ,attractions_two_activity)
