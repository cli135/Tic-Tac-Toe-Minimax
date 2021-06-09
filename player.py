class Player:
  letter = 'X'
  def __init__(self):
    pass
  # fetches move from input. Then modifies board
  def makeMove(self, game):
    moved = False
    while not moved:
      # gather user's choice
      position = self.get_input()
      # try to move there
      moved = game.setBoard(int(position), Player.letter)

  def get_input(self):
    valid = False
    while not valid:
      try:
        position = int(input("Enter an integer 1-9: "))
        # only reaches this point if no exception thrown i think
        if not (position >= 1 and position <= 9):
          raise Exception()
        valid = True
      except ValueError:
        print("Not an int, please try again:")
      except Exception:
        print("Not between 1-9, please try again")
    # for user convenience
    conversion = {1: 6, 2: 7, 3: 8, 4: 3, 5: 4, 6: 5, 7: 0, 8: 1, 9: 2}
    return conversion[position]
