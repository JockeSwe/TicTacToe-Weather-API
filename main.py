# Tre i rad # med tillgång till något internet som t.ex väder # ta annan tre i rad pygame o ändra bakgrund
# Tre i rad random vart den ska placera, ingen smart AI
import random  # Import random
import pygame
import pygameCode  # Import pygameCode.py
import weatherApi # Import weatherApi.py

pygameCode.pygameProgram(1000, 1000)

class gameSystem:

  def __init__(self, playerName, botName):
    self.player = playerName
    self.bot = botName
    self.round = 0
    self.points = [0, 0]  # points[0] is player and points[1] is bot
    self.participantList = [playerName, botName]
    self.playing = random.randint(0,1) # randomizes if firstmove should be random otherwise self.playing changes in "def turn()" line 20
    self.winCondition = False
    self.boardDict = {i: False for i in range(1,10)} # Creates a dictionary where every number is False used for tictactoe number board

  def turn(self):  # different start orders depending on what the player answered
    if FirstMove == "player":
      print("player go first")
      self.playing = 0 # Player in participantList is 0
    elif FirstMove == "bot":
      print("bot go first")
      self.playing = 1 # Bot in participatingList is 1
    elif FirstMove == "random":
      print(f"{self.participantList[self.playing]} go first")

  #def score(self): # Keeps track of the score, it display PlayerPoint and BotPoint and potential ties

  #def checkWin(self): #Checks who won and adds a point
  #When win check, look who won and add a point to PlayerPoint or BotPoint
  def checkBoard(self):

    print("The possible moves are:") 
    for i in range(1,10): # Checks if the numer has been used, if not, print it as available
      if self.boardDict[i] == False:
        print(i)
    while True: # keeps looping when an invalid input has been given such as a used space or text
      self.playPiece = input("Which space would you like to put your piece?")
      self.playPiece = int(self.playPiece)
      print(f"{self.playPiece}, playPiece")
      if self.playPiece in range(1,10):
        if self.boardDict[self.playPiece] is False:  #if the number havent been played, break loop and make it played
          self.boardDict[self.playPiece] = True # the Piece has been used.
          print(f"boardDict boolean {self.boardDict[self.playPiece]} playPiece {self.playPiece}")
          break
      print("Invalid answer")

    #pygameCode.pygameProgram(100,100).imageMove(self.playing)
    pygameCode.pygameProgram(1000,1000).imageMove(self.playing, self.playPiece)


  def play(self):
    pygame.init()

    while self.winCondition == False:
      if self.playing == 0:
        pygame.display.flip()
        games.checkBoard()


      #write checkWin() inside of while loop to check if win
#  end


# -------------------------------------- Game ---------------------------------- #
# Who should move first
while True:
  FirstMove = input("Who should start? player, bot or random\n")
  if FirstMove.lower() in [
      "player", "bot", "random"
  ]:  #if the input doesnt match these three it should ask again
    break
  print("Invalid answer, player, bot or random!")
print("You chose", FirstMove.lower())

games = gameSystem("Jockin", "bot")

games.turn()
games.play()