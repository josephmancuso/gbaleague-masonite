''' A League Database Model '''
from orator import DatabaseManager, Model
from orator.orm import belongs_to
from config.database import Model
from config import database

from app.User import User

class League(Model):

    @belongs_to('current_id', 'id')
    def current(self):
        return User

    
    def draftable_pokemon(self):
        id_collection = database.db.table('draftedpokemon').where_not_null('pokemon_id').get().pluck('pokemon_id')
        return database.db.table(
            'pokemon').where_not_in('id', id_collection).order_by('name', 'asc').get()
