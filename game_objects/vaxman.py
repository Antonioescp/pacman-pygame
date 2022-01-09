from . import GameObject
import pygame

class Vaxman(GameObject):

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
