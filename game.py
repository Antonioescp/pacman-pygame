import pygame

class Game():

    FRAMES_PER_SECOND = 60
    MILISECONDS_IN_SECOND = 1000
    MILISECONDS_BETWEEN_FRAMES = MILISECONDS_IN_SECOND / FRAMES_PER_SECOND

    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 500

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode([Game.SCREEN_WIDTH, Game.SCREEN_HEIGHT])

        self.gameObjects = []
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

            
            for gameObject in self.gameObjects:
                gameObject.handle_input(event)


    def update(self):

        self.clock.tick(Game.FRAMES_PER_SECOND)

        deltaTime = (pygame.time.get_ticks() - self.tickCount) / Game.MILISECONDS_IN_SECOND
        self.tickCount = pygame.time.get_ticks()
        
        for gameObject in self.gameObjects:
            gameObject.update(deltaTime)


    def generate_output(self):

        self.screen.fill((0, 0, 0))
        
        for gameObject in self.gameObjects:
            gameObject.draw(self.screen)

        pygame.display.flip()


    def run_loop(self):
        while (self.isRunning):
            self.handle_input()
            self.update()
            self.generate_output()


    def add_game_object(self, game_object):
        self.gameObjects.append(game_object)
    

    def remove_game_object(self, game_object):
        self.gameObjects.remove(game_object)


    def shutdown(self):
        pygame.quit()
        