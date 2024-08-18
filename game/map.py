import json

from enum import Enum
from types import SimpleNamespace

from game.coordinates import Coordinates
from game.location import Location


class Direction(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4


class Map:
    def __init__(self, filename):
        self.locations: list[Location] = []
        self.player_position: Coordinates = Coordinates(0, 0)

        self.load_map(filename)

    def load_map(self, filename: str) -> None:
        file_path = f"data/{filename}"
        try:
            with open(file_path) as file:
                raw_text = file.read()

            try:
                locations = json.loads(raw_text)["locations"]
                for json_location in locations:
                    location = Location(json_location["description"], Coordinates(json_location["x"], json_location["y"]))
                    self.locations.append(location)
            except:
                print("Wrong json format")
        except:
            print("Problem with access for file")

    def get_location(self, position) -> Location | None:
        for location in self.locations:
            if location.position == position:
                return location
        return None

    def possible_moves(self, current_position: Coordinates) -> list[Direction] | None:
        possible_moves = []
        for location in self.locations:
            if location.position == Coordinates(current_position.get_x() + 1, current_position.get_y()):
                possible_moves.append(Direction.NORTH)
            elif location.position == Coordinates(current_position.get_x(), current_position.get_y() + 1):
                possible_moves.append(Direction.EAST)
            elif location.position == Coordinates(current_position.get_x() - 1, current_position.get_y()):
                possible_moves.append(Direction.SOUTH)
            elif location.position == Coordinates(current_position.get_x(), current_position.get_y() - 1):
                possible_moves.append(Direction.WEST)
        if not possible_moves:
            return None
        else:
            return possible_moves

    def move_player(self, direction: Direction) -> bool:
        possible_moves = self.possible_moves(self.player_position)
        if possible_moves:
            if direction in possible_moves:
                if direction == Direction.NORTH:
                    self.player_position.move_x(1)
                elif direction == Direction.EAST:
                    self.player_position.move_y(1)
                elif direction == Direction.SOUTH:
                    self.player_position.move_x(-1)
                elif direction == Direction.WEST:
                    self.player_position.move_y(-1)
                return True
        return False
