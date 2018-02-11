''' A Module Description '''
from app.League import League
from app.Pokemon import Pokemon
from app.DraftedPokemon import DraftedPokemon

from config import database

class DraftController(object):
    ''' Class Docstring Description '''

    def __init__(self):
        pass

    def show(self, Request):
        league = League.find(Request.param('id'))

        return view('leagues/draft', {'league': league})
    
    def draft(self, Request):
        league = League.find(Request.param('id'))
        
        if Request.has('draft'):
            DraftedPokemon.create(
                team_id=league.current.team(league).id,
                pokemon_id=Request.input('pokemon'),
                league_id=league.id
            )

            DraftedPokemon.where('queue_id', Request.input('pokemon')).where('league_id', league.id).delete()

            return Request.redirect('/league/@id/draft?message=Draft Successful')

        elif Request.has('unqueue'):
            DraftedPokemon \
                .where('queue_id', Request.input('pokemon')) \
                .where('team_id', Request.user() \
                .team(league).id).where('league_id', league.id) \
                .first().delete()

            return Request.redirect('/league/@id/draft?message=Successfully Unqueued')

        elif Request.has('queue'):
            DraftedPokemon.create(
                team_id=league.current.team(league).id,
                queue_id=Request.input('pokemon'),
                league_id=league.id
            )
            return Request.redirect('/league/@id/draft?message=Queue Successful')