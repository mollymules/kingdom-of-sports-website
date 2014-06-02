from google.appengine.ext import ndb

class SeniorLeaderBoard(ndb.Model):
	name = ndb.StringProperty(required=True)
	email = ndb.StringProperty(required=True)
	date = ndb.DateProperty()
	score = ndb.IntegerProperty()