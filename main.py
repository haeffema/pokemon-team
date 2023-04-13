import os

import requests
from PIL import Image


def get_json(url):
    return requests.get('https://pokeapi.co/api/v2/' + url).json()


def get_pokemon_sprite(pokemon):
    return get_json('pokemon/' + pokemon)['sprites']['front_default']


def get_image(url):
    return Image.open(requests.get(url, stream=True).raw)


def generate_image_files(team):
    for f in os.listdir("pokemon_pictures"):
        if not f.endswith(".png"):
            continue
        os.remove(os.path.join("pokemon_pictures", f))
    counter = 1
    for pokemon in team:
        img = get_image(get_pokemon_sprite(pokemon.lower()))
        img.save(f"pokemon_pictures/p{counter}.png")
        counter += 1


if __name__ == '__main__':
    generate_image_files(["Aerodactyl", "Combusken", "Vileplume", "Quagsire", "Dusclops", "Flaaffy"])
