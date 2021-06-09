import random
import copy
import player

class Computer:
  letter = 'O'
  def __init__(self):
    pass
  # contains move logic. Modifies board
  def makeMove(self, game):
    #self.earliestMove(game)
    #self.randomMove(game)
    self.minimax(game, Computer.letter, True)

  # earliest on
  def earliestMove(self, game):
    for i in range(9):
      moved = game.setBoard(i, Computer.letter)
      if moved: return

  # pseudo random pick
  def randomMove(self, game):
    moved = False
    while not moved:
      #random choice for now
      position = int(random.random() * 9)
      # try to move there
      moved = game.setBoard(position, Computer.letter)

  # recursive tree decision algorithm, with game theory idea:
  # +1 for O, -1 for X, 0 for tie
  # consider the worst case scenario for the computer, because the computer assumes the opponent will play optimally to their own advantage. So the computer will too.

  #letterTurn is who is playing: O maximizes, X minimizes
  def minimax(self, game, letterTurn, firstCall): # -> a score -1, 0, 1
    # base case: check if game over:
    if 'N' != game.checkSomeoneWon() or game.boardFull():
      winner = game.checkSomeoneWon()
      # this if-elif-else is a little shaky because
      # haven't established mutual exclusive from this code
      # tie case
      if ('N' == winner) and game.boardFull():
        return 0 # 0 score in tie
      # else, someone won
      elif Computer.letter == winner:
        return 1
      else:
        if not 'X' == winner:
          print("---check the if-elif-else in computer.py, the base case is not airtight", winner)
        return -1 # Player won
    
    ### recursive case:
    # return the score of this game based on its possible moves
    # check possibilities
    possibleMoves = {} # empty spots
    # tracking num of possible moves
    num = 0
    for i in range(9):
      # check for zeroes (empty spots)
      if game.board[i] == 0:
        # hypothetical copy of game with possible move
        hypoGame = copy.deepcopy(game)
        moved = hypoGame.setBoard(i, letterTurn)
        if not moved: print("Error, should have moved to empty spot")
        # toggle turns
        nextLtr = 'N'
        if Computer.letter == letterTurn:
          nextLtr = player.Player.letter
        else:
          nextLtr = Computer.letter
        # score the possible move recursively
        # False means not the first call anymore, 
        # since on the first call we want to actually make
        # the move. The deeper calls we are just calculating
        # scores.
        score = self.minimax(hypoGame, nextLtr, False)
        possibleMoves[i] = score
        num += 1
    
    # minimize (X player) or maximize (O computer) the score
    bestMove = -1
    if Computer.letter == letterTurn:
      # https://www.kite.com/python/answers/how-to-find-the-max-value-in-a-dictionary-in-python
      maxMove = max(possibleMoves, key = possibleMoves.get)
      bestMove = maxMove
    else:
      # error check / assert
      if player.Player.letter != letterTurn:
        print("letter turn is not", player.Player.letter, "but is", letterTurn)
      minMove = min(possibleMoves, key = possibleMoves.get)
      bestMove = minMove
    if not firstCall:
      return possibleMoves[bestMove] # the best score
    else:
      # make the best move
      if Computer.letter != letterTurn:
        print("letterTurn is not", Computer.letter, "it is", letterTurn, ", but we should be only doing minimax for the computer")
      moved = game.setBoard(bestMove, letterTurn)
      if not moved:
        print("Could not move to bestMove:", bestMove, "in computer.py")





