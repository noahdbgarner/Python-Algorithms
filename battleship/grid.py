from ship import Ship
import random

class Grid:
    """
    Representation of the Grid class.
    """
    def __init__(self,
                 rows="",
                 cols="",
                 ships="",
                 is_computer=""):

        self.rows = rows
        self.cols = cols
        self.ships = ships
        self.is_computer = is_computer
        self.grid_ships = []
        self.ship_locations = []
        self.shot_dict = {}

    # Done: For each ship in ships, create a ship object, and add it to the grid_ships list
    def make_ships(self) -> None:
        for ship_info in self.ships:
            self.grid_ships.append(Ship(name=ship_info["name"], health=ship_info["health"]))

    # Done: Randomly assigns each ship in ships a list of coords on the grid
    def randomly_place_ships(self) -> None:
        for ship in self.grid_ships:
            # Keep going until a ship can be placed
            while True:
                # Randomly choose a coordinate to start, and randomly choose orientation
                col, row = random.randrange(self.cols), random.randrange(self.rows)
                vertical = random.choice([True, False])
                # Init ship_coords list
                ship_coords = []

                # Build ship_coords using the health of the ship
                for i in range(ship.health):
                    ship_coords.append((col, row))
                    if vertical:
                        row+=1
                    if not vertical:
                        col+=1

                # If check_coords returns true, break, otherwise try another placement
                if self.check_coords(ship_coords):
                    break

            # If we made it here, the ship can be placed, and it can be added to ship locations
            ship.set_coords(ship_coords)
            for coord in ship_coords:
                self.ship_locations.append(coord)

    def check_coords(self, ship_coords) -> bool:
        # Check coords
        for col, row in ship_coords:
            # Are In bounds of grid
            if col not in range(self.cols) or row not in range(self.rows):
                return False
            # Are not occupied by another ship
            if (col, row) in self.ship_locations:
                return False
        return True

    # Done: Checks if the shot has already been fired
    def shot_not_in_shot_dict(self, coord, col, row, is_computer) -> bool:
        if str(col)+str(row) not in self.shot_dict:
            return True
        # Let player know they already shot here
        if not is_computer:
            print(f"{coord} has already been shot.")
        return False

    # Done: Check the coord is within grid bounds
    def shot_inside_grid(self, coord, col, row) -> bool:
        if col in range(self.cols) and row in range(self.rows):
            return True
        print(f"{coord} is outside the grid bounds.")
        return False

    # Done: Check if there is still a ship, otherwise all ships are sunk
    def all_ships_sunk(self) -> bool:
        for ship in self.grid_ships:
            if ship.health > 0:
                return False
        return True