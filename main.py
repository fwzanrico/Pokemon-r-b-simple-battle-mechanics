from createpokemondb import *
from user_classifier import *
import tkinter as tk



def main():
    pokemon_list = create_list_of_pokemon()
    player1 = Player('rico', 'Manual', pokemon_list)
    player1.select_pokemon(pokemon_list)
    player2 = Bot('bot', 'Auto', pokemon_list)
    player2.select_pokemon(pokemon_list, player1.pokemon)
    print(player1.pokemon.get_name())
    print(player2.pokemon.get_name())

if __name__ == '__main__':
    main()