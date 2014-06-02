from google.appengine.ext import ndb

class Newsletter(ndb.Model):
    email = ndb.StringProperty()
    date = ndb.DateProperty()
    subscribed = ndb.BooleanProperty(default=False)
