# Changelog
Alle nennenswerten Änderungen an diesem Projekt werden in dieser Datei dokumentiert.

## [1.0.0] - 09.04.2024

### Added
+ [tictactoe.py](https://github.com/PixelPilot24/TicTacToe/blob/1.0.0/tictactoe.py)
  + [start_game()](https://github.com/PixelPilot24/TicTacToe/blob/1.0.0/tictactoe.py#L82) eine weitere except
  Anweisung hinzugefügt für die Zahlen die kleiner als 1 und größer als 9 sind 
  + nach dem Abschluss eines Spiels, gibt es die Möglichkeit das Spiel von vorne anzufangen
  [(Zeile 85 bis 92)](https://github.com/PixelPilot24/TicTacToe/blob/1.0.0/tictactoe.py#L85)

### Changed
+ [tictactoe.py](https://github.com/PixelPilot24/TicTacToe/blob/1.0.0/tictactoe.py)
  + [show_boars()](https://github.com/PixelPilot24/TicTacToe/blob/1.0.0/tictactoe.py#L32) die print Ausgabe
  wurde verändert
  + [start_game()](https://github.com/PixelPilot24/TicTacToe/blob/1.0.0/tictactoe.py#L67) die print Ausgabe
  wurde verändert
  + [update_board()](https://github.com/PixelPilot24/TicTacToe/blob/1.0.0/tictactoe.py#L45) die Eingabe ist
  nicht mehr 0 bis 8, sondern 1 bis 9. Deswegen muss field - 1.
+ [player.py](https://github.com/PixelPilot24/TicTacToe/blob/1.0.0/player.py)
  + [computer_turn()](https://github.com/PixelPilot24/TicTacToe/blob/1.0.0/player.py#L11) die freien Felder
  die bestimmt werden, mussten um eins erhöht werden
+ bei allen Methoden die Parameter benötigen, wurden die Typen hinzugefügt und, falls es einen return Wert gibt,
wurde dieser auch hinzugefügt