from pygame import Vector2
from game_objects.characters import Ghost, Vaxman
from game_objects.static import Food, Wall
from game import Game
from config import SCREEN_HEIGHT, SCREEN_WIDTH
import random


WALL_THICKNESS = 20

game = Game()

# All objects in the game
actors = []

# Main character
vax_man = Vaxman()
vax_man.color = (255, 255, 0)

vax_man.position.x = WALL_THICKNESS + vax_man.radius
vax_man.position.y = WALL_THICKNESS + vax_man.radius

# Constructing level
walls = []

wall = Wall()
wall.rect.width = WALL_THICKNESS
wall.rect.height = SCREEN_HEIGHT
wall.rect.topleft = (0, 0)
walls.append(wall)

wall = Wall()
wall.rect.height = WALL_THICKNESS
wall.rect.width = SCREEN_WIDTH
wall.rect.topleft = (0, 0)
walls.append(wall)

wall = Wall()
wall.rect.height = WALL_THICKNESS
wall.rect.width = SCREEN_WIDTH
wall.rect.bottomleft = (0, SCREEN_HEIGHT)
walls.append(wall)

wall = Wall()
wall.rect.height = SCREEN_HEIGHT
wall.rect.width = WALL_THICKNESS
wall.rect.topright = (SCREEN_WIDTH, 0)
walls.append(wall)

# Inner walls
WALLS_PER_COLUMN = (SCREEN_HEIGHT // WALL_THICKNESS - 2) // 2
WALLS_PER_ROW = (SCREEN_WIDTH - WALL_THICKNESS * 4) // (WALL_THICKNESS * 3)

starting_position = Vector2(walls[0].rect.topright[0] + WALL_THICKNESS, walls[0].rect.topright[1] + WALL_THICKNESS * 2)

for h_level in range(WALLS_PER_COLUMN):
    for w_level in range(WALLS_PER_ROW):
        wall = Wall()
        wall.rect.height = WALL_THICKNESS
        wall.rect.width = WALL_THICKNESS * 3
        wall.rect.topleft = (starting_position.x + WALL_THICKNESS * 4 * w_level, starting_position.y + WALL_THICKNESS * 2 * h_level)
        walls.append(wall)

# Dependency injection
vax_man.walls = walls

# creating food
starting_position = Vector2(WALL_THICKNESS + WALL_THICKNESS // 2, WALL_THICKNESS + WALL_THICKNESS // 2)

for h in range(SCREEN_HEIGHT // WALL_THICKNESS - 2):
    for w in range(SCREEN_WIDTH // WALL_THICKNESS - 2):
        position = Vector2(starting_position.x + WALL_THICKNESS * w, starting_position.y + WALL_THICKNESS * h)
        in_wall = False

        for wall in walls:
            if position.x >= wall.rect.left and position.x <= wall.rect.right and \
                position.y >= wall.rect.top and position.y <= wall.rect.bottom:

                in_wall = True
                break

        if in_wall:
            continue
        
        food = Food(vax_man)
        food.position = position
        actors.append(food)

# adding to game actors
actors.append(vax_man)

for wall in walls:
    actors.append(wall)


# adding ghosts
for n in range(0, 7):
    ghost = Ghost(vax_man, game)
    initial_position = Vector2(SCREEN_WIDTH - WALL_THICKNESS - ghost.radius - 1, WALL_THICKNESS + ghost.radius + 1)
    ghost.position.xy = (initial_position.x, initial_position.y + WALL_THICKNESS * 2 * n)
    
    if random.randint(0, 1) == 0:
        ghost.direction.x = random.randrange(-1, 1, 2)
    else:
        ghost.direction.y = random.randrange(-1, 1, 2)

    ghost.walls = walls
    actors.append(ghost)


for actor in actors:
    game.add_game_object(actor)


game.run_loop()

game.shutdown()