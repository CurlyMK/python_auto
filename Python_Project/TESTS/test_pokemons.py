import requests
import pytest

URL = 'https://api.pokemonbattle.ru'
TOKEN = 'a7c08a0438309a9cb9063999471633c5'
HEADER =  {'Content-Type': 'application/json',
            'trainer_token': TOKEN}
TRAINER_ID = '8425'

def test_status_code():
    response = requests.get(url = f'{URL}/v2/trainers', params={'page': 1})
    assert response.status_code == 200

def test_response_trainer_name():
    response_2 = requests.get(url = f'{URL}/v2/trainers', params={'trainer_id': TRAINER_ID})
    assert response_2.json()["data"][0]['trainer_name'] == 'The Event Horizon'