# Project-1-Adventure
Rishika Reva Kalakonda


# Text Adventure Game

This is a simple text-based adventure game written in Python. The game allows players to navigate through a set of interconnected rooms, pick up and drop items, and interact with their environment using various commands.

## Getting Started

To start the game, simply run the `adventure.py` file in your Python environment:

```
python adventure.py <map>
```
## Game Features

The game supports the following commands for players to interact with the game world:

- **go [direction]**: Move the player in the specified direction (north, south, east, west, etc.). Example: `go north`.
- **[direction]**: Shorthand for the go command, allowing players to move in a direction by just typing the direction. Example: `north` (equivalent to `go north`).
- **look**: Show the current room's name, description, available exits, and any items present in the room.
- **get [item]**: Pick up the specified item from the current room and add it to the player's inventory. Example: `get rose`.
- **drop [item]**: Remove the specified item from the player's inventory and place it in the current room. Example: `drop rose`.
- **inventory**: Display the player's current inventory, listing all the items being carried.
- **help**: Show a list of available commands and their usage.
- **quit**: Exit the game.

## Game Structure

The game's rooms and items are defined in a JSON file (`loop.map`). Each room in the JSON file is represented by a dictionary containing the following keys:

- **name**: The room's name (a string).
- **desc**: A description of the room (a string).
- **exits**: A dictionary representing the available exits from the room, with keys being the direction (e.g., "north") and values being the corresponding room ID.
- **items** (optional): A list of items present in the room.

The game reads the JSON file and stores the data in a Python dictionary. Players navigate through the rooms using the "go" command or by typing a direction as a shorthand.

The main game loop processes player input, calling the corresponding functions for each command. When a player successfully moves to a new room, the game displays the new room's description, available exits, and any items present.

## Testing

A test plan is provided to cover various game scenarios and test the functionality of each command. The test plan includes input examples and their expected outputs. To ensure the game works as expected, follow the test plan and verify that the output matches the expected results.
