import game
import player
import computer

def main():
  

  welcome()

  # main loop of game
  playAgain = 'y';
  while 'y' == playAgain:
    print("New game:")
    # set up game and players
    curGame = game.Game()
    p1 = player.Player()
    c1 = computer.Computer()
    gameOver = False
    turn = True # represents player, False represents computer
    while not gameOver:
      # either player or computer makes a move
      if turn:
        #display board
        curGame.displayBoard()
        #let player move
        p1.makeMove(curGame)
      else:
        # comp moves
        c1.makeMove(curGame)

      # check if game over
      if ('N' != curGame.checkSomeoneWon()) or curGame.boardFull():
        gameOver = True
        break
      
      # taking turns
      turn = not turn
    
    # game now over
    curGame.displayBoard()
    winner = curGame.checkSomeoneWon()

    # tie case
    if (winner == 'N') and (curGame.boardFull()):
      print("Tie! Good game to both player and computer.")
    # else, someone won
    else:
      print("Congrats to " + curGame.checkSomeoneWon() + ", they won!")
    
    playAgain = input("Play again? y/n: ")
  print("Thanks for playing!")


#helper method
def welcome():
  print("Welcome to Tic-Tac-Toe!")
  print('\n')
  print("You are 'X' and the computer is 'O'.")
  print("Your move is first. To select your move, please refer to the keypad below or your computer's keypad) and type the corresponding number. Good luck :)")
  print('\n')
  print("First move takes ~10 seconds for the computer to figure out its move")
  displayBoardInstructions()

def displayBoardInstructions():
    spaces = [7,8,9,4,5,6,1,2,3]
    idx = 0
    print()
    print("-------------")
    #through all rows
    for i in range(3):
      #within each row (the cols)
      for j in range(3):
        # print the char and appropriate spacers ( or lack of)
        if j == 0:
          print ("| ", end = "")
        print(spaces[idx], end = "")
        idx += 1
        print("", end = " | ")
      print() #newline at end of each row
      print("-------------")
    print()

main();