import pygame
import numpy as np

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
grid = np.zeros(shape=gridSize)
x_step = size[0] / gridSize[0]
y_step = size[1] / gridSize[1]
print(f"{x_step}, {y_step}")

# for ix,iy in np.ndindex(grid.shape):
#     pygame.draw.rect(buttonSurface, (0, 150, 150, 150), (ix * x_step + 1, iy * y_step + 1, x_step - 1, y_step -1))
# screen.blit(buttonSurface, (0, 0))

clock = pygame.time.Clock()
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            # shrink the board
            x_step = x_step - 1
            y_step = y_step - 1
        elif keys[pygame.K_g]:
            x_step = x_step + 1
            y_step = y_step + 1

    buttonSurface.fill((255, 255, 255, 255))
    for ix,iy in np.ndindex(grid.shape):
        pygame.draw.rect(buttonSurface, (0, 150, 150, 150), (ix * x_step + 1, iy * y_step + 1, x_step - 1, y_step -1))

    screen.blit(background, (0, 0))
    screen.blit(buttonSurface, (0, 0))

    pygame.display.flip()
