# fast2sms
# API URI http://api.fast2sms.com/sms.php?token=&mob=&mess=&sender=FSTSMS&route=0
# By Chayan Naskar

import urllib
import json

def sendSms(token):
	number = raw_input("Enter mobile number : ")
	msg = raw_input("Enter the message : ")
	url = "http://api.fast2sms.com/sms.php?token=" + token + "&mob=" + number + "&mess=" + msg + "&sender=FSTSMS&route=0"
	print url
	send_sms = urllib.urlopen(url).read()
	jsonData = json.loads(send_sms)
	if(jsonData["status"] == "accept"):
		print "Last SMS Cost ", jsonData["cost"]
		print "Remaining Balance ", jsonData["balance"]
	else:
		print "Error Sending SMS : ", jsonData['error_message']


token = raw_input("Please enter Token : ")
sendSms(token)