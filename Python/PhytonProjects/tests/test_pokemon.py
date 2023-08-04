import requests
import pytest

token = '6ba142efc196fa9a4edd4c9b1037fb59'
host = 'https://api.pokemonbattle.me:9104'

def test_status_code():
    response = requests.get(f'{host}/trainers')
    assert response.status_code == 200

def test_search_name():
    response = requests.get(f'{host}/trainers', params= {'trainer_id' : "1272"})
    assert response.json()['trainer_name'] == 'Poda'
    