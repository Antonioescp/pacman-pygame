from game import Game
from game_objects.characters import Ghost, Vaxman
from game_objects.static import Food, Wall

actors = []

# Main character
vax_man = Vaxman()
vax_man.color = (255, 255, 0)

vax_man.position.y -= 70

actors.append(vax_man)

# Ghosts
pinky = Ghost(vax_man)
pinky.position.x = 50

actors.append(pinky)

# Walls in level
left_wall = Wall()

left_wall.rect.width = 25
left_wall.rect.height = Game.SCREEN_HEIGHT

left_wall.rect.topleft = (0, 0)

actors.append(left_wall)

top_wall = Wall()

top_wall.rect.height = 25
top_wall.rect.width = Game.SCREEN_WIDTH

top_wall.rect.topleft = (0, 0)

actors.append(top_wall)

right_wall = Wall()

right_wall.rect.height = Game.SCREEN_HEIGHT
right_wall.rect.width = 25

right_wall.rect.topright = (Game.SCREEN_WIDTH, 0)

actors.append(right_wall)

bottom_wall = Wall()

bottom_wall.rect.height = 25
bottom_wall.rect.width = Game.SCREEN_WIDTH

bottom_wall.rect.bottomleft = (0, Game.SCREEN_HEIGHT)

actors.append(bottom_wall)

# Dependency injection
vax_man.walls = [top_wall, left_wall, bottom_wall, right_wall]

game = Game()

for actor in actors:
    game.add_game_object(actor)

game.run_loop()

game.shutdown()