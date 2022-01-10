from pygame import Vector2
from game import Game
from game_objects.characters import Ghost, Vaxman
from game_objects.static import Food, Wall

WALL_THICKNESS = 20

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
wall.rect.height = Game.SCREEN_HEIGHT
wall.rect.topleft = (0, 0)
walls.append(wall)

wall = Wall()
wall.rect.height = WALL_THICKNESS
wall.rect.width = Game.SCREEN_WIDTH
wall.rect.topleft = (0, 0)
walls.append(wall)

wall = Wall()
wall.rect.height = WALL_THICKNESS
wall.rect.width = Game.SCREEN_WIDTH
wall.rect.bottomleft = (0, Game.SCREEN_HEIGHT)
walls.append(wall)

wall = Wall()
wall.rect.height = Game.SCREEN_HEIGHT
wall.rect.width = WALL_THICKNESS
wall.rect.topright = (Game.SCREEN_WIDTH, 0)
walls.append(wall)

wall = Wall()
wall.rect.height = WALL_THICKNESS
wall.rect.width = 50
wall.rect.topleft = (walls[0].rect.topright[0] + WALL_THICKNESS + 2, walls[0].rect.topright[1] + WALL_THICKNESS * 2 + 2)
walls.append(wall)

# Dependency injection
vax_man.walls = walls

# creating food
starting_position = Vector2(WALL_THICKNESS + WALL_THICKNESS // 2, WALL_THICKNESS + WALL_THICKNESS // 2)
for h in range(Game.SCREEN_HEIGHT // WALL_THICKNESS - 2):
    for w in range(Game.SCREEN_WIDTH // WALL_THICKNESS - 2):
        position = Vector2(starting_position.x + WALL_THICKNESS * w, starting_position.y + WALL_THICKNESS * h)
        in_wall = False

        for wall in walls:
            if position.x >= wall.rect.left and position.x <= wall.rect.right and \
                position.y >= wall.rect.top and position.y <= wall.rect.bottom:

                in_wall = True

        if in_wall:
            continue
        
        food = Food(vax_man)
        food.position = position
        actors.append(food)

# adding to game actors
for item in walls:
    actors.append(item)

actors.append(vax_man)

game = Game()

for actor in actors:
    game.add_game_object(actor)

game.run_loop()

game.shutdown()