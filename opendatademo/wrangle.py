import csv
import re
from datetime import datetime

with open('311data.csv', 'r') as inf:
	data = csv.DictReader(inf)

	for row in data:
		lat = lon = None
		try:
			lat = float(row['Latitude Coordinate'])
			lon = float(row['Longitude Coordinate'])
			
			# extract date_changed
			# TODO: demo looking at python datetime module
			# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
			temp = row['Status Change Date']
			date_changed = datetime.strptime(row['Status Change Date'], \
											'%m/%d/%Y %I:%M:%S %p')
			print(date_changed)

			# extract date_created
			date_created = datetime.strptime(row['Created Date'], \
											'%m/%d/%Y %I:%M:%S %p')

			print(lat, lon, date_created, date_changed)
			
		except Exception as e:
			print(e)