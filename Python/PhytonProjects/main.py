import requests

token = '6ba142efc196fa9a4edd4c9b1037fb59'
host = 'https://api.pokemonbattle.me:9104'

'''response_add_pokemon = requests.post(f'{host}/pokemons', json = {
    "name": "Домашка",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
},
headers = {'trainer_token' : token,
           'Content-Type' : 'application/json'})'''

'''response_rename_pokemon = requests.put(f'{host}/pokemons', json = {
    "pokemon_id": "5895",
    "name": "new name",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"

},
headers = {'trainer_token' : token,
           'Content-Type' : 'application/json'})'''


response_add_pokeball = requests.post(f'{host}/trainers/add_pokeball', json = {
    "pokemon_id": "5895",

},
headers = {'trainer_token' : token,
           'Content-Type' : 'application/json'})

print (response_add_pokeball.text)

