class Ship:
    """
    Representation of the Ship class
    """
    def __init__(self,
                 name="",
                 health="",
                 coords=""):

        self.name = name
        self.health = health
        self.coords = coords

    def get_coords(self) -> None:
        return self.coords

    def get_name(self) -> None:
        return self.name

    def set_coords(self, coords) -> None:
        self.coords = coords

    # If the health is 0, the ship was sunk
    def decrement_health(self) -> None:
        self.health -= 1
        if self.health == 0:
            print(f"You sunk my {self.name}!")