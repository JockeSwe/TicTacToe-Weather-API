import pygame
from weatherApi import weather_list, first_digit

class pygameProgram:
  def __init__(self, width, height):
    pygame.init()  # Initialize pygame
    self.width = 1000 # each box is 100px wide with 100px to leave out on the sides
    self.height = 1000 # each box is 100px tall with 100px to leave out on top and bottom
    self.screen = pygame.display.set_mode((width, height)) # images depending on weather condition
    self.xCord = self.yCord = 100 # x and y cordinates for square
    
    self.playerImg = pygame.image.load("Images/playerMarker.png")
    self.playerImg = pygame.transform.scale(self.playerImg, (80,80))
    self.initImage()

  def initImage(self):
    self.weatherImage = pygame.image.load(f"Images/"+weather_list[first_digit])  # loads the image into a variable from a list in weatherApi.py using pictures stored in folder 'Images/' 
    self.weatherImage = pygame.transform.scale(self.weatherImage, (500,500)) # Make the image 500x500px
    self.screen.blit(self.weatherImage, (0, 0))  # prints image to screen (Test)
    self.draw()

  def drawSquare(self): # Draws the 3x3 tic tac toe grid
   for x in range(3): #Loop for White 3x3 square
     for y in range(3):
       pygame.draw.rect(self.screen, (0,0,0), pygame.Rect(self.xCord + x*100, self.yCord + y*100, 100, 100))

   for x in range(3): # Loop for Black 3x3 square inside of the black square
    for y in range(3):
       pygame.draw.rect(self.screen, (255,255,255), pygame.Rect(self.xCord + x*110, self.yCord + y*110, 80, 80))
    pygame.display.flip()  # Updates display

  def draw(self): # Draws background image + the square
    self.screen.blit(self.weatherImage, (0, 0))
    self.drawSquare()
    pygame.display.flip()
# ----------- When a move has been played in main.py play() put a picture in the right square -------
  
  def imageMove(self, playing, playPiece): 
    startCount = 1
    print(f"imagemove playing {playPiece}")
    if playing == 0: # If the player is playing
       for x in range(3): # Put a picture on the correct spot
        for y in range(3):
          while startCount == playPiece:
             self.screen.blit(self.playerImg, (self.yCord + y*110, self.xCord + x*110))
             print("playerimg")
             """
             # Switch x and y to make the board go
             123
             345
             678
             instead of                  
             147
             258
             369
             """

             print("Image has been printed")
             startCount+=1
             break
          startCount+=1

pyG = pygameProgram(1000,1000)
pyG.initImage() # run initImage before drawSquare to get the image in the background
pyG.drawSquare() # run drawSquare after initImage to get the square in the foreground
#self.screen.blit(weatherImage, (0, 0))
pygame.display.flip()

# ----------------- NEED A LOOP FOR PYGAME, INCORPORATE PYGAME INTO MAIN.PY SO SUMTHing ---------