from google.appengine.ext import ndb

class BookingRequest(ndb.Model):
    email = ndb.StringProperty()
    name = ndb.StringProperty()
    phoneNumber = ndb.StringProperty()
    message = ndb.StringProperty()
    dateEnquiryMade = ndb.DateProperty()
    dateRequested = ndb.DateProperty()