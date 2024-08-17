import json

from enum import Enum
from types import SimpleNamespace

from game.location import Location


class Direction(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4


class Map:
    def __init__(self, filename):
        self.locations: Location = []
        self.player_position = (0, 0)
        self.load_map(filename)

    def load_map(self, filename: str) -> None:
        file_path = f"data/{filename}"
        try:
            with open(file_path) as file:  # TODO Try catch here
                raw_text = file.read()

            try:
                locations = json.loads(raw_text)["locations"]
                for json_location in locations:
                    location = Location(json_location["description"], (json_location["x"], json_location["y"]))
                    self.locations.append(location)
            except:
                print("Wrong json Format")
        except:
            print("Problem with access for file")

    def get_location(self,position):
        for location in self.locations:
            if location.position == position:
                return location
        return None
    def possible_moves(self):
        self.player_position
    def move_player(self, direction: Direction):
        current_position = self.player_position
        #  TODO Validation is it posible to move here?
        if direction == Direction.NORTH:
            self.player_position = (current_position[0] + 1, current_position[1])
        elif direction == Direction.EAST:
            self.player_position = (current_position[0], current_position[1] + 1)
        elif direction == Direction.SOUTH:
            self.player_position = (current_position[0] - 1, current_position[1])
        elif direction == Direction.WEST:
            self.player_position = (current_position[0], current_position[1] - 1)
