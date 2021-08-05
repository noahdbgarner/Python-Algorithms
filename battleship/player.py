from grid import Grid
import random
import json

class Player:
    """
    Representation of the Player class. A Player has a Grid
    """
    def __init__(self,
                 name="",
                 grid: Grid="",
                 is_computer=""):

        self.name: str = name
        self.grid: Grid = grid
        self.is_computer: bool = is_computer

    def get_name(self) -> str:
        return self.name

    # Build grid, Build ships, and Place ships
    def build_grid_and_place_ships(self, datafile) -> None:

        dimensions = self.read_dimensions(datafile)
        self.grid = Grid(rows=dimensions["rows"], cols=dimensions["cols"])

        ship_data = self.read_ships(datafile)
        self.grid.build_ships(ship_data)

        self.grid.randomly_set_ship_locations()

    # Choose a coordinate to fire on, check the coordinate, and added to the shot_dict
    def attack(self, enemy_grid: Grid) -> None:

        coord, col, row = self.check_and_validate_attack_coord(enemy_grid)
        print(f"{self.name} attacked {coord}!")

        location_data = self.damage_ship_and_update_location_data(coord, col, row, enemy_grid)

        # Add the location data to the shots dictionary
        enemy_grid.shots_dict[str(col) + str(row)] = location_data
        return

    def check_and_validate_attack_coord(self, enemy_grid) -> tuple:
        while True:
            coord = self.get_attack_coord(enemy_grid)

            # Try-else since control flows off of the try
            try:
                col, row = int(ord(coord[0])) - 97, int(coord[1:]) - 1
            except ValueError as err:
                print("Bad input. Coordinate must be of the form a10 or J1")
            else:
                not_in_shots_dict = enemy_grid.attack_not_in_shots_dict(coord, col, row, self.is_computer)
                in_grid = enemy_grid.attack_inside_grid(coord, col, row)

                if not_in_shots_dict and in_grid:
                    break

        return coord, col, row

    def get_attack_coord(self, enemy_grid) -> str:
        # Computer defaults to random char from a to enemy_grid.cols inclusive, and 1 tp enemy_grid.rows
        coord = chr(random.randrange(97, 97 + enemy_grid.cols)) + str(random.randint(1, enemy_grid.rows))
        if not self.is_computer:
            coord = self.get_and_validate_player_input()
        return coord

    def get_and_validate_player_input(self) -> str:
        while True:
            coord = input("Choose a coordinate to fire on: ").lower()
            if 1 < len(coord) <= len(str(self.grid.cols)) + 1:
                break
            print("Bad length. Coordinate must be of the form a10 or J1")
        return coord

    def damage_ship_and_update_location_data(self, coord, col, row, enemy_grid) -> str:
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
            exit(1)

    # Print a grid. If coord is in the s, print location_data, otherwise print ~
    def print_grid(self) -> None:

        # Print offset, and col headers, considering num cols could change
        print(' ' * (len(str(self.grid.cols)) + 1), end="")
        print(*[chr(c+97).upper() for c in range(self.grid.cols)], end="")

        for r in range(self.grid.rows):

            # Print row headers, and offset considering num rows could change
            offset = ' ' * ((len(str(self.grid.rows))) - len(str(r+1)))
            print(f"\n{r+1} " + offset, end="")

            for c in range(self.grid.cols):
                coord = str(c)+str(r)
                location_info = self.grid.shots_dict.get(coord, "~")

                # If printing player grid, we should print first letter of ship where ship not hit yet
                if coord not in self.grid.shots_dict and (c, r) in self.grid.ship_locations and not self.is_computer:
                    for ship in self.grid.grid_ships:
                        if (c, r) in ship.get_coords():
                            location_info = ship.get_name()[0]

                print(location_info + " ", end="")
        print("\n")

    @staticmethod
    def read_dimensions(data_file) -> list:
        with open(data_file) as file:
            return json.loads(file.read())[0]

    @staticmethod
    def read_ships(data_file) -> list:
        with open(data_file) as file:
            return json.loads(file.read())[1:]