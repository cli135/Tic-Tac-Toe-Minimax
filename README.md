# Tic-Tac-Toe-Minimax
Tic-tac-toe in the terminal, player vs. computer! The computer runs on minimax algorithm to play optimally

# How to play:
You are 'X' and the computer is 'O'.
Your move is first. To select your move, please refer \n
to the keypad below or your computer's keypad) and type \n
the corresponding number. Good luck :)

First move takes ~10 seconds for the computer to figure out its move

# Credits / sources: WIP
1. "Coding Challenge 154: Tic Tac Toe AI with Minimax Algorithm" by The Coding Train
https://youtu.be/trKjYdBASyQ?t=109
--main inspiration for the minimax alg. This video has a great whiteboard explanation from 1:49 - 8:20 of minimax.

--python syntax sources below
2. https://www.kite.com/python/answers/how-to-find-the-max-value-in-a-dictionary-in-python
3. 

# Code details:
The four files are main.py, game.py, player.py, and computer.py.
main.py guides the game flow. It creates a game, player, and computer, and uses a while loop to keep the game going.
game.py has the game board. This class adds moves to the board and checks who has won (or if it's a tie).
player.py has the input-output, where the user can enter their choice.
computer.py has the minimax algorithm, which looks ahead multiple moves and chooses the best possible one.
