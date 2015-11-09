import webapp2
import datetime
import cgi
import os
import re
import json

from kosdatastore.Newsletter import Newsletter
from kosdatastore.BookingRequest import BookingRequest
from kosdatastore.SeniorLeaderBoard import SeniorLeaderBoard
from kosdatastore.WomenLeaderBoard import WomenLeaderBoard
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import mail
from google.appengine.ext import ndb
from datetime import datetime


class MainPage(webapp2.RequestHandler):    
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'Home.html')
        self.response.out.write(template.render(path, {}))

class Activities(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'Activities.html')
        self.response.out.write(template.render(path, {}))
        

class Sports(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'Sports.html')
        self.response.out.write(template.render(path, {}))
       
class BookNow(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'BookNow.html')
        self.response.out.write(template.render(path, {}))
        
    
    def post(self):
        print self.request;
        nameGiven = cgi.escape(self.request.get('name'))
        emailAddress =self.request.get('email')
        phone = self.request.get('phone')
        messageSent = self.request.get('message')
        date = datetime.strptime(self.request.get('date'), '%d-%m-%Y')  
        sender = "info@kingdomofsports.ie"
        subject = "Booking enquiry from: %s"%(nameGiven)
        body = "This enquiry is from %s and their number is %s. Here is the message %s. This is the preferred date %s."%(emailAddress,phone,messageSent,date)
        mail.send_mail(sender, sender, subject, body)
        newRequest = BookingRequest(email = emailAddress, dateEnquiryMade = datetime.now(), message = messageSent, phoneNumber = phone, dateRequested = date, name = nameGiven)
        newRequest.put() 
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), 'BookNow.html')
        self.response.out.write(template.render(path, template_values))

        
class Contact(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), 'Contact.html')
        self.response.out.write(template.render(path, template_values))
        
class Gallery(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), 'Gallery.html')
        self.response.out.write(template.render(path, template_values))
        
class Membership(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), 'Membership.html')
        self.response.out.write(template.render(path, template_values))
        
class Packages(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), 'Packages.html')
        self.response.out.write(template.render(path, template_values))
        
class Pricing(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), 'Pricing.html')
        self.response.out.write(template.render(path, template_values))
        
class Tournaments(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), 'Tournaments.html')
        self.response.out.write(template.render(path, template_values))

class Testimonials(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), 'Testimonials.html')
        self.response.out.write(template.render(path, template_values))
        
class FAQ(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), 'FAQ.html')
        self.response.out.write(template.render(path, template_values))

class Leaderboards(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), 'Leaderboard.html')
        self.response.out.write(template.render(path, template_values))

class GetMenLeaderBoard(webapp2.RequestHandler):
    def get(self):
        leaderboard_result = []
        dbLeaderboard = SeniorLeaderBoard.query().order(-SeniorLeaderBoard.score).fetch(10)
        boardPosition = 1
        for leaderBoard in dbLeaderboard:
            leaderboard_result.append({ "position": boardPosition, "name": leaderBoard.name, "score": leaderBoard.score })
            boardPosition = boardPosition +1
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(leaderboard_result, indent=4)) 

class GetWomenLeaderBoard(webapp2.RequestHandler):
    def get(self):
        leaderboard_result = []
        dbLeaderboard = WomenLeaderBoard.query().order(-WomenLeaderBoard.score).fetch(10)
        boardPosition = 1
        for leaderBoard in dbLeaderboard:
            leaderboard_result.append({ "position": boardPosition, "name": leaderBoard.name, "score": leaderBoard.score })
            boardPosition = boardPosition +1
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(leaderboard_result, indent=4)) 

        
class NewsletterSignUp(webapp2.RequestHandler):
    def post(self):
        emailAddress = self.request.get('email')
        if not re.match(r"[^@]+@[^@]+\.[^@]+", emailAddress):
            template_values = {'message': 'Not a valid email address. Please try again.'}
        else:    
            isSignedUp = Newsletter.query(Newsletter.email == emailAddress).get()
            if isSignedUp is None:
                newSignUp = Newsletter(email = emailAddress, date = datetime.now(), subscribed = True)
                newSignUp.put() 
                template_values = {'message': 'Thanks for signing up!'}
            else:      
                template_values = {'message': 'You have previously signed up. But thanks for trying again.'}
        path = os.path.join(os.path.dirname(__file__), 'Pricing.html')
        self.response.out.write(template.render(path, template_values))
         
class SiteMap(webapp2.RequestHandler):    
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), 'SiteMap.html')
        self.response.out.write(template.render(path, template_values))

class DownloadInvitaton(webapp2.RequestHandler):    
    def get(self):
        csv = List2CSV(testvalues)
        self.response.headers['Content-Type'] = 'text/pdf'
        self.response.headers['Content-Disposition'] = 'attachment; filename=invitation.pdf'
        self.response.out.write(csv)
        
class DownloadHours(webapp2.RequestHandler):    
    def get(self):
        csv = List2CSV(testvalues)
        self.response.headers['Content-Type'] = 'text/pdf'
        self.response.headers['Content-Disposition'] = 'attachment; filename=christmas.pdf'
        self.response.out.write(csv)
        
class DownloadSchools(webapp2.RequestHandler):    
    def get(self):
        csv = List2CSV(testvalues)
        self.response.headers['Content-Type'] = 'text/pdf'
        self.response.headers['Content-Disposition'] = 'attachment; filename=schools.pdf'
        self.response.out.write(csv)  
        
             
app = webapp2.WSGIApplication([('/', MainPage),
                                      ('/Activities', Activities),
                                      ('/Sports', Sports),
                                      ('/BookNow', BookNow),
                                      ('/Contact', Contact),
                                      ('/Gallery', Gallery),
                                      ('/Membership', Membership),
                                      ('/Packages', Packages),
                                      ('/Pricing', Pricing),
                                      ('/Testimonials', Testimonials),
                                      ('/FAQ', FAQ),
                                      ('/Leaderboards', Leaderboards),
                                      ('/GetMenLeaderBoard', GetMenLeaderBoard),
                                      ('/GetWomenLeaderBoard', GetWomenLeaderBoard),
                                      ('/Newsletter', NewsletterSignUp),
                                      ('/Tournaments', Tournaments),
                                      ('/SiteMap', SiteMap),
                                      ('/Invitation', DownloadInvitaton),
                                      ('/Schools', DownloadSchools),
                                      ], debug=True)


def main():
    run_wsgi_app(app)

if __name__ == "__main__":
    main()