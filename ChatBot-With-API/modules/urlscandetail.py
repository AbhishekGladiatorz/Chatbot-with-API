import requests
from virustotal_api import api
import json

def urlscandetail1(message):
	if api == "XXX":
		print("\033[93m {}\033[00m" .format("*****************************************************"))
		print("\033[93m {}\033[00m" .format("Please fill in the virustotal_api.py for access virustotal api"))
		print("\033[93m {}\033[00m" .format("*****************************************************"))

	else:
		try:

			headers = {
			  "Accept-Encoding": "gzip, deflate",
			  "User-Agent" : "gzip,  My Python requests library example client or username"
			  }
			params = {'apikey': api, 'resource': message ,'allinfo':1 } # message is target url
			response = requests.post('https://www.virustotal.com/vtapi/v2/url/report',
			  params=params, headers=headers)

			json_response = response.json()

			positives = json_response.get("positives")  # detection
			print("\033[93m {}\033[00m".format("positives " + str(positives)))


			total = json_response.get("total")  # total scan
			print("\033[93m {}\033[00m".format("total " + str(total)))


			scan = json_response.get("scans")  # scan data
			for firm in scan:
				a = scan.get(firm)
				detected = str(a.get("detected"))
				if detected == "True":
					print("\033[93m {}\033[00m".format("*************Malicious reportees*************"))
					print("\033[92m {}\033[00m" .format(str(firm)) + " : " + str(a.get("result")))
					print("\033[93m {}\033[00m".format("*************End of Malicious reportees*************"))
				
			scan2 = json_response.get("scans")  # scan data
			for firm in scan2:
				a = scan2.get(firm)
				detected = str(a.get("detected"))
				if detected == "False":
					print("\033[92m {}\033[00m" .format(str(firm)) + " : " + str(a.get("result")))

			scan_id = json_response.get("scan_id")
			print("\033[93m {}\033[00m".format("scan_id " + str(scan_id)))

			resource = json_response.get("resources")
			print("\033[93m {}\033[00m".format("resource " + str(resource)))

			url_given = json_response.get("url")
			print("\033[93m {}\033[00m".format("url_given " + str(url_given)))

			scan_date = json_response.get("scan_date")
			print("\033[93m {}\033[00m".format("scan_date " + str(scan_date)))
			

			permalink = json_response.get("permalink")
			print("\033[93m {}\033[00m".format("permalink " + str(permalink)))
			
			last_seen = json_response.get("last_seen")
			print("\033[93m {}\033[00m".format("last_seen " + str(last_seen)))

			first_seen = json_response.get("first_seen")
			print("\033[93m {}\033[00m".format("first_seen " + str(first_seen)))

			addinfo = json_response.get("additional_info")
			print("\033[93m {}\033[00m".format("resolution :" + addinfo['resolution']))

			addinfo1 = json_response.get("additional_info")
			print("\033[93m {}\033[00m".format("resolution country :" + addinfo1['resolution_country']))

			addinfo2 = json_response.get("additional_info")
			print("\033[93m {}\033[00m".format("Forcepoint ThreatSeeker category :" + addinfo2['Forcepoint ThreatSeeker category']))

			addinfo3 = json_response.get("additional_info")
			print("\033[93m {}\033[00m".format("redirector :" + addinfo3['redirector']))
			
			print("\033[93m {}\033[00m".format("*****************************************************"))
			


		except:
			print("Somethings wrong...")
