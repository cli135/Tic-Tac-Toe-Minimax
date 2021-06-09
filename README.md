# Tic-Tac-Toe-Minimax
Tic-tac-toe in the terminal, player vs. computer! The computer runs on minimax algorithm to play optimally

# How to play:
The player is 'X' and the computer is 'O'.
Your move is first. To select your move, please refer
to the keypad below or your computer's keypad) and type
the corresponding number. Good luck :)

| 7 | 8 | 9 |  
| 4 | 5 | 6 |  
| 1 | 2 | 3 |  

First move takes ~10 seconds for the computer to figure out its move

# Credits / sources: WIP
Main sources:  
1. "Coding Challenge 154: Tic Tac Toe AI with Minimax Algorithm" by The Coding Train  
https://youtu.be/trKjYdBASyQ?t=109  
--main guide for coding minimax algorithm. This video has a great explanation from 1:49 - 8:20.  
2. https://realpython.com/python3-object-oriented-programming/#define-a-class-in-python  
--main guide on how to do object-oriented-programming in Python  

Other sources:  
4. https://openbookproject.net/thinkcs/python/english3e/classes_and_objects_I.html  
5. https://dzone.com/articles/python-class-attributes-vs-instance-attributes  
6. https://www.geeksforgeeks.org/class-instance-attributes-python/  
7. https://www.kite.com/python/answers/how-to-find-the-max-value-in-a-dictionary-in-python  
8. https://www.w3schools.com/python/gloss_python_raise.asp  
9. https://docs.python.org/3/library/random.html  
10. https://www.guru99.com/print-without-newline-python.html  
11. https://www.tutorialsteacher.com/python/public-private-protected-modifiers  
12. StackOverFlow was a very useful resource for Python syntax.  

# Code details:
The four files are main.py, game.py, player.py, and computer.py.
1. main.py guides the game flow. It creates a game, player, and computer, and uses a while loop to keep the game going.
2. game.py has the game board. It adds 'X' and 'O' to the board and checks who has won (or if it's a tie).
3. player.py has the input-output, which allows the user to enter their choice.
4. computer.py has the minimax algorithm, which looks ahead multiple moves and chooses the best possible one for the computer.
