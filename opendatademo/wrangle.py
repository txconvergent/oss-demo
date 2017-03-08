import csv
import re
import json
import requests
from datetime import datetime
import folium

# clone pyzipcode from https://github.com/invernizzi/pyzipcode
# And run `pip install -e` from this repo folder.
# The repo in standard `pip install ...` db does not work with python 3.
# If you are running Python 2, just run `pip install pyzipcode`.

APP_TOKEN = 'HnqXaIwPkD3s0YQQBY4w0Rcez'
url = "https://data.austintexas.gov/resource/5h38-fd8d.json?$$app_token=%s" % APP_TOKEN
#url = "https://data.austintexas.gov/resource/5h38-fd8d.json"

response = requests.get(url)
if response.status_code == 200:
    data = response.json() 
else:
	print response.status_code

from pyzipcode import ZipCodeDatabase
zcdb = ZipCodeDatabase()

map_zipAvg = folium.Map(location=[30.288009, -97.739133]) # location in center of UT

# schema: {zip: average time}
incident_count = 0
avg_zipcode_times = {}
for incident in data:
	incident_count =  incident_count + 1
	lat = lon = None	
	try:
		zipc = incident.get("sr_location_zip_code", "Null")
		if not zipc:
			continue
		else:
			zipc = int(zipc)
		
		# extract date_changed
		# TODO: demo looking at python datetime module
		# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
		date_changed = datetime.strptime(incident.get("sr_status_date"), \
										'%Y-%m-%dT%H:%M:%S.%f')

		# extract date_created
		date_created = datetime.strptime(incident.get("sr_created_date"), \
										'%Y-%m-%dT%H:%M:%S.%f')

		# TODO: lookup datetime subtract
		# https://docs.python.org/3/library/datetime.html#timedelta-objects
		# Sanity check for total_seconds() method
		response_time = (date_changed - date_created).total_seconds()

		if zipc in avg_zipcode_times:
			avg_zipcode_times[zipc] = (avg_zipcode_times[zipc] + response_time) / 2
		else:
			avg_zipcode_times[zipc] = response_time

	except Exception as e:
		print(e)
print('Number of entries:%d' % incident_count)
print('Creating map... showing avg per zip code')
for zipc, avg in avg_zipcode_times.items():
	latlong = zcdb[zipc]
	folium.Marker([latlong.latitude, latlong.longitude], popup=str(avg)).add_to(map_zipAvg)
	print(zipc, avg)

print('Saving to html map...')
map_zipAvg.save('zipPlot.html')