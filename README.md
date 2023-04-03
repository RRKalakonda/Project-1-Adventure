# Project-1-Adventure

Rishika Reva Kalakonda - rkalakon@stevens.edu

URL of this Git repo https://github.com/RRKalakonda/Project-1-Adventure

I have spent around 30 hours to do this project, majorly I spent much time doing code refactoring, handling errors & corner case scenarios

## Testing

To test the program, I created a map that allowed me to perform all actions such as 'go', 'get', and 'drop'. The map included rooms with different items and exits, ensuring that I could test various scenarios. Throughout the testing process, I made sure to test the 'help', 'quit', and 'inventory' actions at various stages of the game to confirm that they functioned correctly in different scenarios. This comprehensive testing approach helped me validate the program's functionality and ensure that it works as expected for all the supported actions and directions.


## Bugs & Issues

During the development and testing of the program, there were a few issues that needed to be addressed. One such issue was the incorrect error message displayed when using the 'go' verb without a direction. The program initially showed the error message "Sorry, you need to 'get' something." instead of "Sorry, you need to 'go' somewhere."

To resolve this issue, I reviewed the code and identified that the 'go' verb's error handling was using the wrong message. I corrected the error message in the code and retested the program to confirm that the appropriate error message was displayed when using the 'go' verb without a direction.

Resolving these issues and any other bugs encountered during development and testing required a thorough understanding of the code, careful debugging, and diligent testing to ensure that the program functioned correctly for all supported actions and directions.

## Extensions

I have implemented the following three extensions in the text adventure game:

Directions as verbs:
This extension allows players to use single-letter directions (e.g., 'n', 's', 'e', 'w', 'nw', 'ne', 'sw', 'se') as verbs, simplifying the navigation process. This feature does not interfere with other verbs that have similar starting letters, such as 'eat'. To exercise this feature, you can simply type the single-letter direction command while playing the game, and the player will move in the corresponding direction, if available. The directions can be used in any room where there are valid exits.

Drop verb:
The 'drop' verb allows players to drop items from their inventory into the current room. This feature complements the 'get' verb, enabling players to pick up and drop items throughout the game. To exercise the 'drop' feature, pick up an item using the 'get' verb and then use the 'drop' verb followed by the item's name. The item will be dropped in the current room, and the room's description will be updated to include the dropped item.

Help verb:
The 'help' verb displays a list of available commands to assist players in navigating the game. The help text is generated dynamically, ensuring that any new commands added to the game are automatically included in the help message. To exercise the 'help' feature, simply type 'help' while playing the game. The list of available commands, including their correct usage, will be displayed.

These extensions can be tested in any room on the map, as they are not tied to specific locations. By incorporating these features, the text adventure game becomes more user-friendly, allowing for a more engaging and interactive gaming experience.


# Text Adventure Game

This is a simple text-based adventure game developed in Python. The game enables players to explore a set of interconnected rooms, pick up and drop items, and engage with their surroundings using a variety of commands.

## Getting Started

To begin the game, simply execute the adventure.py file in your Python environment:

```
python adventure.py <map>
```
## Game Features

The game supports the following commands, allowing players to interact with the game world:

- go [direction]: Move the player in the specified direction (north, south, east, west, etc.). Example: go north.
- [direction]: A shorthand for the "go" command, which lets players move in a direction by merely typing the direction. Example: north (equivalent to go north).
- look: Display the current room's name, description, available exits, and any items in the room.
- get [item]: Pick up the specified item from the current room and add it to the player's inventory. Example: get rose.
- drop [item]: Remove the specified item from the player's inventory and place it in the current room. Example: drop rose.
- inventory: Show the player's current inventory, listing all the items being carried.
- help: Present a list of available commands and their usage.
- quit: Exit the game.

## Game Structure

The game's rooms and items are defined in a JSON file (loop.map). Each room in the JSON file is represented by a dictionary containing the following keys:

- name: The room's name (a string).
- desc: A description of the room (a string).
- exits: A dictionary representing the available exits from the room, with keys being the direction (e.g., "north") and values being the corresponding room ID.
- items (optional): A list of items present in the room.

The game reads the JSON file and stores the data in a Python dictionary. Players navigate through the rooms using the "go" command or by typing a direction as a shorthand.

The primary game loop processes player input, calling the corresponding functions for each command. When a player successfully moves to a new room, the game displays the new room's description, available exits, and any items present.
