#!/usr/bin/env python
import sys
import subprocess
from twython import TwythonStreamer
from twython import Twython

class TStream(TwythonStreamer):
		
	def on_success(self, data):
		CONSUMER_KEY = 'u23rwH4IdLqZ1V7rGigrMA'
		CONSUMER_SECRET = 'KpmFN6cQcZqvzK10rhHjVIJZMM31Vm1aRDl6hFo38Q'
		ACCESS_KEY = '2393551369-KG8tx9DTI3j8XG10eSdsTjC7srzr5ScHhpryH2o'
		ACCESS_SECRET = '26lrduosBYj9vTteWL2iIzAUjcSRJxcq0PR91aq2EiNOj'
		api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
		
		if 'text' in data:
			text = data['text'].encode('utf-8')
			user = data['user']['screen_name']
			print user + " said:"
			print text
			test = text.find("RPiTAYLOR Hello")
			kill = text.find("RPiTAYLOR command: kill")
			if test > 0:
				print "Somebody loves me!"
				try:
					api.update_status(status="@" + user + " Hi!")
				except Exception:
					print "Error sending"
			elif kill > 0 and user == 'coreyzerf':
				subprocess.call(['./shutdown.sh'])
				self.disconnect()
			
	def on_error(self, status_code, data):
		print status_code

        # Want to stop trying to get data because of the error?
        # Uncomment the next line!
        # self.disconnect()
		
CONSUMER_KEY = 'u23rwH4IdLqZ1V7rGigrMA'
CONSUMER_SECRET = 'KpmFN6cQcZqvzK10rhHjVIJZMM31Vm1aRDl6hFo38Q'
ACCESS_KEY = '2393551369-KG8tx9DTI3j8XG10eSdsTjC7srzr5ScHhpryH2o'
ACCESS_SECRET = '26lrduosBYj9vTteWL2iIzAUjcSRJxcq0PR91aq2EiNOj'

stream = TStream(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
stream.user(track="coreyzerf")