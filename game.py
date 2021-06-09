import player
import computer


class Game:
  # class attributes are static
  def __init__(self):
    # instance attributes are instance vars 
    # board is empty
    self.board = []
    for i in range(9):
      self.board.append(0)
  
  def displayBoard(self):
    
    print()
    print("-------------")
    #through all rows
    for i in range(3):
      #within each row (the cols)
      for j in range(3):
        char = self.board[3 * i + j]
        # print space instead of 0 for empty spots
        if char == 0:
          char = ' '
        # print the char and appropriate spacers ( or lack of)
        if j == 0:
          print ("| ", end = "")
        print(char, end = "")
        print("", end = " | ")
      print() #newline at end of each row
      print("-------------")
    print()

  # sets the piece at that position to 'X' or 'O'
  def setBoard(self, position, letter):
    # as long as nothing already there
    if self.board[position] == 0:
      self.board[position] = letter;
      return True
    else:
      return False

  # returns 0, 'X' or 'O'
  def checkSomeoneWon(self):
    # check both player's and computer's win states
    participants = [player.Player.letter, computer.Computer.letter]
    for ltr in participants:
      #check rows
      for i in range(3):
        inRow = 0
        for j in range(3):
          if self.board[3 * i + j] == ltr:
            inRow += 1
        if inRow == 3:
          return ltr
      #check cols
      for i in range(3):
        inCol = 0
        for j in range(3):
          if self.board[i + 3 * j] == ltr:
            inCol += 1
        if inCol == 3:
          return ltr
      #check diagonals
      diags = [[0,4,8],[2,4,6]]
      for diag in diags:
        inDiag = 0
        for pos in diag:
          if self.board[pos] == ltr:
            inDiag += 1
        if inDiag == 3:
          return ltr
    # exhausted all searches,
    # at this point return 'N' for "no", no one has won yet
    # print("got here, no one won yet")
    return 'N'
  
  def boardFull(self):
    # search board for empty spots
    for ltr in self.board:
      if ltr == 0:
        # empty spot found, so not full yet
        return False
    # must be full, no empty found
    return True   