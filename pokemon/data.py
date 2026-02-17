pokemon_types =[
 'water', 'Fire', 'Grass', 'Flying', 'Rock',
 'Ground', 'Steel', 'Electric', 'Fairy', 'Ghost',
 'Dark', 'Dragon', 'Ice','Bug', 'Fighting', 'poison',
 'Psychic', 'Normal', 
 ]

from pokemon.models import Type
type =[Type(name=type) for type in pokemon_types]