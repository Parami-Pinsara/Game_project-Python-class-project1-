from Players_Class import Players
from prettytable import PrettyTable
import random

"""
Game class includes all the core processes to decide the winner
This class includes all the processes with 4 methods

1) roll_dices() method - Generate random values and saves in 3 global variables which are rolld1, rolld2, rolld3
2) rounds() method - Implement 3 rounds for each player and returns their ultimate total marks
3) score_table() method - Creates the score table to display
4) winner() method - returns the winner's same
"""

class Game:

    count_round = 0
    dice2_cities = ['CMB', 'TYK', 'NY', 'LON', 'ATN', 'SYN']        # dice2 values list
    dice3 = [True, False]                                           # dice3 values list
    rolld1 = 0                                        # global variable to save random value of dice1
    rolld2 =''                                        # global variable to save random value of dice2
    rolld3 = []                                       # global variable to save random value of dice3
    dic_players_total = { }                           # dictionary that stores player name with respected total mark

    def __init__(self):
        pass

    def roll_dices():

        dice1 = random.randint(1, 6)                    # generate random values for dice1
        dice2 = random.choice(Game.dice2_cities)        # generate random values for dice2
        dice3 = random.choice(Game.dice3)               # generate random values for dice3
        Game.rolld1 = dice1
        Game.rolld2 = dice2
        Game.rolld3 = dice3


    def rounds():

        total =0
        rounds = ["Round1", "Round2" , "Round3"]            # list with 3 rounds names
        Dic_play = { }
        total_mark = { }                                    #dictionary that saves total marks with player names in this method

        for i in range(len(Players.players_list)):          # loop that operates until all players are done playing

            player = Players.players_list[i]                # holds player name
            print(player)
            Dic_rnd = {}                                    # dictionary that includes results of 3 rounds

            for x in range (3):                             #loop that implemets 3 rounds

                enter = input(f"Press 'Enter ' to roll 3 dices for round{x + 1} :")     # take enter key as an input to rolla dice
                Game.roll_dices()                                                       # roll 3 dices per round

                if enter == '':

                    if Game.rolld3 == False:                # check if the dice 3 value i is False

                        Game.rolld1 *=  (-1)                # if so, converts the dice1 value to negative

                else:
                    print("Invalid Input")
                    exit()

                Round_list = [ str(Game.rolld1), Game.rolld2, str(Game.rolld3) ]        # this list saves 3 dices vales per round
                Dic_rnd[rounds[x]] = str(Round_list)

                total += Game.rolld1                                        # calcultes total marks
                total_mark.update({Players.players_list[i]: total})         # adding players with respected total mark to the dictionary

            print(Dic_rnd)
            total = 0
        print("\n----- Score Tbale -----")
        
        return total_mark

    def score_table():

        Game.dic_players_total = Game.rounds()

        table_r = PrettyTable()                                # creating a table



        table_r.field_names = ["Player", "Total Score"]        # defining table field values
        key_list = list(Game.dic_players_total.keys())
        value_list = list(Game.dic_players_total.values())

        
        for s in range(len(Players.players_list)):
            
            table_r.add_row([key_list[s], value_list[s]])       #adding values to table rows


        return table_r

    def winner():

        winner= max(Game.dic_players_total, key=Game.dic_players_total.get)     #take the player that has the maximum total mark
        return winner


