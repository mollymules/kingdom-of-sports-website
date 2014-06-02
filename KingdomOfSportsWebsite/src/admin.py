import webapp2
import os
import datetime
import json

from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
from kosdatastore.SeniorLeaderBoard import SeniorLeaderBoard
from kosdatastore.WomenLeaderBoard import WomenLeaderBoard

class AdminHome(webapp2.RequestHandler):    
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), 'Admin/Admin.html')
        self.response.out.write(template.render(path, template_values))

class LeaderBoard(webapp2.RequestHandler):    
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), 'Admin/AdminLeaderBoard.html')
        self.response.out.write(template.render(path, json.dumps(template_values)))
    def post(self):
        emailAddress = self.request.get('email')
        score = self.request.get('score')
        name = self.request.get('name')
        leaderBoard = self.request.get('board')
        if leaderBoard == 'm':
            isAlreadyPresent = SeniorLeaderBoard.query(SeniorLeaderBoard.email == emailAddress).get()
            if isAlreadyPresent is None:
                newSignUp = SeniorLeaderBoard(email = emailAddress, date = datetime.datetime.now(), score = int(score), name = name)
                newSignUp.put() 
            else:
                isAlreadyPresent.score = int(score)
                isAlreadyPresent.put()              
                               
        else:
            isAlreadyPresent = WomenLeaderBoard.query(WomenLeaderBoard.email == emailAddress).get()
            if isAlreadyPresent is None:
                newSignUp = WomenLeaderBoard(email = emailAddress, date = datetime.datetime.now(), score = int(score), name = name)
                newSignUp.put() 
            else:
                isAlreadyPresent.score = int(score)
                isAlreadyPresent.put()                        
        
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), 'Admin/AdminLeaderBoard.html')
        self.response.out.write(template.render(path, json.dumps(template_values)))
        
        
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
        
app = webapp2.WSGIApplication([('/Admin/', AdminHome),
                               ('/Admin/Leader', LeaderBoard),
                               ('/GetMenLeaderBoard', GetMenLeaderBoard),
                               ('/GetWomenLeaderBoard', GetWomenLeaderBoard),
                                ], debug=True)


def admin():
    run_wsgi_app(app)

if __name__ == "__admin__":
    admin()