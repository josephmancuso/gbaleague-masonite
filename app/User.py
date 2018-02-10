from orator import DatabaseManager, Model
from config.database import Model, db
from app.Team import Team
from app.DraftedPokemon import DraftedPokemon

class User(Model):

    __fillable__ = ['name', 'email', 'password']

    __auth__ = 'email'

    def team(self, league):
        return Team.where('owner_id', self.id).where('league_id', league.id).first()

    def queued_pokemon(self, league):
        ''' Get all queued pokemon ID '''
        return DraftedPokemon.where('league_id', league.id).where('team_id', self.team(league).id).get().pluck('queue_id')
    
    def get_queued_pokemon(self, league):
        return DraftedPokemon \
            .where('league_id', league.id) \
            .where('team_id', self.team(league).id) \
            .where_null('pokemon_id') \
            .where_not_null('queue_id') \
            .get()

    def get_team_pokemon(self, league):
        return DraftedPokemon.where('league_id', league.id).where('team_id', self.team(league).id).where_not_null('pokemon_id').get()