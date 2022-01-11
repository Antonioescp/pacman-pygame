from pygame.math import Vector2
from config import SCREEN_WIDTH, SCREEN_HEIGHT
# Monolithic class hierarchy since it is a simple game
class GameObject():

    # this class encapsulates common behaviour and data present in most game objects

    def __init__(self):
        self.position = Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

        self.color = (255, 255, 255)

        self.must_destroy = False


    # This will be call on Game draw method
    def draw(self, screen):
        pass


    # This will be call on Game update method
    def update(self, deltaTime):
        pass


    def handle_input(self, event):
        pass