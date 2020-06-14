from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys #allows bot to type things into search field
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
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
import multiprocessing as mp
import datetime
import time

def trip_planning():
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
	attractions_three = request.form.get('attractions3')
	attractions_four = request.form.get('attractions4')
	attractions_location = request.form['game_location']
	vacation_timeline_one = request.form['first_part']
	vacation_timline_one_price = request.form['first_part_price']
	'''
	vacation_timeline_two = request.form['second_part']
	vacation_timline_two_price = request.form['second_part_price']
	vacation_timeline_three = request.form['third_part']
	vacation_timline_three_price = request.form['third_part_price']
	vacation_timeline_four = request.form['fourth_part']
	vacation_timline_four_price = request.form['fourth_part_price']
	'''
	print('location', trip_location, 'length', 'trip_length', 'start date', trip_start_date, 'end date', trip_end_date, 'num going',
		num_people, 'purpose_trip', purpose_trip, 'living', living_accomdations, 'place 1', attractions_one, 'place 2', attractions_two,
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

		@staticmethod
		def calc_room_size(family):
			if family == 0:
				room_size = 1
			elif family >= 1 and family < 3:
				room_size = 7
			else:
				room_size = 9
			return room_size

		def hotels_trivago(self, vacation_timeline_str, num_people_arg):
			print('peopless', num_people_arg)
			#cleaning up data
			start_date_one = str(Planner.date_cleaner_start(vacation_timeline_str))
			end_date_one = str(Planner.date_cleaner_end(vacation_timeline_str))
			city = Planner.city(vacation_timeline_str)
			room_size = Planner.calc_room_size(num_people_arg)
			print("check_in", start_date_one, "check_out", end_date_one, "city", city, "room type", room_size)
			#return (start_date_one, end_date_one, city, room_size)

			#searching fr now
			if city == "milan":
				url = "https://www.trivago.com/?aDateRange%5Barr%5D={start_date}&aDateRange%5Bdep%5D={end_date}&aPriceRange%5Bfrom%5D=0&aPriceRange%5Bto%5D=0&iRoomType={room_type}&aRooms%5B0%5D%5Badults%5D=2&cpt2=26352%2F200&hasList=1&hasMap=1&bIsSeoPage=0&sortingId=1&slideoutsPageItemId=&iGeoDistanceLimit=16093&address=&addressGeoCode=&offset=0&ra=&overlayMode="\
				.format(start_date = start_date_one, \
						room_type = room_size, \
						end_date = end_date_one )

				search = self.driver.get(url)
				content = None

				self.driver.implicitly_wait(5)
				time.sleep(10)

				'''
				main = WebDriverWait(driver, 10).until(
	        		city_type = EC.presence_of_element_located((By.ID, "querytext"))
	    		)
				
				city_type = self.driver.find_element_by_id("querytext")
				city_type.send_keys("MILAN")
				city_type.send_keys(Keys.RETURN)
				'''
				self.driver.quit()

			elif city == "rome":
				url = "https://www.trivago.com/?aDateRange%5Barr%5D={start_date}&aDateRange%5Bdep%5D={end_date}&aPriceRange%5Bfrom%5D=0&aPriceRange%5Bto%5D=0&iRoomType={room_type}&aRooms%5B0%5D%5Badults%5D=2&cpt2=25084%2F200&hasList=1&hasMap=1&bIsSeoPage=0&sortingId=1&slideoutsPageItemId=&iGeoDistanceLimit=16093&address=&addressGeoCode=&offset=0&ra=&overlayMode="\
				.format(start_date = start_date_one, \
						room_type = room_size, \
						end_date = end_date_one )

				search = self.driver.get(url)
				content = None

				self.driver.implicitly_wait(5)
				time.sleep(10)

		def find_house(self, vacation_timeline, num_people):
			check_in_day = planner.date_cleaner_start(vacation_timeline)
			check_out_day = planner.date_cleaner_end(vacation_timeline)
			room_size = num_people
			city = planner.city(vacation_timeline)

			url_airbnb = "https://www.airbnb.com/s/{city_name}/homes?tab_id=all_tab&refinement_paths%5B%5D=%2Fhomes&checkin={check_in}&checkout={check_out}&children=0&adults={num}&source=structured_search_input_header&search_type=search_query"\
            .format(city_name = city, \
                    check_in = check_in_day, \
                    check_out = check_out_day, \
                    num = num_people
            )
			search_airbnb = self.driver.get(url_airbnb)
			content = None

			self.driver.implicitly_wait(5)
			time.sleep(10)

	planner = Planner()
	if living_accomdations == 'Hotels':
		planner.hotels_trivago(vacation_timeline_one, int(num_people))
	elif living_accomdations == 'Air B&b':
		planner.find_house(vacation_timeline_one, num_people)

	city_name_two = planner.city(vacation_timeline_one)

	if city_name_two == 'milan':
		return 1
	elif city_name_two == 'rome':
		return 2
