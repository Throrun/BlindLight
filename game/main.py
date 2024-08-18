from player import Player
from map import Map, Direction


def main():
    player = Player("hero")
    game_map = Map("testMap.json")
    print(game_map.player_position)


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
