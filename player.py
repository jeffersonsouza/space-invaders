class Player:
    name = ''
    score = ''
    positionX = 0
    positionY = 0
    positionChangeX = 0
    positionChangeY = 0

    def __init__(self, x = 0, y = 0):
        self.positionX = x
        self.positionY = y

    def setPosition(self, x, y):
        if x >= 0:
            self.positionX = x
        if y >= 0:
            self.positionX = y
