my_game_character={
    "name": "Alex",
    "level": 100,
    "hp": 200,
    "attack": "super speed",
    "weapon": "Katana"
}
print(my_game_character)
my_game_character["allies"]= "Maxim"
print(my_game_character)
print(my_game_character.get("level"))
del my_game_character["allies"]
print (my_game_character)