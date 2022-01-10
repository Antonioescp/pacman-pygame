from . import GameObject
import pygame

class Food(GameObject):

    remaining = 0

    def __init__(self, eater):
        super().__init__()

        self.radius = 2
        self.eater = eater

        Food.remaining += 1

    
    def draw(self, screen):
        super().draw(screen)

        pygame.draw.circle(screen, self.color, self.position.xy, self.radius)

    
    def update(self, deltaTime):
        super().update(deltaTime)

        distance = self.position.distance_to(self.eater.position)

        if distance <= (self.radius + self.eater.radius):

            self.must_destroy = True
            Food.remaining -= 1


class Wall(GameObject):

    def __init__(self):
        super().__init__()

        self.color = (0, 0, 255)

        width = 50
        height = 50

        left = self.position.x - width / 2
        top = self.position.y - height / 2

        self.rect = pygame.Rect(left, top, width, height)


    def draw(self, screen):
        super().draw(screen)

        pygame.draw.rect(screen, self.color, self.rect)