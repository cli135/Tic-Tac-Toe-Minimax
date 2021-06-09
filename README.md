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
1. "Coding Challenge 154: Tic Tac Toe AI with Minimax Algorithm" by The Coding Train
https://youtu.be/trKjYdBASyQ?t=109
--main inspiration for the minimax alg. This video has a great whiteboard explanation from 1:49 - 8:20 of minimax.
https://realpython.com/python3-object-oriented-programming/#define-a-class-in-python
https://openbookproject.net/thinkcs/python/english3e/classes_and_objects_I.html
https://dzone.com/articles/python-class-attributes-vs-instance-attributes
https://www.geeksforgeeks.org/class-instance-attributes-python/
2. https://www.kite.com/python/answers/how-to-find-the-max-value-in-a-dictionary-in-python
3. https://realpython.com/iterate-through-dictionary-python/#iterating-through-items
4. https://stackoverflow.com/questions/24575680/new-lines-inside-paragraph-in-readme-md
5. https://stackoverflow.com/questions/24575680/new-lines-inside-paragraph-in-readme-md
6. https://stackoverflow.com/questions/7979623/why-is-assignment-to-this-not-allowed-in-java
7. https://stackoverflow.com/questions/44814719/can-both-the-values-and-keys-of-a-dictionary-be-integers/44814737
8. https://stackoverflow.com/questions/5424716/how-to-check-if-string-input-is-a-number
9. https://stackoverflow.com/questions/3106689/pointers-in-python
10. https://stackoverflow.com/questions/47561840/python-how-can-i-separate-functions-of-class-into-multiple-files/47562412
11. https://stackoverflow.com/questions/43715953/nameerror-class-name-is-not-defined/43716037
12. https://www.w3schools.com/python/python_ref_dictionary.asp
13. https://www.w3schools.com/python/gloss_python_raise.asp
14. https://docs.python.org/3/library/random.html
15. https://www.geeksforgeeks.org/print-without-newline-python/
16. https://www.guru99.com/print-without-newline-python.html
17. https://www.tutorialsteacher.com/python/public-private-protected-modifiers
18. https://realpython.com/python-return-statement/#:~:text=In%20general%2C%20a%20function%20takes,value%2C%20either%20explicit%20or%20implicit.

# Code details:
The four files are main.py, game.py, player.py, and computer.py.
1. main.py guides the game flow. It creates a game, player, and computer, and uses a while loop to keep the game going.
2. game.py has the game board. This class adds moves to the board and checks who has won (or if it's a tie).
3. player.py has the input-output, where the user can enter their choice.
4. computer.py has the minimax algorithm, which looks ahead multiple moves and chooses the best possible one.
