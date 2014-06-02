from google.appengine.ext import ndb

class WomenLeaderBoard(ndb.Model):
    name = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    date = ndb.DateProperty()
    score = ndb.IntegerProperty()