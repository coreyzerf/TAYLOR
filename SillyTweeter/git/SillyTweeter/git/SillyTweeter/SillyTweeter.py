#!/usr/bin/env python
import sys
from twython import Twython
CONSUMER_KEY = 'u23rwH4IdLqZ1V7rGigrMA'
CONSUMER_SECRET = 'KpmFN6cQcZqvzK10rhHjVIJZMM31Vm1aRDl6hFo38Q'
ACCESS_KEY = '2393551369-KG8tx9DTI3j8XG10eSdsTjC7srzr5ScHhpryH2o'
ACCESS_SECRET = '26lrduosBYj9vTteWL2iIzAUjcSRJxcq0PR91aq2EiNOj'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 

api.update_status(status=sys.argv[1])
