rooms= {
    "entrance": {
    "description": "A dark stone entrance. Torches flicker on the walls." ,
    "exits": {"north": "library", "east": "garden"},
    "items": {"torch": "A flickering torch.", "key": "A rusty key."}
    },
    "library": {
    "description": "A dusty library filled with ancient books.",
    "exits": {"south": "entrance"},
    "items": {"book": "An ancient book.", "quill": "A feathered quill."}
    },
    "garden": {
    "description": "A lush garden with blooming flowers.",
    "exits": {"west": "entrance"},
    "items": {"flower": "A fragrant flower.", "shovel": "A sturdy shovel."}  
    },
    "treasure_room": {
    "description": "A hidden room filled with treasures.",
    "exits": {"south": "library"},
    "items": {"gold": "A pile of gold coins.", "gem": "A"}
    }
}   

def show_room(room_name):
    room = rooms[room_name]
    print("\n" + "=" * 40)
    print("LOCATION:", room_name.upper())
    print(room["description"])
    if room["items"]:
        print("ITEMS:", ", ".join(room["items"].keys()))
    if room["exits"]:
        print("EXITS:", ", ".join(room["exits"].keys()))

def move(current_room, direction):
    exits = rooms[current_room]["exits"]
    if direction in exits:
        new_room = exits[direction]
        print("You go", direction + ".")
        return new_room
    print("You can't go that way.")
    return current_room

def pick_up(room_name, inventory):
    items = rooms[room_name]["items"]
    if items:
        item_name = next(iter(items))
        items.pop(item_name)
        inventory.append(item_name)
        print("You picked up:", item_name)
    else:
        print("There are no items to pick up.")

# The main game loop
current_room = "entrance"
inventory = []

print("===WELCOME TO THE DUNGEON ADVENTURE===")
print("Commands: go north/south/east/west | pick up | inventory | quit")

while True:
    show_room(current_room)
    if current_room == "treasure_room":
        print("Congratulations! You found the treasure and won the game!")
        break

    cmd = input("\nWhat do you do? ").strip().lower()
    if cmd.startswith("go "):
        direction = cmd[3:]
        current_room = move(current_room, direction)
    elif cmd == "pick up":
        pick_up(current_room, inventory)
    elif cmd == "inventory":
        print("You are carrying:", inventory if inventory else "nothing.")
    elif cmd == "quit":
        print("You fled the dungeon")
        break
    else:
        print("Invalid command. Try again.")
#1. Add the locked door bonus mechanic (needs rusty key to enter treasure romm)
#2. add a 'dungeon' room connected to the entrance going south.
#3. add a monster in on e room -- if you enter without a weapon, you lose.
#4. add a move counter -- tell the player how many moves it took to win""""""



rooms = {
    "entrance": {
        "description": "A dark stone entrance. Torches flicker on the walls.",
        "exits": {"north": "library", "east": "garden", "south": "dungeon"},
        "items": {"torch": "A flickering torch.", "key": "A rusty key."}
    },
    "library": {
        "description": "A dusty library filled with ancient books.",
        "exits": {"south": "entrance", "north": "treasure_room"},
        "items": {"book": "An ancient book.", "quill": "A feathered quill."}
    },
    "garden": {
        "description": "A lush garden with blooming flowers.",
        "exits": {"west": "entrance"},
        "items": {"flower": "A fragrant flower.", "shovel": "A sturdy shovel."}
    },
    "dungeon": {
        "description": "A damp, foul-smelling dungeon. Something growls in the shadows...",
        "exits": {"north": "entrance"},
        "items": {"sword": "A rusty but sharp sword."},
        "monster": "orc"                              # 3. monster flag
    },
    "treasure_room": {
        "description": "A hidden room filled with treasures.",
        "exits": {"south": "library"},
        "items": {"gold": "A pile of gold coins.", "gem": "A glittering gem."},
        "locked": True                                # 1. locked door flag
    }
}

WEAPONS = {"sword", "shovel", "torch"}               


def show_room(room_name):
    room = rooms[room_name]
    print("\n" + "=" * 40)
    print(f"LOCATION: {room_name.upper()}")
    print(room["description"])
    if room.get("monster") and not room.get("monster_defeated"):
        print(f"  A fearsome {room['monster']} blocks your path!")
    if room["items"]:
        print("ITEMS:", ", ".join(room["items"].keys()))
    if room["exits"]:
        print("EXITS:", ", ".join(room["exits"].keys()))


def move(current_room, direction, inventory, moves):
    exits = rooms[current_room]["exits"]
    if direction not in exits:
        print("You can't go that way.")
        return current_room, moves

    target = exits[direction]

    if rooms[target].get("locked"):
        if "key" not in inventory:
            print("The door is locked. You need a key to enter.")
            return current_room, moves
        print("You use the rusty key to unlock the door. It creaks open...")

    
    if rooms[target].get("monster") and not rooms[target].get("monster_defeated"):
        has_weapon = any(item in WEAPONS for item in inventory)
        if not has_weapon:
            print(f"\nYou stumble into the dungeon unarmed.")
            print(f"The {rooms[target]['monster']} lunges at you — you are defeated!")
            print(f" GAME OVER. You lasted {moves} move(s).")
            return None, moves                        # None signals game over
        print(f"You brandish your weapon at the {rooms[target]['monster']}!")
        print(f"The {rooms[target]['monster']} flees into the darkness. The dungeon is safe.")
        rooms[target]["monster_defeated"] = True

    moves += 1                                       
    print(f"You go {direction}.")
    return target, moves


def pick_up(room_name, inventory, item_name=None):
    items = rooms[room_name]["items"]
    if not items:
        print("There are no items here.")
        return
    if item_name is None:
        print("Pick up what?", ", ".join(items.keys()))
        return
    if item_name not in items:
        print(f"There's no '{item_name}' here.")
        return
    inventory.append(item_name)
    items.pop(item_name)
    print(f"You picked up: {item_name}")


# Main game loop
current_room = "entrance"
inventory = []
moves = 0                                         

print("=== WELCOME TO THE DUNGEON ADVENTURE ===")
print("Commands: go <direction> | pick up <item> | look | inventory | quit")
print("Tip: explore carefully — some doors are locked, and monsters lurk below.\n")

while True:
    show_room(current_room)

    if current_room == "treasure_room":
        print(f" Congratulations! You found the treasure and won in {moves} move(s)!")
        break

    cmd = input("\nWhat do you do? ").strip().lower()

    if cmd.startswith("go "):
        result_room, moves = move(current_room, cmd[3:], inventory, moves)
        if result_room is None:                       
            break
        current_room = result_room
    elif cmd.startswith("pick up "):
        pick_up(current_room, inventory, item_name=cmd[8:])
    elif cmd == "pick up":
        pick_up(current_room, inventory)
    elif cmd == "look":
        pass                                          
    elif cmd == "inventory":
        print("You are carrying:", inventory if inventory else "nothing.")
    elif cmd == "quit":
        print(f"You fled the dungeon after {moves} move(s).")
        break
    else:
        print("Invalid command. Try again.")