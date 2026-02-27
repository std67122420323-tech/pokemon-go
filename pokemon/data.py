from pokemon.extensions import db
from pokemon.models import Type

pokemon_types = [
    'Water', 'Fire', 'Grass', 'Flying', 'Rock',
    'Ground', 'Steel', 'Electric', 'Fairy', 'Ghost',
    'Dark', 'Dragon', 'Ice', 'Bug', 'Fighting',
    'Poison', 'Psychic', 'Normal'
]

for t in pokemon_types:
    db.session.add(Type(name=t))

db.session.commit()