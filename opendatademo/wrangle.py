import csv
import re
from datetime import datetime
import folium

# clone pyzipcode from https://github.com/invernizzi/pyzipcode
# And run `pip install -e` from this repo folder.
# The repo in standard `pip install ...` db does not work with python 3.
from pyzipcode import ZipCodeDatabase
zcdb = ZipCodeDatabase()

map_zipAvg = folium.Map(location=[30.288009, -97.739133])

with open('311data.csv', 'r') as inf:
	data = csv.DictReader(inf)

	# schema: {zip: average time}
	avg_zipcode_times = {}
	for row in data:
		lat = lon = None
		try:
			# lat = float(row['Latitude Coordinate'])
			# lon = float(row['Longitude Coordinate'])
			zipc = row['Zip Code']
			
			# extract date_changed
			# TODO: demo looking at python datetime module
			# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
			temp = row['Status Change Date']
			date_changed = datetime.strptime(row['Status Change Date'], \
											'%m/%d/%Y %I:%M:%S %p')
			# print(date_changed)

			# extract date_created
			date_created = datetime.strptime(row['Created Date'], \
											'%m/%d/%Y %I:%M:%S %p')

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

	for zipc, avg in avg_zipcode_times.items():
		if not zipc:
			continue # zipc can be an empty string

		latlong = zcdb[int(zipc)]
		folium.Marker([latlong.latitude, latlong.longitude], popup=str(avg)).add_to(map_zipAvg)
		print(zipc, avg)

map_zipAvg.save('zipPlot.html')