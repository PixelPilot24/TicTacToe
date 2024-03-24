import random


class Player:
    @staticmethod
    def computer_turn(fields):
        possible_moves_list = []

        for i in range(9):
            if fields[i] == " ":
                possible_moves_list.append(i)

        computer_choice = random.choice(possible_moves_list)
        print("O(Computer) ist am Zug: " + str(computer_choice))
        return computer_choice

    @classmethod
    def player_turn(cls, player, player_num, fields) -> list:
        if player:
            field = input("X(Spieler 1) ist am Zug: ")
            return [field, 0]
        elif not player and player_num == 2:
            field = input("O(Spieler 2) ist am Zug: ")
            return [field, 1]
        else:
            field = cls.computer_turn(fields)
            return [field, 1]
