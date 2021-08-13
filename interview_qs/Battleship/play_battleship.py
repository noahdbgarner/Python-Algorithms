from player import Player
import json
def play_battleship(player_1, player_2, game_data) -> None:
    """
    Description:
        Builds each player's grid and ships. Both players print their grids and attack each other until a player has no ships left
    """
    player_1.build_grid_and_place_ships(game_data)
    player_2.build_grid_and_place_ships(game_data)

    while True:
        player_2.print_grid()
        player_1.print_grid()
        player_1.attack(player_2.grid)
        player_2.attack(player_1.grid)

def print_battleship_info() -> None:
    print("""Welcome to Battleship!
    
In this game, you and the opponent will take turns attacking each other's ships on a grid.
The ships will be randomly placed for you and the opponent.
The first player to sink all the other player's ships wins!

How to play:
    1. When prompted, enter your name
    2. When prompted, enter a grid coordinate to attack (e.g. a10 or J1) 

To make the game more interesting:
    1. Add or remove ships in data.json
    2. Change rows and cols in data.json to increase or decrease the grid size
    3. If you would like to automate the entire game, pass 'is_computer=True' to both player objects in play_battelship.py
""")

if __name__ == "__main__":
    """
    Description:
        1. Prints battleship info and rules
        2. Instantiates two player objects. If is_computer=True, that player will act as a computer
        3. Plays battleship between the two players with ships in data.json
    """
    print_battleship_info()

    player = Player(name=input(f"Enter your name when you are ready to play: "), is_computer=False)
    computer = Player(name="computer", is_computer=True)
    data = "data.json"

    play_battleship(player, computer, data)