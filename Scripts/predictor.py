import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
#plotly =  advanced version of seaborn and matplotlib
import plotly.io as pio
from plotly.subplots import make_subplots
import plotly.express as px
import plotly.graph_objects as go 
#folium - helps populate maps
import folium
from folium import plugins
import warnings
#prophet - forecasting software
from fbprophet import Prophet
#chart studio - integrating graphs into html
import chart_studio
import chart_studio.plotly as py
import chart_studio.tools as tls

username = 'TanishT'
api_key = 'T6LVJjGuUuHF00psTBcF'
chart_studio.tools.set_credentials_file(username = username, api_key = api_key)

#config plot 
plt.rcParams['figure.figsize'] = 10, 12

#disabling warnings
warnings.filterwarnings('ignore')

#reading in datasets
df = pd.read_excel('ContentPredict/Covid cases in India.xlsx')
df_india = df.copy()

#indian states coordinates
india_coord = pd.read_excel('ContentPredict/Indian Coordinates.xlsx')

#day by day info
dbd_india = pd.read_excel('ContentPredict/per_day_cases.xlsx', parse_dates = True, sheet_name = 'India')
dbd_italy = pd.read_excel('ContentPredict/per_day_cases.xlsx', parse_dates = True, sheet_name = 'Italy')
dbd_korea = pd.read_excel('ContentPredict/per_day_cases.xlsx', parse_dates = True, sheet_name = 'Korea')
dbd_wuhan = pd.read_excel('ContentPredict/per_day_cases.xlsx', parse_dates = True, sheet_name = 'Wuhan')

#get total number of confirmed bases in India up to a certain date
df.drop(['S. No.'], axis = 1, inplace = True) #filtering out columns we don't need
df['Total cases'] = df['Total Confirmed cases (Indian National)'] + df['Total Confirmed cases ( Foreign National )']
total_cases = df['Total cases'].sum() 
print('Total Number of Confirmed COVID-19 Cases all across India up to 3/22/2020: ', total_cases)

df.style.background_gradient(cmap = 'Reds') #color codes numbers in all rows, dark shade of red = more severe fatalities

#get total number of active cases 
df['Total active'] = df['Total cases'] - (df['Death'] + df['Cured'])
total_active = df['Total active'].sum()
print('Total Number of Active Cases all across India up to 3/22/2020: ', total_active) 

#sorting cases in order from most to least
sort_total_active = df.groupby('Name of State / UT')['Total active'].sum().sort_values(ascending = False).to_frame()
sort_total_active = df.style.background_gradient(cmap = 'Reds')

#use follium to create zoomable map 
df_full = pd.merge(india_coord,df,on='Name of State / UT')
map = folium.Map(location=[20, 70], zoom_start=4,tiles='Stamenterrain')
for lat, lon, value, name in zip(df_full['Latitude'], df_full['Longitude'], df_full['Total cases'], df_full['Name of State / UT']):
	folium.CircleMarker([lat, lon], radius=value*0.8, popup = ('<strong>State</strong>: ' + 
		str(name).capitalize() + '<br>''<strong>Total Cases</strong>: ' + str(value) + '<br>'),
		color='red',fill_color='red',fill_opacity=0.3 ).add_to(map)
print(map)

#graphs for confirmed, recovered, deaths
f, ax = plt.subplots(figsize=(12, 8))
data = df_full[['Name of State / UT','Total cases','Cured','Death']]
data.sort_values('Total cases',ascending=False,inplace=True)
sns.set_color_codes("muted") #gives color in darker shade
sns.barplot(x="Total cases", y="Name of State / UT", data=data,label="Total", color="r")
sns.barplot(x="Cured", y="Name of State / UT", data=data, label="Cured", color="g")
sns.barplot(x="Death", y="Name of State / UT", data=data, label="Death", color="b")

ax.legend(ncol=2, loc="lower right", frameon=True)
ax.set(xlim=(0, 120), ylabel="State",xlabel="Cases")
sns.despine(left=True, bottom=True)
plt.show()

#creating daily graphs of COVID-cases using Plotly
pio.renderers.default = 'browser'

#rise of cases daily
fig = go.Figure()
fig.add_trace(go.Scatter(
	x = dbd_india['Date'], 
	y = dbd_india['Total Cases'], 
	mode = 'lines+markers', 
	name = 'Total cases')
)
fig.update_layout(title_text = 'Trend of Coronavirus cases in India (Cumulative Cases)', plot_bgcolor = 'rgb(230, 230, 230)', )
fig.show()

#py.plot(fig, filename = 'Trend of Coronavirus cases in India (Cumulative Cases)', auto_open = True)

#bar graph
fig2 = px.bar(dbd_india, x = "Date", y = "New Cases", barmode = "group", height = 400)
fig2.update_layout(title_text = "Corona Cases day-by-day in India", plot_bgcolor = 'rgb(230,230, 230)')
fig2.show()

py.plot(fig2, filename = 'Corona Cases day-by-day in India', auto_open = True, width = 450, height = 1600)

"""
#graph comparing Italy, South Korea, Wuhan
def barGraph(count, title):
	fig = px.bar(count, x = "Date", y = 'Total Cases', color = 'Total Cases', orientation = 'v', height = 600, title = title, color_discrete_sequence = px.colors.cyclical.IceFire)
	fig.update_layout(plot_bgcolor = 'rgb(230, 230, 230)')
	fig.show()

barGraph(dbd_india, 'Confirmed Cases in India')
barGraph(dbd_italy, 'Confirmed Cases in Italy')
barGraph(dbd_korea, 'Confirmed Cases in Korea')
barGraph(dbd_wuhan, 'Confirmed Cases in Wuhan')  
"""

#above graph on one plot, wuhan info has been poorly recorded so it will not be used for the following 2 segments
fig = make_subplots(
	#graph params
	rows = 2, cols = 2,
	specs = [[{}, {}], [{'colspan': 2}, None]],
	subplot_titles = ('S. Korea', 'Italy', 'India', 'Wuhan')
)

#getting graph info
fig.add_trace(go.Bar(x=dbd_india['Date'], y=dbd_india['Total Cases'],marker=dict(color=dbd_india['Total Cases'], coloraxis="coloraxis")),1, 1)
fig.add_trace(go.Bar(x=dbd_italy['Date'], y=dbd_italy['Total Cases'],marker=dict(color=dbd_italy['Total Cases'] ,coloraxis="coloraxis")),1, 2)
fig.add_trace(go.Bar(x=dbd_korea['Date'], y=dbd_korea['Total Cases'],marker=dict(color=dbd_korea['Total Cases'], coloraxis="coloraxis")),2, 1)
#fig.add_trace(go.Bar(x=dbd_wuhan['Date'], y=dbd_wuhan['Total Cases'],marker=dict(color=dbd_wuhan['Total Cases'], coloraxis="coloraxis")),2, 2)

fig.update_layout(coloraxis = dict(colorscale = 'Bluered_r'), showlegend = False, 
	title_text = 'Total Confirmed Cases For India, Italy, S.Korea areas(Cumulative) up to 3/22/2020', 
	plot_bgcolor = 'rgb(230, 230, 230)')

fig.show()
#py.plot(fig, filename = 'Total Confirmed Cases For India, Italy, S.Korea areas(Cumulative) up to 3/22/2020', auto_open = True)




#trend after country reaching 100 cases - Wuhan's data is poorly recorded b/c outbreak happened very quickly
#getting info and setting style
title = 'Trend after Reaching 100 cases'
labels = ['S. Korea', 'Italy', 'India']
colors = ['rgb(122, 128, 0)', 'rgb(255, 0, 0)', 'rgb(49, 130, 189)']

mode_size = [10, 10, 12]
line_size = [1, 1, 8]

fig = go.Figure()
def after100(locationX, locationY, labelIndex, colorIndex, lineIndex):
	fig.add_trace(go.Scatter(x = locationX,
							y = locationY, mode = 'lines', #mode determines graph drawing type
							name = labelIndex,
							line  = dict(color = colorIndex, width = lineIndex),
							connectgaps = True)) #connect gaps cleans up missing data values

after100(dbd_korea['Days after surpassing 100 cases'], dbd_korea['Total Cases'], labels[0], colors[0], line_size[0])
after100(dbd_italy['Days after surpassing 100 cases'], dbd_italy['Total Cases'], labels[1], colors[1], line_size[1])
after100(dbd_india['Days after surpassing 100 cases'], dbd_india['Total Cases'], labels[2], colors[2], line_size[2])

#styling graph in depth
annotations = []

annotations.append(dict(xref='paper',
						yref='paper', 
						x=0.5, y=-0.1, 
						xanchor='center', yanchor='top', 
						text='Days after crossing 100 cases ', 
						font=dict(family='Arial', size=12, color='rgb(150,150,150)'), showarrow=False))

fig.update_layout(annotations=annotations,plot_bgcolor='white', yaxis_title='Cumulative cases')
fig.show()
#py.plot(fig, filename = 'Days after surpassing 100 cases (Cumulative Cases)', auto_open = False)


#exploring world wide data
df = pd.read_csv('ContentPredict/covid_19_clean_complete.csv', parse_dates = ['Date'])
df.rename(columns = {'ObservationDate': 'Date', 'Country/Region': 'Country'}, inplace = True)

df_confirmed = pd.read_csv('ContentPredict/time_series_covid19_confirmed_global.csv')
df_recovered = pd.read_csv('ContentPredict/time_series_covid19_recovered_global.csv')
df_deaths = pd.read_csv('ContentPredict/time_series_covid19_deaths_global.csv')

df_confirmed.rename(columns = {'Country/Region': 'Country'}, inplace = True)
df_recovered.rename(columns = {'Country/Region': 'Country'}, inplace = True)
df_deaths.rename(columns = {'Country/Region': 'Country'}, inplace = True)

#df_deaths.head()

df2 = df.groupby(["Date", "Country", "Province/State"])[['Date', 'Province/State', 'Country', 'Confirmed', 'Deaths', 'Recovered']].sum().reset_index()
df2.head()

#check for India Data
df.query('Country == "India"').groupby('Date')[['Confirmed', 'Deaths', 'Recovered']].sum().reset_index()

#overall stats
df.groupby('Date').sum().head()

#graph for all covid cases
#reset values for fresh input
confirmed = df.groupby('Date').sum()['Confirmed'].reset_index()
deaths = df.groupby('Date').sum()['Deaths'].reset_index()
recovered = df.groupby('Date').sum()['Recovered'].reset_index()

#graph
fig = go.Figure()

fig.add_trace(go.Scatter(x=confirmed['Date'], y=confirmed['Confirmed'], mode='lines+markers', name='Confirmed',line=dict(color='blue', width=2)))
fig.add_trace(go.Scatter(x=deaths['Date'], y=deaths['Deaths'], mode='lines+markers', name='Deaths', line=dict(color='Red', width=2)))
fig.add_trace(go.Scatter(x=recovered['Date'], y=recovered['Recovered'], mode='lines+markers', name='Recovered', line=dict(color='Green', width=2)))
fig.update_layout(title='Worldwide COVID-19 Cases', xaxis_tickfont_size=14,yaxis=dict(title='Number of Cases'))
fig.show()

#forecasting and predictions - Prophet
confirmed = df.groupby('Date').sum()['Confirmed'].reset_index()
deaths = df.groupby('Date').sum()['Deaths'].reset_index()
recovered = df.groupby('Date').sum()['Recovered'].reset_index()

#inputting info into prophet

"""
The input to Prophet is always a dataframe with two columns: **ds** and **y**. The **ds (datestamp)** column should be of a format expected by Pandas, 
ideally YYYY-MM-DD for a date or YYYY-MM-DD HH:MM:SS for a timestamp. The y column must be numeric, and represents the measurement we wish to forecast
"""

confirmed.columns = ['ds', 'y'] #ds = date, y = mi,ner comfirmed worldwide
confirmed['ds'] = pd.to_datetime(confirmed['ds']) #converting vals of ds colimn into ideal format

#generating forecast of a week ahead for confirmed cases

#generating future dates
m = Prophet(interval_width = 0.95) #interval_width  = 0.95 means where are 95% sure that our algorithm will work
m.fit(confirmed)
future = m.make_future_dataframe(periods = 7)

#getting prediction values
forecast = m.predict(future)
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']] .tail()) #predict method assigns each row value named yhat. the info we are getting are date, and range from yhat_lower to y_hat upper

#plotting forecast
corfirmed_forecast_plot = m.plot(forecast)
confirmed_forcecast_plot = m.plot_components(forecast)
print(confirmed_forcecast_plot)

#generating forecast of a week ahead with deaths

deaths.columns = ['ds', 'y'] #ds = date, y = mi,ner comfirmed worldwide
deaths['ds'] = pd.to_datetime(deaths['ds']) #converting vals of ds colimn into ideal format

m = Prophet(interval_width = 0.95) #interval_width  = 0.95 means where are 95% sure that our algorithm will work
m.fit(deaths)
futureDeaths = m.make_future_dataframe(periods = 7)

forecast = m.predict(futureDeaths)
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']] .tail()) 

deaths_forecast_plot = m.plot(forecast)
deaths_forcecast_plot = m.plot_components(forecast)

#generating week ahead results with recoveries
recovered.columns = ['ds', 'y'] #ds = date, y = mi,ner comfirmed worldwide
recovered['ds'] = pd.to_datetime(recovered['ds']) #converting vals of ds colimn into ideal format

m = Prophet(interval_width = 0.95) #interval_width  = 0.95 means where are 95% sure that our algorithm will work
m.fit(recovered)
futureRecovered = m.make_future_dataframe(periods = 7)

forecast = m.predict(futureRecovered)
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']] .tail()) 

recovered_forecast_plot = m.plot(forecast)
recovered_forcecast_plot = m.plot_components(forecast)