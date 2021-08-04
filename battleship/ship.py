class Ship:
    """
    Representation of the Ship class
    """
    def __init__(self,
                 name="",
                 health="",
                 coords=""):

        self.name: str = name
        self.health: int = health
        self.coords: list[int] = coords

    def get_name(self) -> None:
        return self.name

    def get_coords(self) -> None:
        return self.coords

    def set_coords(self, coords) -> None:
        self.coords = coords

    def decrement_health(self) -> None:
        self.health -= 1
        if self.health == 0:
            print(f"You sunk my {self.name}!")