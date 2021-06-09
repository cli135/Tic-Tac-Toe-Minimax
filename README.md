# Tic-Tac-Toe-Minimax
Tic-tac-toe in the terminal, player vs. computer! The computer runs on minimax algorithm to play optimally

# How to play:
The player is 'X' and the computer is 'O'.
Your move is first. To select your move, please refer
to the keypad below or your computer's keypad) and type
the corresponding number. Good luck :)

-------------
| 7 | 8 | 9 | 
-------------
| 4 | 5 | 6 | 
-------------
| 1 | 2 | 3 | 
-------------

First move takes ~10 seconds for the computer to figure out its move

# Credits / sources: WIP
1. "Coding Challenge 154: Tic Tac Toe AI with Minimax Algorithm" by The Coding Train
https://youtu.be/trKjYdBASyQ?t=109
--main inspiration for the minimax alg. This video has a great whiteboard explanation from 1:49 - 8:20 of minimax.
2. https://www.kite.com/python/answers/how-to-find-the-max-value-in-a-dictionary-in-python
--python syntax source used in computer.py
3. 

# Code details:
The four files are main.py, game.py, player.py, and computer.py.
1. main.py guides the game flow. It creates a game, player, and computer, and uses a while loop to keep the game going.
2. game.py has the game board. This class adds moves to the board and checks who has won (or if it's a tie).
3. player.py has the input-output, where the user can enter their choice.
4. computer.py has the minimax algorithm, which looks ahead multiple moves and chooses the best possible one.
