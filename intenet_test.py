import time
import os, requests
from datetime import datetime as dt

url = "https://google.com"
timeout = 5 # second
minutes = 0
report_interval = 3 # minutes
int_down = False
downtime_start_at = ""
downtime_stop_at = ""
downtime_minutes = 0
file_name = "internet-downtime-details.csv"

print("+++=== START ===+++\n")

while True:
	now=dt.now()
	time_now = now.strftime("%H:%M:%S")
	starttime = time.time()
	
	try:
		request = requests.get(url, timeout=timeout)
		if int_down == True:
			downtime_stop_at = time_now
			print(f"{downtime_stop_at} - Up after {downtime_minutes}min(s)")
			downtime_minutes = 0
			int_down = False
		
		
	except (requests.ConnectionError, requests.Timeout) as exception:
		if int_down == False:
			downtime_start_at = time_now
			print(f"{downtime_start_at} - Downtime started")
			int_down = True
		print(f"{time_now} - No internet connection for {downtime_minutes}")
		
		downtime_minutes+=1
	if minutes % report_interval == 0:
		if int_down == True:
			print(f"{time_now} - Working - No Internet - Runtime: {minutes}min")
		else:
			print(f"{time_now} - Working - Internet Working - Runtime: {minutes}min")
	#finally:
	#	print("DONE")
	time.sleep(60.0 - ((time.time() - starttime) % 60.0))
	minutes+=1