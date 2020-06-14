#14.35 mins into tutorial
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



#creating daily graphs of COVID-cases using Plotly
pio.renderers.default = 'browser'


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

