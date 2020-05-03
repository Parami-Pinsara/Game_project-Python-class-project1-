from Players_Class import Players
from Game_build_class import Game


if __name__ == '__main__':


    Players()
    Game()

    print(Game.score_table())
    print("\n")

    print(f"Congartulations! {Game.winner()}\n You won the Game.")
