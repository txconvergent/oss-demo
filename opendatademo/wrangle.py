import csv
import re
from datetime import datetime

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

			prev_time = avg_zipcode_times[zipc]
			avg_zipcode_times = (prev_time + response_time) / 2
			
		except Exception as e:
			print(e)