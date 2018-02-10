''' A Module Description '''
from masonite.view import view
from app.League import League
from app.Team import Team

class LeagueController(object):
    ''' Class Docstring Description '''

    def __init__(self):
        pass

    def show(self, Request, View):
        league = League.find(Request.param('id'))
        return View('leagues/index', {'league': league})

    def teams(self, Request, View):
        league = League.find(Request.param('id'))
        teams = Team.where('league_id', league.id).get()

        return View('leagues/teams', {'league': league, 'teams': teams})
