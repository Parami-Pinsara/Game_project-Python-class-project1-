""""This class includes the players name who are going to compete and the number of player that are going to play"""


class Players:
    players_list = []       # save the list of players in a list

    """Following method counts the number of players that is engaged to play at once."""

    def __init__(self):

        self.p = input("Enter the number of players :")     # take the number of players as an input

        for x in range(int(self.p)):

            n = input(f"Enter player{x + 1} name :")        # Tke players names as inputs

            Players.players_list.append(n)

