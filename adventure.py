import json


import os
import argparse

# Add argument parsing
parser = argparse.ArgumentParser(description="Adventure Game")
parser.add_argument("map_file", help="The JSON file containing the game map.")
args = parser.parse_args()

# Load the game map from the specified file
if not os.path.isfile(args.map_file):
    print(f"Error: {args.map_file} not found.")
    exit(1)

with open(args.map_file, "r") as f:
    map_data = json.load(f)


def is_valid_room(room):
    if not all(key in room for key in ["name", "desc", "exits"]):
        return False

    if not isinstance(room["name"], str) or not isinstance(room["desc"], str) or not isinstance(room["exits"], dict):
        return False

    return True

def validate_map(map_data):
    for room_id, room in enumerate(map_data):
        if not is_valid_room(room):
            return False

        for direction, exit_room_id in room["exits"].items():
            if not isinstance(direction, str) or not isinstance(exit_room_id, int):
                return False

            if exit_room_id < 0 or exit_room_id >= len(map_data):
                return False

    return True


if validate_map(map_data):
    print("The map is valid.")
else:
    print("The map is not valid.")


def display_room(room):
    print(f"> {room['name']}")
    print("")
    print(room['desc'])
    print("")
    if "items" in room:
        if len(room['items']) > 0:
            items = " ".join(room['items'])
            print(f"Items: {items}")
            print("")
    exits = " ".join(room['exits'].keys())
    print(f"Exits: {exits}")
    print("")



def go(direction, current_room, map_data):
    if direction.lower() not in current_room["exits"]:
        print(f"There's no way to go {direction}.")
        return current_room

    new_room_id = current_room["exits"][direction.lower()]
    new_room = map_data[new_room_id]
    print(f"You go {direction}.")
    return new_room

current_room = map_data[0]
display_room(current_room)

def get_item(item, current_room, inventory):
    if "items" in current_room and item in current_room["items"]:
        current_room["items"].remove(item)
        inventory.append(item)
        print(f"You pick up the {item}.")
    else:
        print(f"There's no {item} anywhere.")

def show_inventory(inventory):
    if inventory:
        print("Inventory:")
        for item in inventory:
            print(item)
    else:
        print("You're not carrying anything.")

inventory = []

verbs = {
    "go": "go ...",
    "get": "get ...",
    "drop": "drop ...",
    "look": "look",
    "inventory": "inventory",
    "quit": "quit",
    "help": "help"
}

def display_help():
    print("You can run the following commands:")
    for verb in verbs.values():
        print(verb)

def drop_item(item, current_room, inventory):
    if item in inventory:
        inventory.remove(item)
        if "items" not in current_room:
            current_room["items"] = []
        current_room["items"].append(item)
        print(f"You drop the {item}.")
    else:
        print(f"You don't have a {item} to drop.")

directions = [
    "north",
    "south",
    "east",
    "west",
    "northeast",
    "northwest",
    "southeast",
    "southwest"
]

while True:
    try:
        action = input("What would you like to do? ").strip().split()
    except EOFError:
        print("\nUse 'quit' to exit.")
        continue

    if not action:
        continue

    command = action[0].lower()

    if command in verbs:
        if command == "go":
            if len(action) == 2:
                direction = action[1]
                current_room = go(direction, current_room, map_data)
                display_room(current_room)
            else:
                print("Sorry, you need to 'go' somewhere.")
        elif command == "look" and len(action) == 1:
            display_room(current_room)
        elif command == "get":
            if len(action) == 2:
                item = action[1]
                get_item(item, current_room, inventory)
            else:
                print("You need to 'get' something.")
        elif command == "inventory" and len(action) == 1:
            show_inventory(inventory)
        elif command == "quit" and len(action) == 1:
            print("Goodbye!")
            break
        elif command == "help" and len(action) == 1:
            display_help()
        elif command == "drop":
            if len(action) == 2:
                item = action[1]
                drop_item(item, current_room, inventory)
            else:
                print("You need to 'drop' something.")
        else:
            print("Invalid use of the command. Type 'help' to see the correct usage.")
    elif command in directions and len(action) == 1:
        # direction = [k for k, v in directions.items() if v == command][0]
        current_room = go(command, current_room, map_data)
        display_room(current_room)
    else:
        print("Sorry, you need to use a valid command. Type 'help' to see the available commands.")
