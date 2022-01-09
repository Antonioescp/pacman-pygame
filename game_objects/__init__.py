from .vector import Vector2
from game import Game
import pygame

# Monolithic class hierarchy since it is a simple game
class GameObject():

    # this class encapsulates common behaviour and data present in most game objects

    def __init__(self):
        self.position = Vector2(Game.SCREEN_WIDTH / 2, Game.SCREEN_HEIGHT / 2)
        self.velocity = Vector2()
        self.direction = Vector2()

        self.color = (255, 255, 255)
        self.radius = 10
        
        self.movement_speed = 125

        self.tag = ""


    # This will be call on Game draw method
    def draw(self, screen):

        # characters and most objects will be circular
        pygame.draw.circle(screen, self.color, self.position.to_tuple(), self.radius)


    # This will be call on Game update method
    def update(self, deltaTime):
        
        # updating position based on velocity and direction
        self.velocity.x = self.movement_speed * self.direction.x
        self.velocity.y = self.movement_speed * self.direction.y

        self.position.x += self.velocity.x * deltaTime
        self.position.y += self.velocity.y * deltaTime


    def handle_input(self, event):
        pass