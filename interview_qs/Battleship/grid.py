from ship import Ship
import random

class Grid:
    """
    Representation of the Grid class. A Grid has rows, cols, a list of ships, a list of ship locations, and a dictionary of shots
    """
    def __init__(self,
                 rows="",
                 cols=""):

        self.rows: int = rows
        self.cols: int = cols
        self.grid_ships: list[Ship] = []
        self.ship_locations: list[list[int]] = []
        self.shots_dict: dict = {}

    def build_ships(self, ship_data) -> None:
        for ship in ship_data:
            self.grid_ships.append(Ship(name=ship["name"], health=ship["health"]))

    def randomly_set_ship_locations(self) -> None:
        for ship in self.grid_ships:
            ship_coords = self.build_ship_coordinates(ship)

            # Set this ship's coords, and add them to ship locations
            ship.set_coords(ship_coords)
            for coord in ship_coords:
                self.ship_locations.append(coord)

    def build_ship_coordinates(self, ship) -> list:
        while True:
            # Randomly choose a coordinate on the grid, and randomly choose orientation
            col, row = random.randrange(self.cols), random.randrange(self.rows)
            vertical = random.choice([True, False])

            # Build ship_coords using ship health
            ship_coords = []
            for i in range(ship.health):
                ship_coords.append((col, row))
                if vertical:
                    row += 1
                if not vertical:
                    col += 1

            if self.ship_coords_in_grid_and_not_occupied(ship_coords):
                break

        return ship_coords

    def ship_coords_in_grid_and_not_occupied(self, ship_coords) -> bool:
        for (col, row) in ship_coords:
            if col not in range(self.cols) or row not in range(self.rows):
                return False
            if (col, row) in self.ship_locations:
                return False
        return True

    def attack_not_in_shots_dict(self, coord, col, row, is_computer) -> bool:
        if str(col)+str(row) not in self.shots_dict:
            return True
        # Let player know they already shot here
        if not is_computer:
            print(f"{coord} has already been shot.")
        return False

    def attack_inside_grid(self, coord, col, row) -> bool:
        if col in range(self.cols) and row in range(self.rows):
            return True
        print(f"{coord} is outside the grid bounds.")
        return False

    def all_ships_sunk(self) -> bool:
        # If a ship has health > 0, not all ships are sunk
        for ship in self.grid_ships:
            if ship.health > 0:
                return False
        return True