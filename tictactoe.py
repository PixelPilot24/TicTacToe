from player import Player
from win import Win


class Board:
    def __init__(self):
        self.fields = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.player_list = ["Spieler 1", "Spieler 2", "Computer"]
        self.round_num = 0

    def init_game(self):
        while True:
            player_num = input("Gib die Anzahl an Spielern an oder \"beenden\": ")
            if player_num == "beenden":
                print("Spiel beendet")
                break

            try:
                player_num = int(player_num)

                if 1 <= player_num <= 2:
                    if player_num == 1:
                        self.start_game(1)
                    else:
                        self.start_game(2)
                    break
                else:
                    print("Die Anzahl der Spieler muss 1 oder 2 sein.")
            except ValueError:
                print("Die Anzahl an Spielern muss eine Zahl sein")

    def show_board(self):
        print(self.fields[0] + "|" + self.fields[1] + "|" + self.fields[2])
        print(self.fields[3] + "|" + self.fields[4] + "|" + self.fields[5])
        print(self.fields[6] + "|" + self.fields[7] + "|" + self.fields[8])

    def update_board(self, field, player_int) -> list:
        if player_int == 0:
            player_var = "X"
            player_bool = True
        else:
            player_var = "O"
            player_bool = False

        field = int(field)
        result = []

        if 0 <= field <= 8:
            if self.fields[field] == " ":
                self.fields[field] = player_var
                self.round_num += 1
                self.show_board()
                result = [not player_bool, True]
            elif self.fields[field] != " ":
                print("Feld besetzt")
                result = [player_bool, True]

            if Win.display_winner(self.fields, self.player_list[1]):
                result = [player_bool, False]
            elif self.round_num == 9:
                print("Spiel unentschieden")
                result = [player_bool, False]

            return result
        else:
            print("Die eingegeben Wert muss zwischen 0 und 8 liegen")

    def start_game(self, player_num):
        print("0|1|2\n3|4|5\n6|7|8")
        player_bool = True
        del self.player_list[player_num]

        while True:
            input_info = Player.player_turn(player_bool, player_num, self.fields)

            try:
                bool_list = self.update_board(input_info[0], input_info[1])
                player_bool = bool_list[0]

                if not bool_list[1]:
                    break
            except ValueError:
                print("Die eingegeben Wert muss eine Zahl sein")


if __name__ == "__main__":
    Board.init_game(Board())
