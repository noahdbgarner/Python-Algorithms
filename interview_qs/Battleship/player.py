from grid import Grid
import random
import json

class Player:
    """
    Representation of the Player class. A Player has a Grid and may be a computer
    """
    def __init__(self,
                 name="",
                 grid: Grid="",
                 is_computer=""):

        self.name: str = name
        self.grid: Grid = grid
        self.is_computer: bool = is_computer

    def build_grid_and_place_ships(self, game_data) -> None:
        """
        Description:
            Validates the game_data, builds the grid, builds the ships, and places the ships
        """
        dimensions, ships = self.validate_and_get_dimensions_and_ships(game_data)

        self.grid = Grid(rows=dimensions["rows"], cols=dimensions["cols"])
        self.grid.build_ships(ships)
        self.grid.randomly_set_ship_locations()

    def attack(self, enemy_grid: Grid) -> None:
        coord, col, row = self.validate_and_get_attack_coord(enemy_grid)
        print(f"{self.name} attacked {coord}!")

        location_data = self.damage_ship_and_get_location_data(coord, col, row, enemy_grid)

        # Update the location data to the shots dictionary
        enemy_grid.shots_dict[str(col) + str(row)] = location_data

    def validate_and_get_attack_coord(self, enemy_grid) -> tuple:
        while True:
            coord = self.get_attack_coord(enemy_grid)
            # Handles bad input of the form '7b', '//', '%m', 'a?', '?7'...
            try:
                col, row = int(ord(coord[0])) - 97, int(coord[1:]) - 1
            except ValueError:
                print("Bad input. Coordinate must be of the form a10 or J1")
            else:
                not_in_shots_dict = enemy_grid.attack_not_in_shots_dict(coord, col, row, self.is_computer)
                in_grid = enemy_grid.attack_inside_grid(coord, col, row)

                if not_in_shots_dict and in_grid:
                    break

        return coord, col, row

    def get_attack_coord(self, enemy_grid) -> str:
        coord = chr(random.randrange(97, 97 + enemy_grid.cols)) + str(random.randint(1, enemy_grid.rows))
        if not self.is_computer:
            coord = self.get_and_validate_player_input()
        return coord

    def get_and_validate_player_input(self) -> str:
        """
        Description:
            Checks user input is within grid. Assumes the grid has equal cols and rows
        """
        while True:
            coord = input("Choose a coordinate to fire on: ").lower()
            if 1 < len(coord) <= len(str(self.grid.cols)) + 1:
                break
            print("Bad length. Coordinate must be of the form a10 or J1")
        return coord

    def damage_ship_and_get_location_data(self, coord, col, row, enemy_grid) -> str:
        """
        Description:
            Sets default location_data to a miss. If the (col, row) is a ship location,
            mark it has a hit, and decrement ship health. Then, check if the game is over
        """
        location_data = "M"
        if (col, row) in enemy_grid.ship_locations:
            location_data = "H"
            print(f"{coord} was a hit!")

            # Find the ship that was hit, and decrement it's health. Check if game is over
            for ship in enemy_grid.grid_ships:
                if (col, row) in ship.get_coords():
                    ship.decrement_health()
                    self.is_game_over(enemy_grid)

        if location_data == "M":
            print(f"{coord} missed!")
        return location_data

    def is_game_over(self, enemy_grid) -> None:
        if enemy_grid.all_ships_sunk():
            print(f"{self.name} wins!")
            exit(0)

    def print_grid(self) -> None:
        print(self.name)
        # Print offset, and col headers, considering num rows could change
        print(' ' * (len(str(self.grid.rows)) + 1), end="")
        print(*[chr(c+97).upper() for c in range(self.grid.cols)], end="")

        for r in range(self.grid.rows):
            # Print row headers, and offset considering num rows could change
            offset = ' ' * ((len(str(self.grid.rows))) - len(str(r+1)))
            print(f"\n{r+1} " + offset, end="")

            for c in range(self.grid.cols):
                coord = str(c)+str(r)
                location_info = self.grid.shots_dict.get(coord, "~")

                # If not computer grid, we should print first letter of ship if (c, r) not hit yet
                if coord not in self.grid.shots_dict and (c, r) in self.grid.ship_locations and not self.is_computer:
                    for ship in self.grid.grid_ships:
                        if (c, r) in ship.get_coords():
                            location_info = ship.get_name()[0]

                print(location_info + " ", end="")
        print("\n")

    @staticmethod
    def validate_and_get_dimensions_and_ships(data) -> tuple:
        """
        Description:
            1. Reads the data_file
            2. Checks rows * cols < sum_ship_health
            3. Checks rows and cols < max_ship_health
            4. Returns the dimensions and ships data
        """
        with open(data) as file:

            dimensions = json.loads(file.read())[0]
            rows = dimensions["rows"]
            cols = dimensions["cols"]

            # Reset the file.read() cursor
            file.seek(0)

            ships = json.loads(file.read())[1:]

            # get max_ship_health and sum_ship_health
            max_ship_health = 0
            sum_ship_health = 0
            for ship in ships:
                sum_ship_health += ship["health"]
                if ship["health"] > max_ship_health:
                    max_ship_name = ship["name"]
                    max_ship_health = ship["health"]

            # Check rows * cols < sum(each ship["health"])
            if rows * cols < sum_ship_health:
                print("Grid dimensions not large enough to place all ships. Please check 'data.json'. Exiting.")
                exit(1)

            # Check rows and cols < max ship["health"]
            if rows < max_ship_health and cols < max_ship_health:
                print(f"Grid dimensions not large enough for {max_ship_name}. Please check 'data.json'. Exiting.")
                exit(1)

        return dimensions, ships