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

        self.name = name
        self.grid = grid
        self.is_computer = is_computer

    # Get player name
    def get_name(self) -> None:
        return self.name

    # Build grid, and place ships
    def build_grid_and_place_ships(self, datafile) -> None:
        dimensions = self.read_dimensions(datafile)
        ship_list = self.read_ships(datafile)

        self.grid = Grid(rows=dimensions["rows"], cols=dimensions["cols"], ships=ship_list, is_computer=self.is_computer)

        self.grid.make_ships()
        self.grid.randomly_place_ships()

    # PLayer chooses a coordinate to fire on, the coordinate is checked, and added to the shot_dict
    def attack(self, enemy_grid: Grid) -> None:
        while True:
            # Get the coordinate to attack on enemy grid
            coord = self.get_attack_coord(enemy_grid)

            # grab and adjust letter and number to row col with base 0
            col = int(ord(coord[0])) - 97
            row = int(coord[1:]) - 1

            # Check if not already shot, and within grid
            not_in_shot_dict = enemy_grid.shot_not_in_shot_dict(coord, col, row, self.is_computer)
            in_grid = enemy_grid.shot_inside_grid(coord, col, row)
            if not_in_shot_dict and in_grid:
                break

        # Let them know the coordinate was chosen
        print(f"{self.name} attacked {coord}!")

        # TODO: Refactor - If a hit, decrement health, and update location_data in shot_dictionary
        location_data = "M"
        if (col, row) in enemy_grid.ship_locations:
            location_data = "H"
            print(f"{coord} was a hit!")
            # Find the ship that was hit, and decrement it's health
            for ship in enemy_grid.grid_ships:
                if (col, row) in ship.get_coords():
                    ship.decrement_health()
        if location_data == "M":
            print(f"{coord} missed!")

        # TODO: Refactor - Check if game over after attack
        if enemy_grid.all_ships_sunk():
            print(f"{self.name} wins!")
            exit(1)

        # add the shot to the shot_dict
        enemy_grid.shot_dict[str(col) + str(row)] = location_data

    # Drops ship data and returns {col, row} data
    def read_dimensions(self, data_file) -> list:
        with open(data_file) as file:
            return json.loads(file.read())[0]

    # Drops the {col, row} data and returns list of ship data
    def read_ships(self, data_file) -> list:
        with open(data_file) as file:
            return json.loads(file.read())[1:]

    def get_attack_coord(self, enemy_grid) -> str:
        # Computer defaults to random char from a to enemy_grid.cols inclusive, and 1 tp enemy_grid.rows
        coord = chr(random.randrange(97, 97 + enemy_grid.cols)) + str(random.randint(1, enemy_grid.rows))
        if not self.is_computer:
            coord = input("Choose a coordinate to fire on: ").lower()
        return coord

    # Print a grid. If coord is in the shot_dict, print location_data, otherwise print ~
    def print_grid(self) -> None:

        # Print offset, and col headers, considering that num cols could change
        print(' ' * (len(str(self.grid.cols)) + 1), end="")
        print(*[chr(c+97).upper() for c in range(self.grid.cols)], end="")

        for r in range(self.grid.rows):

            # Print row headers, and offset considering num rows could change
            offset = ' ' * ((len(str(self.grid.rows))) - len(str(r+1)))
            print(f"\n{r+1} " + offset, end="")
            for c in range(self.grid.cols):
                coord = str(c)+str(r)
                location_info = self.grid.shot_dict.get(coord, "~")

                # If printing player grid, we should print first letter of ship where ship not hit yet
                if coord not in self.grid.shot_dict and (c, r) in self.grid.ship_locations and not self.is_computer:
                    for ship in self.grid.grid_ships:
                        if (c, r) in ship.get_coords():
                            location_info = ship.get_name()[0]
                print(location_info + " ", end="")
        print("\n")