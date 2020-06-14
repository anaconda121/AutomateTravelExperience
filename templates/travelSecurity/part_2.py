def trip_planning2():
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

	class Planner():
		def __init__(self):
			self.driver = webdriver.Chrome(PATH) #using chrome browser

		@staticmethod
		def date_cleaner_start(org_str):
			vacation_timeline_one_split = vacation_timeline_one.split(', ')
			dates_one = vacation_timeline_one_split[1].split(' : ')
			dates_one_start = dates_one[0]
			dates_one_start_two = dates_one_start.split('-')
			dates_one_start_final = dates_one_start_two[2] +"-" + dates_one_start_two[0] +"-" + dates_one_start_two[1]
			return (dates_one_start_final)

		@staticmethod
		def date_cleaner_end(org_str):
			vacation_timeline_one_split = vacation_timeline_one.split(', ')
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
				time.sleep(100)
				content = None

				driver.implicitly_wait(5)
				'''
				main = WebDriverWait(driver, 10).until(
	        		city_type = EC.presence_of_element_located((By.ID, "querytext"))
	    		)
				'''
				
				city_type = driver.find_element_by_id("querytext")
				city_type.send_keys("MILAN")
				city_type.send_keys(Keys.RETURN)
				driver.quit()
			elif city == "rome":
				url = "https://www.trivago.com/?aDateRange%5Barr%5D={start_date}&aDateRange%5Bdep%5D={end_date}&aPriceRange%5Bfrom%5D=0&aPriceRange%5Bto%5D=0&iRoomType={room_type}&aRooms%5B0%5D%5Badults%5D=2&cpt2=25084%2F200&hasList=1&hasMap=1&bIsSeoPage=0&sortingId=1&slideoutsPageItemId=&iGeoDistanceLimit=16093&address=&addressGeoCode=&offset=0&ra=&overlayMode="\
				.format(start_date = start_date_one, \
						room_type = room_size, \
						end_date = end_date_one )
				
				search = self.driver.get(url)
				time.sleep(100)
				content = None

				driver.implicitly_wait(5)
				'''
				main = WebDriverWait(driver, 10).until(
	        		city_type = EC.presence_of_element_located((By.ID, "querytext"))
	    		)
				'''
				
				city_type = driver.find_element_by_id("querytext")
				city_type.send_keys("MILAN")
				city_type.send_keys(Keys.RETURN)
				driver.quit()
	planner = Planner()
	planner.hotels_trivago(vacation_timeline_two, int(num_people))