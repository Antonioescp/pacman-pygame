from pygame.sprite import DirtySprite
from . import GameObject
from game import Game
from pygame.math import Vector2
import pygame

class Character(GameObject):

    def __init__(self):
        super().__init__()

        self.velocity = Vector2()
        self.direction = Vector2()

        self.movement_speed = 125
        self.radius = 10

    
    def draw(self, screen):
        super().draw(screen)
        
        # characters will be a circle
        pygame.draw.circle(screen, self.color, self.position.xy, self.radius)

    
    def update(self, deltaTime):
        super().update(deltaTime)

        # updating position based on velocity and direction
        self.velocity.x = self.movement_speed * self.direction.x
        self.velocity.y = self.movement_speed * self.direction.y

        self.position.x += self.velocity.x * deltaTime
        self.position.y += self.velocity.y * deltaTime

    
class Vaxman(Character):

    def __init__(self):
        super().__init__()

        self.walls = []
    

    def update(self, deltaTime):

        # Collisions with walls
        for wall in self.walls:

            # Detecting collisions

            top = Vector2(self.position.x, self.position.y - self.radius)
            left = Vector2(self.position.x - self.radius, self.position.y)
            right = Vector2(self.position.x + self.radius, self.position.y)
            bottom = Vector2(self.position.x, self.position.y + self.radius)


            if top.x >= wall.rect.left and top.x <= wall.rect.right and\
                top.y <= wall.rect.bottom and top.y >= wall.rect.top:

                self.direction.xy = (0, 0)
                self.position.y += 1

            if left.x >= wall.rect.left and left.x <= wall.rect.right and \
                left.y >= wall.rect.top and left.y <= wall.rect.bottom:

                self.direction.xy = (0, 0)
                self.position.x += 1

            if right.x >= wall.rect.left and right.x <= wall.rect.right and \
                right.y >= wall.rect.top and right.y <= wall.rect.bottom:

                self.direction.xy = (0, 0)
                self.position.x -= 1

            if bottom.x >= wall.rect.left and bottom.x <= wall.rect.right and \
                bottom.y >= wall.rect.top and bottom.y <= wall.rect.bottom:

                self.direction.xy = (0, 0)
                self.position.y -= 1


        super().update(deltaTime)


    def handle_input(self, event):
        super().handle_input(event)
        
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_w:
                self.direction.y = -1
                self.direction.x = 0

            if event.key == pygame.K_s:
                self.direction.y = 1
                self.direction.x = 0

            if event.key == pygame.K_d:
                self.direction.x = 1
                self.direction.y = 0

            if event.key == pygame.K_a:
                self.direction.x = -1
                self.direction.y = 0


class Ghost(Character):

    def __init__(self, vaxman):
        super().__init__()

        self.vaxman = vaxman

    
    def update(self, deltaTime):
        super().update(deltaTime)

        distance = self.position.distance_to(self.vaxman.position)

        if distance <= (self.radius + self.vaxman.radius):
            print("Covid destroyed")
            self.must_destroy = True