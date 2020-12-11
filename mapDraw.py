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

center_offset_x = 0
center_offset_y = 0
clock = pygame.time.Clock()
keys = pygame.key.set_repeat(200, 400)
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
            center_offset_x = center_offset_x + x_step / 2.0
            center_offset_y = center_offset_y + y_step / 2.0
        elif keys[pygame.K_g]:
            x_step = x_step + 1
            y_step = y_step + 1
            center_offset_x = center_offset_x - x_step / 2.0
            center_offset_y = center_offset_y - y_step / 2.0
        elif keys[pygame.K_DOWN]:
            center_offset_y = center_offset_y + 1
        elif keys[pygame.K_UP]:
            center_offset_y = center_offset_y - 1
        elif keys[pygame.K_LEFT]:
            center_offset_x = center_offset_x - 1
        elif keys[pygame.K_RIGHT]:
            center_offset_x = center_offset_x + 1

    buttonSurface.fill((0, 0, 0, 0))
    for ix,iy in np.ndindex(grid.shape):
        pygame.draw.rect(buttonSurface, (0, 150, 150, 150), (ix * x_step + center_offset_x + 1, iy * y_step + center_offset_y + 1, x_step - 1, y_step -1))

    screen.blit(background, (0, 0))
    screen.blit(buttonSurface, (0, 0))

    pygame.display.flip()
