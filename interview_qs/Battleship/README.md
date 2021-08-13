# Battleship (OOP Python Version)

## 1. Introduction

### 1.1 Description
This program plays the classic game Battleship. It was built to be scalable with respect to grid dimensions and ships.
Feel free to add/remove ships or change cols/rows in data.json. Additionally, please try passing 'is_computer=True' to
both player objects in **play_battleship.py**, and see what happens.

### 1.2 Technologies

- Python 3.6 or higher 
   - This is required because I make use of annotating variables and functions with type hints

## 2. Design

### 2.1 Files
- **data.json**
   - contains grid dimension and ship data
- **grid.py**
   - contains the Grid class
- **play_battleship.py**
   - contains the program driver
- **player.py**
   - Contains the Player class
- **ship.py**
   - Contains the Ship class

### 2.2 Behavior
- The driver prints battleship instructions, creates two players, and plays battleship
- Both players create their grids and place their ships on the grid
- Players print their grids and take turns attacking each other until a player has no ships left

## 3. Setup

### Instructions
- Install Python 3.6 or higher
- In terminal, run `python3 play_battleship.py`

## 4. Approach

### 4.1 Two-dimensional array -> list + dictionary
- I tried solving the problem using a two-dimensional array which I would iterate over to place ships on a grid. 
  After drawing out this solution, I found that it would be more efficient in space and time to add ship locations to a list, and shots fired to a dictionary.
  This reduced the program complexity, because I would not need any two-dimensional array logic. This also reduced the time complexity of searching for shots and ships to O(1).
   
### 4.2 Computer + User -> Player Class
- I started the project with separate classes for the computer and the user. Early into development, however, I realized these classes could be merged into one class. 
  I then added an is_computer field to this new Player class which changes the behavior of certain methods. For example, the attack function will generate a random coordinate if 'is_computer=True'

## 5. Future Improvements
- The computer's coordinate choice could be intelligent. One way to do this would be to add a function that checks coordinates within a close area of a damaged ship.
- The handling and printing of extreme col and row combinations such as 100x1 and 50x50 could be improved
- The Game can support more than two players. However, the Player class could be slightly refactored to hide all Player's ships. This would enable a hot swap game mode.