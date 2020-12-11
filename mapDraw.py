import pygame
import numpy as np

defualtButtonColor = (0, 150, 150, 150)

class Button:
    buttonColors = {
        "hallway": (0, 150, 150, 150),
        "unavailable": (0, 0, 0, 200),
        "start_position": (100, 200, 0, 150),
        "room": (100, 0, 200, 150)
    }

    def __init__(self, surface, rect, index):
        self.surface = surface
        self.position = rect
        self.spaceType = "hallway"
        pygame.draw.rect(surface, Button.buttonColors[self.spaceType], self.position)
        
    def updatePosition(self, newRect):
        self.position = newRect
    
    def draw(self):
        pygame.draw.rect(self.surface, Button.buttonColors[self.spaceType], self.position)

    def mouseOver(self, position):
        if position[0] > self.position[0] and position[0] < self.position[0] + self.position[2]:
            if position[1] > self.position[1] and position[1] < self.position[1] + self.position[3]:
                return True
        return False

    def cycleSpaceType(self):
        if self.spaceType == "hallway":
            self.spaceType = "unavailable"
        elif self.spaceType == "unavailable":
            self.spaceType = "start_position"
        elif self.spaceType == "start_position":
            self.spaceType = "room"
        elif self.spaceType == "room":
            self.spaceType = "hallway"



pygame.init()

filename = input("What file?? ")
#set up board window and image
boardImage = pygame.image.load(filename)
size = boardImage.get_size()
screen = pygame.display.set_mode(size, pygame.DOUBLEBUF)
background = pygame.Surface(size, pygame.SRCALPHA)
background.blit(boardImage, (0, 0))
buttonSurface = pygame.Surface(size, pygame.SRCALPHA)
buttonSurface.fill((0, 0, 0, 0))
screen.blit(boardImage, (0, 0))
pygame.display.update()


#initialize board grid
#we've seen both 22 and 25
gridSize = eval(input("What size is the board? ")) #pls pass me a tuple
x_step = size[0] / gridSize[0]
y_step = size[1] / gridSize[1]
print(f"{x_step}, {y_step}")

center_offset_x = 0
center_offset_y = 0
clock = pygame.time.Clock()
keys = pygame.key.set_repeat(200, 400)
def getButtonRect(index):
    return (index[0] * x_step + center_offset_x + 1, index[1] * y_step + center_offset_y + 1, x_step - 1, y_step - 1)

buttonList = []
for x in range(gridSize[0]):
    for y in range(gridSize[1]):
        buttonList.append(Button(buttonSurface, getButtonRect((x, y)), (x, y)))
screen.blit(buttonSurface, (0, 0))

def updateButtonPositions():
    for i in range(len(buttonList)):
        buttonList[i].updatePosition(getButtonRect((i // gridSize[0], i % gridSize[0])))

print("""
Color Legend:
    Cyan: Hallway
    Magenta: Starting Position
    Yellow: Room
    Black: Unavailable
""")

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttonList:
                if button.mouseOver(pygame.mouse.get_pos()):
                    button.cycleSpaceType()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            # shrink the board
            x_step = x_step - 1
            y_step = y_step - 1
            center_offset_x = center_offset_x + x_step / 2.0
            center_offset_y = center_offset_y + y_step / 2.0
            updateButtonPositions()
        elif keys[pygame.K_g]:
            x_step = x_step + 1
            y_step = y_step + 1
            center_offset_x = center_offset_x - x_step / 2.0
            center_offset_y = center_offset_y - y_step / 2.0
            updateButtonPositions()
        elif keys[pygame.K_DOWN]:
            center_offset_y = center_offset_y + 1
            updateButtonPositions()
        elif keys[pygame.K_UP]:
            center_offset_y = center_offset_y - 1
            updateButtonPositions()
        elif keys[pygame.K_LEFT]:
            center_offset_x = center_offset_x - 1
            updateButtonPositions()
        elif keys[pygame.K_RIGHT]:
            center_offset_x = center_offset_x + 1
            updateButtonPositions()
            

    buttonSurface.fill((0, 0, 0, 0))
    for button in buttonList:
        button.draw()

    screen.blit(background, (0, 0))
    screen.blit(buttonSurface, (0, 0))

    pygame.display.flip()


# save the state of the game
# button position, grid size, etc
with open("board_image_data.txt") as f:
    f.write("Button Positions, Spaces, ")
    for b in buttonList:
        f.write([b.position, b.spaceType])
    f.write("Grid Dimensions")
    f.write(gridSize)
    

