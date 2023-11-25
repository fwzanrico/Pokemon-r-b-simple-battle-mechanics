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

    # Start the battle
    battle(player1, player2)

def battle(pokemon1, pokemon2):
    print(f"Battle between {pokemon1.get_name()} and {pokemon2.get_name()}")
    while pokemon1.get_hp() > 0 and pokemon2.get_hp() > 0:
        # Pokemnon 1 attacks Pokemon 2
        selected_move_pokemon1 = random.choice(pokemon1.get_skills())
        pokemon1.attack(pokemon2, selected_move_pokemon1)

        # Check if Pokemon 2 fainted
        if pokemon2.get_hp() <= 0:
            print(f"{pokemon2.get_name()} fainted!")
            break

        # Pokemon 2 attacks Pokemon 1
        selected_move_pokemon2 = random.choice(pokemon2.get_skills())
        pokemon2.attack(pokemon1, selected_move_pokemon2)

        # Check if Pokemon 1 fainted
        if pokemon1.get_hp() <= 0:
            print(f"{pokemon1.get_name()} fainted!")
            break
        print(f"\n{pokemon1.get_name()} HP: {pokemon1.get_hp()} \ {pokemon2.get_hp()}\n")

if __name__ == '__main__':
    main()
