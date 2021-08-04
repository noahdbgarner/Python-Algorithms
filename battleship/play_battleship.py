from player import Player

def play_battleship(player_1, player_2, datafile) -> None:

    player_1.build_grid_and_place_ships(datafile)
    player_2.build_grid_and_place_ships(datafile)

    print(f"{player_1.get_name()} VS {player_2.get_name()}")

    # Print grids and PvP until a player loses all their ships
    while True:
        player_2.print_grid()
        player_1.print_grid()
        player_1.attack(player_2.grid)
        player_2.attack(player_1.grid)

def print_battleship_rules():
    print("""Welcome to Battleship!
    
In this game, you and the opponent will take turns attacking each other's ships on a grid.
The ships will be randomly placed for you and the opponent.
The first player to sink all the other player's ships wins!
To make the game more interesting, add more ships to data.json, or change rows | cols

How to play:
    1. When prompted enter your name
    2. When prompted, enter a grid coordinate to attack (e.g. a10 or J1) 
    """)

if __name__ == "__main__":

    # Print rules
    print_battleship_rules()

    # Create player and computer
    player = Player(name=input(f"Enter your name when you are ready to play: "))
    computer = Player(name="computer", is_computer=True)
    data = "data.json"

    # Play Battleship
    play_battleship(player, computer, data)