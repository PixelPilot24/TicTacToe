class Win:
    @staticmethod
    def check_win(fields) -> str:
        finish_list = [
            fields[0] + fields[1] + fields[2],
            fields[3] + fields[4] + fields[5],
            fields[6] + fields[7] + fields[8],
            fields[0] + fields[3] + fields[6],
            fields[1] + fields[4] + fields[7],
            fields[2] + fields[5] + fields[8],
            fields[0] + fields[4] + fields[8],
            fields[2] + fields[4] + fields[6]
        ]

        for i in finish_list:
            if i == "XXX":
                return "X"
            elif i == "OOO":
                return "O"

    @classmethod
    def display_winner(cls, fields, o_player) -> bool:
        win_str = cls.check_win(fields)

        if win_str == "X":
            print("X(Spieler 1) hat gewonnen!")
            return True
        elif win_str == "O":
            print("O(" + o_player + ") hat gewonnen!")
            return True

        return False
