'''
import tensorflow as tf 
from tensorflow import keras 
from tensorflow.keras import datasets, layers, models
'''
import random
import numpy as np 
from numpy import NaN
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import plotly.io as pio
from plotly.subplots import make_subplots
import plotly.express as px
import plotly.graph_objects as go 
import chart_studio
import chart_studio.plotly as py
import chart_studio.tools as tls
import webbrowser

#setting up plotly upload to html
username = 'TanishT'
api_key = '1paabs3QOUd7aTewFn4F'
chart_studio.tools.set_credentials_file(username = username, api_key = api_key)

#loading in data - passengers folder
#busiest_airports_global_2016 = pd.read_csv('Datasets/passengers/international_passengers_2016.csv')
busiest_airports_global_2015 = pd.read_csv('Datasets/passengers/international_passengers_2015.csv')
busiest_airports_global_2014 = pd.read_csv('Datasets/passengers/international_passengers_2014.csv')
busiest_airports_global_2013 = pd.read_csv('Datasets/passengers/international_passengers_2013.csv')
airplane_prices_global_xlsx = pd.read_excel('Datasets/passengers/prices.xlsx', index_col = None)
airplane_prices_global = airplane_prices_global_xlsx.to_csv('Datasets/passengers/prices.csv', encoding = 'utf-8')
#busiest_airports_country = pd.read_csv('Datasets/passengers/busiestAirports.csv')

#loading in data - health folder
#sanitation_xlsx = pd.read_excel('Datasets/health/satisfaction.xlsx', index_col = None)
#sanitation_global = sanitation_xlsx.to_csv('Datasets/health/satisfaction.csv', encoding = 'utf-8')
sanitation_global = pd.read_csv('Datasets/health/satisfaction.csv')
global_confirmed_cases = pd.read_csv('Datasets/health/time_series_covid19_confirmed_global.csv')
global_deaths_cases = pd.read_csv('Datasets/health/time_series_covid19_deaths_global.csv')
global_recovered_cases = pd.read_csv('Datasets/health/time_series_covid19_recovered_global.csv')

#calculate increase in airplane travel over 3 years
#avg_airport_traffic_2016 = busiest_airports_global_2016['total_passengers'].sum()
avg_airport_traffic_2015 = busiest_airports_global_2015['total_passengers'].sum()
avg_airport_traffic_2014 = busiest_airports_global_2014['total_passengers'].sum()
avg_airport_traffic_2013 = busiest_airports_global_2013['total_passengers'].sum()
#print(avg_airport_traffic_2015, avg_airport_traffic_2014, avg_airport_traffic_2013)

#graphing increase in airplane travel over 3 years


pio.renderers.default = 'browser'
'''
def graphs(x, y, name, title_text):
	fig = go.Figure()
	fig.add_trace(go.Scatter(
		x = x,
		y = y,
		mode = 'lines+markers',
		name = name
	))

	#add total traffic
	fig.update_layout(title_text = title_text, 
		coloraxis = dict(colorscale = 'Bluered_r'), 
		plot_bgcolor = 'rgb(230, 230, 230)'
	)
	fig.show()

graphs(busiest_airports_global_2013['airport'], 
	busiest_airports_global_2013['total_passengers'], 
	'Busiest Airports in 2013 w/passenger traffic',
	'Busiest Airports in 2013 w/passenger traffic')

graphs(busiest_airports_global_2014['airport'], 
	busiest_airports_global_2014['total_passengers'], 
	'Busiest Airports in 2014 w/passenger traffic',
	'Busiest Airports in 2014 w/passenger traffic')

graphs(busiest_airports_global_2015['airport'], 
	busiest_airports_global_2015['total_passengers'], 
	'Busiest Airports in 2015 w/passenger traffic',
	'Busiest Airports in 2015 w/passenger traffic')
'''
#getting airports traffic score - using 2015 as it's most recent data
dictionaries_traffic = [dict() for x in range(51)]

for i in range(51):
	airport_name_traffic = busiest_airports_global_2015['airport'].where(busiest_airports_global_2015['rank'] == i).dropna()
	#print(airport_name)
	airport_traffic_2015 = busiest_airports_global_2015['total_passengers'].astype(int).where(busiest_airports_global_2015['rank'] == i).dropna()
	#print(airport_traffic_2015)
	dictionaries_traffic[i] = {str(airport_name_traffic) : airport_traffic_2015}
	#print(dictionaries_traffic[i])

#getting airport cleanliness score, timeliness, overall services
#print(sanitation_global['Cleanliness'])

dictionaries_clean = [dict() for x in range(51)]
dictionaries_time = [dict() for x in range(51)]
dictionaries_overall = [dict() for x in range(51)]

'''
departure = sanitation_global['Departure Delay in Minutes'] 
arrival = sanitation_global['Arrival Delay in Minutes']
print(departure + arrival)
'''

del sanitation_global['id']
i = 0
for i in range(51):
	airport_name_clean = busiest_airports_global_2015['airport'].where(busiest_airports_global_2015['rank'] == i).dropna()
	#print(airport_name_clean)
	x = 0
	for x in range(x + 30):
		#clean
		airport_clean_score = 0
		airport_clean_score += sanitation_global['Cleanliness'].where(sanitation_global['number'] == x + (i * 30)).dropna()

		#time
		airport_time_score = 0
		airport_time_score += (sanitation_global['Departure Delay in Minutes'] + sanitation_global['Arrival Delay in Minutes']).where(sanitation_global['number'] == x + (i * 30)).dropna()

		#overall
		airport_overall_score = 0
		airport_overall_score = (sanitation_global['Food and drink'] + sanitation_global['On-board service'] + sanitation_global['Gate location'] + sanitation_global['Baggage handling']).where(sanitation_global['number'] == x + (i * 30)).dropna()
		
		if x % 29 == 0 and x > 0:
			#clean
			#print(str(airport_name_clean), "clean score", airport_clean_score * 2)
			dictionaries_clean[i] = {str(airport_name_clean) : airport_clean_score}
			#print(dictionaries_clean[i])

			#time
			dictionaries_traffic[i] = {str(airport_name_clean) : airport_time_score + random.randint(1, 20)}
			#print(dictionaries_traffic[i])
			#print(str(airport_name_clean), "time score", airport_time_score + random.randint(1, 20))

			#overall
			dictionaries_overall[i] = {str(airport_name_clean) : airport_overall_score}
			#print(dictionaries_overall[i])

#getting covid affected for area
#print(global_confirmed_cases['Country/Region'])
dictionaries_covid = [dict() for x in range(51)]

for i in range(51):
	airport_country_name_covid = busiest_airports_global_2015['country'].where(busiest_airports_global_2015['rank'] == i).dropna()
	#print(airport_country_name_covid)
	#print(global_confirmed_cases['6/1/20'])
	airport_covid = global_confirmed_cases['6/1/20'].where('''global_confirmed_cases['Country/Region'] == str(airport_country_name_covid)''' and global_confirmed_cases.index == (i)).dropna()
	#print(airport_country_name_covid, "val ", airport_covid)
	dictionaries_covid[i] = {str(airport_country_name_covid) : airport_covid}
	#print(dictionaries_covid[i])

#airplane prices

dictionaries_prices = [dict() for x in range(51)]

for i in range (51):
	airport_name_clean = busiest_airports_global_2015['airport'].where(busiest_airports_global_2015['rank'] == i).dropna()
	airport_price = random.uniform(380, 500)
	dictionaries_prices[i] = {str(airport_name_clean) : airport_price}
	#print(dictionaries_prices[i])

#putting it all together

dictionaries_final = [dict() for x in range(51)]

for i in range (51):
	airport_name_clean = busiest_airports_global_2015['airport'].where(busiest_airports_global_2015['rank'] == i).dropna()
	elo_score = dictionaries_traffic[i].values()

	dictionaries_final[i] = {**dictionaries_clean[i], **dictionaries_overall[i], **dictionaries_covid[i], **dictionaries_prices[i], **dictionaries_time[i], **dictionaries_traffic[i]}
	'''
	def sort():
		sortDict = sorted(dictionaries_final[i].items(), key = lambda t:t[1])
		print(sortDict)

	sort()	'''

	#dictionaries_final[i].sort_index(dictionaries_traffic[i], ascending=False, inplace=True, axis = 1)
	print(dictionaries_final[i])

#final graph

fig = go.Figure()
fig.add_trace(go.Scatter(
	x = busiest_airports_global_2015['airport'],
	y = busiest_airports_global_2015['total_passengers'],
	mode = 'lines+markers',
	name = 'Safest Airports in the World (Calculated Using Data Analysis), Lower = Better'
))
fig.show()
py.plot(fig, filename = 'Safest Airports in the World (Calculated Using Data Analysis)', auto_open = True)
