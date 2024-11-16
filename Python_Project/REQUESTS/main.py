import requests

URL = 'https://api.pokemonbattle.ru'
TOKEN = 'a7c08a0438309a9cb9063999471633c5'
HEADER =  {'Content-Type': 'application/json',
            'trainer_token': TOKEN
}
body_create = {
    "name": "generate",
    "photo_id": -1
}

body_change = {
    "pokemon_id": "134168",
    "name": "Паразит",
    "photo_id": -1
}

body_pokeball = {
    "pokemon_id": "134168"
}

response_create = requests.post(url = f'{URL}/v2/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

response_change = requests.put(url = f'{URL}/v2/pokemons', headers = HEADER, json = body_change)
print(response_change.text)

response_pokeball = requests.post(url = f'{URL}/v2/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)





