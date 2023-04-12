import requests


def get_json(url):
    return requests.get('https://pokeapi.co/api/v2/' + url).json()


def generate_pokemon_list():
    updated_pokemon_list = []
    for pokemon in get_json('pokemon_pictures?limit=100000&offset=0')['results']:
        updated_pokemon_list.append(pokemon['name'])
    return updated_pokemon_list


def get_sprites(pokemon):
    return get_json('pokemon_pictures/' + pokemon)['sprites']['front_default']
