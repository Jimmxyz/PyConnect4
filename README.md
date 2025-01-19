# PyConnect4
A Connect 4 for CLI (Or Python Calculator)

## Features
Exemple of a game:
```
[Connect 4] Move 11 (O turn)
[0][1][2][3][4][5][6][7][8][9]
[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
[ ][ ][O][ ][ ][ ][ ][ ][ ][ ]
[ ][ ][X][O][X][X][ ][ ][ ][ ]
[X][O][X][X][O][O][ ][ ][ ][ ]
```
>[!NOTE]
>The 'O' and 'X' are colored if you play it in a CLI (not compatible with Python Calculator)

**Other features :**
- The game can detect an alignment of 4 vertical, horizontal or diagonal pieces (and detect when the grid is full).
- When the grid is full, a draw is declared.
- The game does not crash when you type an invalid entry and will ask you again.
- The numbers at the top disappear when an 'X' or an 'O' is placed in that column.

## How to play
- Type a number between 0 and 9 to choose the column where your 'X' or 'O' will be placed
- Type 'e' to exit the game

## Credit
Created by me (@Jimmxyz on Github)

The library termcolor is used (https://github.com/termcolor/termcolor)

## License
This Program is under the MIT License
This means that anyone can use this code as they wish
