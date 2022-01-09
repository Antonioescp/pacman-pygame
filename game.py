import pygame

class Game():

    SCREEN_WIDTH = 1024
    SCREEN_HEIGHT = 768

    @property
    def initialized(self):
        return pygame.get_init()


    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode([Game.SCREEN_WIDTH, Game.SCREEN_HEIGHT])

        self.isRunning = True

    
    def handle_input(self):
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.isRunning = False


    def update(self):
        self.screen.fill((0, 0, 0))

        pygame.display.flip()


    def generate_output(self):
        pass


    def run_loop(self):
        while (self.isRunning):
            self.handle_input()
            self.update()
            self.generate_output()


    def shutdown(self):
        pygame.quit()
        