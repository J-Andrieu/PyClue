import pygame

class Notes:

    class Button:
        buttonColors = {
            "selected": (200, 0, 0, 150),
            "unselected": (0, 200, 0, 150),
            "highlight": (128, 128, 128, 100),
        }

        def __init__(self, surface, rect, text):
            pygame.init()
            self.font = pygame.font.SysFont('Arial', 25)
            self.surface = surface
            self.position = rect
            self.selected = "unselected"
            self.hovered = False
            self.text = text
            pygame.draw.rect(surface, Notes.Button.buttonColors["highlight"] if self.hovered else Notes.Button.buttonColors[self.selected], self.position)
            textimage = self.font.render(self.text, True, (191,)*3)
            self.surface.blit(textimage, textimage.get_rect(center= pygame.Rect(self.position).center))
            
        def updatePosition(self, newRect):
            self.position = newRect
        
        def draw(self):
            pygame.draw.rect(self.surface, Notes.Button.buttonColors["highlight"] if self.hovered else Notes.Button.buttonColors[self.selected], self.position)
            textimage = self.font.render(self.text, True, (191,)*3)
            self.surface.blit(textimage, textimage.get_rect(center= pygame.Rect(self.position).center))

        def mouseOver(self, position):
            if position[0] > self.position[0] and position[0] < self.position[0] + self.position[2]:
                if position[1] > self.position[1] and position[1] < self.position[1] + self.position[3]:
                    self.hovered = True
                    return True
            self.hovered = False
            return False

        def toggleSelection(self):
            if self.selected == "selected":
                self.selected = "unselected"
            elif self.selected == "unselected":
                self.selected = "selected"
            


    def __init__(self, positionOffset):
        self.characters = ["Col. Mustard", "Prof. Plum", "Mr. Green", "Mrs. Peacock", "Miss Scarlet", "Mrs. White"]
        self.weapons = ["Knife","Candlestick","Revolver","Rope","Lead Pipe","Wrench"]
        self.rooms = ["Hall","Lounge","Dining Room","Kitchen","Ball Room","Conservatory","Billiard Room","Library","Study"]
        self.offset = positionOffset
        self.size = (250 * 3 + 60, 50 * len(self.rooms) + 10 * len(self.rooms))
        self.notesSurface = pygame.Surface(self.size, pygame.SRCALPHA)
        self.createButtons()
    
    def createButtons(self):
        self.font = pygame.font.SysFont('Arial', 25)
        width = 250
        height = 50
        self.buttonList = []
        pos_x = 10
        pos_y = 10
        for element in self.characters:
            self.buttonList.append(Notes.Button(self.notesSurface, (pos_x, pos_y, width, height), element))
            pos_y = pos_y + height + 10
        pos_x = pos_x + width + 20
        pos_y = 10
        for element in self.weapons:
            self.buttonList.append(Notes.Button(self.notesSurface, (pos_x, pos_y, width, height), element))
            pos_y = pos_y + height + 10
        pos_x = pos_x + width + 20
        pos_y = 10
        for element in self.rooms:
            self.buttonList.append(Notes.Button(self.notesSurface, (pos_x, pos_y, width, height), element))
            pos_y = pos_y + height + 10
            
    def draw(self, surface):
        self.notesSurface.fill((0, 0, 0, 0))
        for button in self.buttonList:
            button.draw()
        surface.blit(self.notesSurface, self.offset)
        return surface
    