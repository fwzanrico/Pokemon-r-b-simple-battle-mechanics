import csv
import os
import random
import time
from abc import ABC, abstractmethod
class Move():
    def __init__(self, Name, Damage, Accuracy, Effect, Duration):
        self.__name = Name
        self.__Damage = Damage
        self.__Accurasy = Accuracy
        self.__Effect = Effect
        self.__Duration = Duration
    def get_name(self):
        return self.__name
    def get_damage(self):
        return self.__Damage
    def get_accurasy(self):
        return self.__Accurasy
    def get_effect(self):
        return self.__Effect
    def get_duration(self):
        return self.__Duration
class Pokemon(ABC):
    def __init__(self, Name, HP, Attack, Defense, Sp_attack, Sp_defense, Speed, Elemental, Type, Moves) -> None:
        self.__name = Name
        self.__HP = HP
        self.__Attack = Attack
        self.__Defense = Defense
        self.__SPattack = Sp_attack
        self.__SPDefense = Sp_defense
        self.__Speed = Speed
        self.__Elemental = Elemental
        self.__Type = Type
        self.__Skills = Moves

    def get_name(self):
        return self.__name
    def get_hp(self):
        return self.__HP
    def get_defense(self):
        return self.__Defense
    def get_spattack(self):
        return self.__SPattack
    def get_spdefence(self):
        return self.__SPDefense
    def get_Speed(self):
        return self.__Speed
    def get_Elemental(self):
        return self.__Elemental
    def get_Type(self):
        return self.__Type
    
    def attack(self, other, move):
        move_name = move.get_name()
        move_damage = move.get_damage()
        move_accurasy = move.get_accurasy()
        move_effect = move.get_effect()
        move_duration = move.get_duration()
        if move_accurasy > random.randint(0,100):
            if move_effect == 'burn':
                other.__HP -= move_damage
                other.__HP -= 10
                print(f'{self.__name} used {move_name} and dealt {move_damage} damage and inflicted burn')
            elif move_effect == 'none':
                other.__HP -= move_damage
                print(f'{self.__name} used {move_name} and dealt {move_damage} damage')
            elif move_effect == 'poison':
                other.__HP -= move_damage
                other.__HP -= 5
                print(f'{self.__name} used {move_name} and dealt {move_damage} damage and inflicted poison')
            elif move_effect == 'paralyze':
                other.__HP -= move_damage
                other.__HP -= 5
                print(f'{self.__name} used {move_name} and dealt {move_damage} damage and inflicted paralyze')
            elif move_effect == 'freeze':
                other.__HP -= move_damage
                other.__HP -= 5
                print(f'{self.__name} used {move_name} and dealt {move_damage} damage and inflicted freeze')
        else:
            print(f'{self.__name} missed {move_name}')




class FirePokemon(Pokemon):
    def __init__(self, Name, HP, Attack, Defense, Sp_attack, Sp_defense, Speed, Elemental, Type, Moves) -> None:
        super().__init__(Name, HP, Attack, Defense, Sp_attack, Sp_defense, Speed, Elemental, Type, Moves)
        self.__Elemental = 'fire'
        self.__SkillEffect = 'burn'
        fireball = Move('fireball',30,70,self.__SkillEffect,2)
        skill_set = Moves
        skill_set.append(fireball)
        self.__Skills = skill_set


class GrassPokemon(Pokemon):
    def __init__(self, Name, HP, Attack, Defense, Sp_attack, Sp_defense, Speed, Elemental, Type, Moves) -> None:
        super().__init__(Name, HP, Attack, Defense, Sp_attack, Sp_defense, Speed, Elemental, Type, Moves)
        self.__Elemental = 'grass'
        grass_whip = Move('root whip',18,90,'none',1)
        skill_set = Moves
        skill_set.append(grass_whip)
        self.__Skills = skill_set


class WaterPokemon(Pokemon):
    def __init__(self, Name, HP, Attack, Defense, Sp_attack, Sp_defense, Speed, Elemental, Type, Moves) -> None:
        super().__init__(Name, HP, Attack, Defense, Sp_attack, Sp_defense, Speed, Elemental, Type, Moves)
        self.__Elemental = 'water'
        water_gun = Move('water gun',25,80,'none',1)
        skill_set = Moves
        skill_set.append(water_gun)
        self.__Skills = skill_set


class IcePokemon(Pokemon):
    def __init__(self, Name, HP, Attack, Defense, Sp_attack, Sp_defense, Speed, Elemental, Type, Moves) -> None:
        super().__init__(Name, HP, Attack, Defense, Sp_attack, Sp_defense, Speed, Elemental, Type, Moves)
        self.__Elemental = 'ice'
        ice_beam = Move('ice beam',30,70,'freeze',1)
        skill_set = Moves
        skill_set.append(ice_beam)
        self.__Skills = skill_set


class ElectricPokemon(Pokemon):
    def __init__(self, Name, HP, Attack, Defense, Sp_attack, Sp_defense, Speed, Elemental, Type, Moves) -> None:
        super().__init__(Name, HP, Attack, Defense, Sp_attack, Sp_defense, Speed, Elemental, Type, Moves)
        self.__Elemental = 'electric'
        thunderbolt = Move('thunderbolt',35,60,'paralyze',1)
        skill_set = Moves
        skill_set.append(thunderbolt)
        self.__Skills = skill_set

def create_list_of_pokemon():
    # create charizard
    charizard_skill_set = []
    tail_whip = Move('tail whip', 10, 100, 'stun', 2)
    claw = Move('claw', 20, 80, 'none', 1)
    charizard_skill_set = [tail_whip, claw]
    charizard = FirePokemon('charizard', 100, 20, 10, 30, 20, 30, 'fire', 'ground', charizard_skill_set)
    # create venusaur
    venusaur_skill_set = []
    vine_whip = Move('vine whip', 10, 100, 'none', 1)
    razor_leaf = Move('razor leaf', 20, 80, 'none', 1)
    venusaur_skill_set = [vine_whip, razor_leaf]
    venusaur = GrassPokemon('venusaur', 100, 20, 10, 30, 20, 30, 'grass', 'ground', venusaur_skill_set)
    # create blastoise
    blastoise_skill_set = []
    water_gun = Move('water gun', 10, 100, 'none', 1)
    hydro_pump = Move('hydro pump', 20, 80, 'none', 1)
    blastoise_skill_set = [water_gun, hydro_pump]
    blastoise = WaterPokemon('blastoise', 100, 20, 10, 30, 20, 30, 'water', 'grund', blastoise_skill_set)
    # create lapras 
    lapras_skill_set = []
    water_gun = Move('water gun', 10, 100, 'none', 1)
    hydro_pump = Move('hydro pump', 20, 80, 'none', 1)
    lapras_skill_set = [water_gun, hydro_pump]
    lapras = WaterPokemon('lapras', 100, 20, 10, 30, 20, 30, 'water', 'water', lapras_skill_set)
    # create articuno
    articuno_skill_set = []
    ice_beam = Move('ice beam', 10, 100, 'freeze', 1)
    blizzard = Move('blizzard', 20, 80, 'freeze', 1)
    articuno_skill_set = [ice_beam, blizzard]
    articuno = IcePokemon('articuno', 100, 20, 10, 30, 20, 30, 'ice', 'fly', articuno_skill_set)
    # create zapdos
    zapdos_skill_set = []
    thunderbolt = Move('thunderbolt', 10, 100, 'paralyze', 1)
    thunder = Move('thunder', 20, 80, 'paralyze', 1)
    zapdos_skill_set = [thunderbolt, thunder]
    zapdos = ElectricPokemon('zapdos', 100, 20, 10, 30, 20, 30, 'electric', 'electric', zapdos_skill_set)

    pokemon_list = [charizard, venusaur, blastoise, lapras, articuno, zapdos]
    return pokemon_list