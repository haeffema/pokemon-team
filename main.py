import os

import requests
from PIL import Image


def get_json(url):
    return requests.get('https://pokeapi.co/api/v2/' + url).json()


def generate_pokemon_list():
    updated_pokemon_list = []
    for pokemon in get_json('pokemon?limit=100000&offset=0')['results']:
        updated_pokemon_list.append(pokemon['name'])
    return updated_pokemon_list


def get_pokemon_sprite(pokemon):
    return get_json('pokemon/' + pokemon)['sprites']['front_default']


def generate_image_files(team):
    for f in os.listdir("pokemon_pictures"):
        if not f.endswith(".png"):
            continue
        os.remove(os.path.join("pokemon_pictures", f))
    counter = 1
    for pokemon in team:
        img = Image.open(requests.get(get_pokemon_sprite(pokemon.lower()), stream=True).raw)
        img.save(f"pokemon_pictures/p{counter}.png")
        counter += 1


if __name__ == '__main__':
    generate_image_files(["Charizard", "Ditto", "Aerodactyl", "Umbreon", "Mudkip"])
    # generate_window.render_team()
