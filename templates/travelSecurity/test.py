from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import cgi #getting info from form
import sys
import numpy as np 
from numpy import NaN
import pandas as pd 
from flask import Flask, request, render_template
from geopy.distance import geodesic 
#location
import geopandas as gpd 
import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from selenium import webdriver
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

def trip_planning():
	#getting input from form
	trip_location = request.form['place']
	trip_length = request.form['length']
	trip_start_date = request.form['start']
	trip_end_date = request.form['end']
	num_people = request.form['num_people']

	if num_people == 0:
		avg_age = 0
		relatioship = ""
	else:
		avg_age = request.form['average']
		relationship = request.form['relationship']

	purpose_trip = request.form['purpose']
	living_accomdations = request.form['room']
	attractions_one = request.form.getlist('attractions1')
	attractions_two = request.form.getlist('attractions2')
	attractions_three = request.form.getlist('attractions3')
	attractions_four = request.form.getlist('attractions4')
	attractions_location = request.form['game_location']
	vacation_timeline_one = request.form['first_part']
	vacation_timline_one_price = request.form['first_part_price']
	vacation_timeline_two = request.form['second_part']
	vacation_timline_two_price = request.form['second_part_price']
	vacation_timeline_three = request.form['third_part']
	vacation_timline_three_price = request.form['third_part_price']
	vacation_timeline_four = request.form['fourth_part']
	vacation_timline_four_price = request.form['fourth_part_price']

	print('location', trip_location, 'length', 'trip_length', 'start date', trip_start_date, 'end date', trip_end_date, 'num going', 
		num_people, 'purpose_trip', purpose_trip, 'living', living_accomdations, 'place 1', attractions_one, 'place 2', attractions_two, 
		'place 3', attractions_three, 'place 4', attractions_four, 'timeline 1', vacation_timeline_one, 'timeline 2', vacation_timeline_two
		,'timeline 3', vacation_timeline_three, 'timeline 4', vacation_timeline_four, 'price part 1', vacation_timline_one_price, 
		'price part 2', vacation_timline_two_price, 'price part 3', vacation_timline_three_price, 'price part 4', vacation_timline_four_price)

	PATH = "C:\Program Files (x86)\chromedriver.exe"
	driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe") #using chrome browser

	class Planner():

		#@staticmethod
		def date_cleaner_start(self, org_str):
			vacation_timeline_one_split = vacation_timeline_one.split(', ')
			dates_one = vacation_timeline_one_split[1].split(' : ')
			dates_one_start = dates_one[0]
			dates_one_start_two = dates_one_start.split('-')
			dates_one_start_final = dates_one_start_two[2] +"-" + dates_one_start_two[0] +"-" + dates_one_start_two[1]
			return (dates_one_start_final)

		#@staticmethod
		def date_cleaner_end(self, org_str):
			vacation_timeline_one_split = vacation_timeline_one.split(', ')
			dates_one = vacation_timeline_one_split[1].split(' : ')
			dates_one_end = dates_one[1]
			dates_one_end_two = dates_one_end.split('-')
			dates_one_end_final = dates_one_end_two[2] +"-" + dates_one_end_two[0] +"-" + dates_one_end_two[1]
			return (dates_one_end_final)

		#@staticmethod
		def city(self, raw_string):
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

		def hotels_trivago(self, check_in, check_out, num_people_arg):
			#cleaning up data
			start_date_one = check_in			
			end_date_one = check_out
			room_size = Planner.calc_room_size(num_people_arg)
			print("check_in", start_date_one, "check_out", end_date_one, "city", city, "room type", room_size)

			#searching fr now
			url = "https://www.trivago.com/?aDateRange%5Barr%5D={start_date}&aDateRange%5Bdep%5D={end_date}&aPriceRange%5Bfrom%5D=0&aPriceRange%5Bto%5D=0&iRoomType={room_type}&aRooms%5B0%5D%5Badults%5D=2&cpt2=%2F200&hasList=1&hasMap=1&bIsSeoPage=0&sortingId=1&slideoutsPageItemId=&iGeoDistanceLimit=16093&address=&addressGeoCode=&offset=0&ra=&overlayMode="\
			.format(start_date = check_in, \
				end_date = check_out, \
				room_type = num_people_arg )
			driver.get(url);
			time.sleep(100)

			driver.implicitly_wait(5)
			city_type = driver.find_element_by_id("querytext")
			print(city_type, type(city_type))
			city_type.send_keys(city)
			city_type.send_keys(Keys.RETURN)

	planner = Planner()
	check_in_date = planner.date_cleaner_start(vacation_timeline_one)
	check_out_date = planner.date_cleaner_end(vacation_timeline_one)
	city = planner.city(vacation_timeline_one)
	planner.hotels_trivago(check_in_date, check_out_date, city, int(num_people))

