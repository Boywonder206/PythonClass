#This game is about a boy facing monsters and he just wants to escape to safety
from turtle import *
print("Chaos is taking place outside. Monsters roam the land chasing the people of this land, while your in the corner of your room, scared. You conjure up all of your strength and make a plan to escape to the airport, but you face a choice.")
user = str(input("chose '1' if you want to search the police station thatis across the street in search of weapons. Chose '2' if you want to search more of the aparment complex "))

if user == '1':
    print("You were able to successfully reach the police station and luckly the zombies were locked up ina  jail cell, but who did it? You stumble across a baton, so you store it in your backpack. You collect all the resources you need, but you need a way of transportation")
if user == '2':
    print("You attempted to search the apartment complex, but the nosy neighbor has devoured you")
    
