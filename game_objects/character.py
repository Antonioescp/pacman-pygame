from . import GameObject
from .vector import Vector2
import pygame

class Character(GameObject):

    def __init__(self):
        super().__init__()

        self.velocity = Vector2()
        self.direction = Vector2()

        self.movement_speed = 125

    
    def draw(self, screen):
        super().draw(screen)
        
        # characters and most objects will be circular
        pygame.draw.circle(screen, self.color, self.position.to_tuple(), self.radius)

    
    def update(self, deltaTime):
        super().update(deltaTime)

        # updating position based on velocity and direction
        self.velocity.x = self.movement_speed * self.direction.x
        self.velocity.y = self.movement_speed * self.direction.y

        self.position.x += self.velocity.x * deltaTime
        self.position.y += self.velocity.y * deltaTime