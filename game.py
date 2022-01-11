from config import INITIAL_AMOUNT_OF_GHOSTS, SCREEN_HEIGHT, SCREEN_WIDTH, FRAMES_PER_SECOND, MILISECONDS_IN_SECOND
import game_objects
from game_objects.characters import Ghost
from game_objects.static import Food
import pygame
import pygame.freetype


class Game():

    game_font = None
    message = ""
    finished = False

    def __init__(self):
        pygame.init()

        Game.game_font = pygame.freetype.Font("font.ttf", 24)

        self.screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

        self.game_objects = []
        self.tickCount = 0
        self.clock = pygame.time.Clock()

        self.isRunning = pygame.get_init()

    
    def handle_input(self):
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.isRunning = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.isRunning = False

            
            for gameObject in self.game_objects:
                gameObject.handle_input(event)


    def update(self):

        self.clock.tick(FRAMES_PER_SECOND)

        deltaTime = (pygame.time.get_ticks() - self.tickCount) / MILISECONDS_IN_SECOND
        self.tickCount = pygame.time.get_ticks()
        
        for game_object in self.game_objects:
            game_object.update(deltaTime)

            if game_object.must_destroy:
                self.game_objects.remove(game_object)

        if Food.remaining == 0:
            Game.message = "YOU WIN"
            Game.finished = True


        if Ghost.remaining >= INITIAL_AMOUNT_OF_GHOSTS * 32:
            Game.message = "YOU LOSE"
            Game.finished = True


    def generate_output(self):

        self.screen.fill((0, 0, 0))
        
        if not Game.finished:
            for gameObject in self.game_objects:
                gameObject.draw(self.screen)
        else:
            Game.game_font.render_to(self.screen, (40, 50), Game.message, (255, 255, 255))

        pygame.display.flip()


    def run_loop(self):
        while (self.isRunning):
            self.handle_input()
            self.update()
            self.generate_output()


    def add_game_object(self, game_object):
        self.game_objects.append(game_object)
    

    def remove_game_object(self, game_object):
        self.game_objects.remove(game_object)


    def shutdown(self):
        pygame.quit()
        