import numpy as np

class Deck:
    class Card:
        def __init__(self, cardType, text):
            self.cardType = cardType
            self.text = text

    def __init__(self):
        self.cards = []
        self.characters = ["Col. Mustard", "Prof. Plum", "Mr. Green", "Mrs. Peacock", "Miss Scarlet", "Mrs. White"]
        self.weapons = ["Knife","Candlestick","Revolver","Rope","Lead Pipe","Wrench"]
        self.rooms = ["Hall","Lounge","Dining Room","Kitchen","Ball Room","Conservatory","Billiard Room","Library","Study"]
        self.crimeCards = self.getCrimeCards()
        for name in self.characters:
            self.cards.append(Deck.Card("character", name))
        for weapon in self.weapons:
            self.cards.append(Deck.Card("weapon", weapon))
        for room in self.rooms:
            self.cards.append(Deck.Card("room", room))
        np.random.shuffle(self.cards)        
    
    def getCrimeCards(self):
        murdererIndex = np.random.randint(0,len(self.characters))
        murderer = self.characters[murdererIndex]
        del self.characters[murdererIndex]
        weaponIndex = np.random.randint(0,len(self.weapons))
        murder_weapon = self.weapons[weaponIndex]
        del self.weapons[weaponIndex]
        roomIndex = np.random.randint(0,len(self.rooms))
        murder_room = self.cards[roomIndex]
        del self.rooms[roomIndex]
        return (murderer, murder_weapon, murder_room)
        
    def drawCard(self):
        return self.cards.pop()
        
    def makeGuess(self, guess):
        if guess[0].lower() == self.crimeCards[0].lower():
            if guess[1].lower() == self.crimeCards[1].lower():
                if guess[2].lower() == self.crimeCards[2].lower():
                    return True
        
        return False
