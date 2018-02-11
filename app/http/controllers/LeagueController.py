''' A Module Description '''
from app.League import League
from app.Team import Team

class LeagueController(object):
    ''' Class Docstring Description '''

    def __init__(self):
        pass

    def show(self):
        league = League.find(request().param('id'))

        return view('leagues/index', {'league': league})

    def teams(self):
        league = League.find(request().param('id'))
        teams = Team.where('league_id', league.id).get()

        return view('leagues/teams', {'league': league, 'teams': teams})
