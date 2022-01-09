from game import Game
from game_objects.vaxman import Vaxman

def main():
    
    # Main character
    vax_man = Vaxman()
    vax_man.color = (255, 255, 0)

    game = Game()

    game.add_game_object(vax_man)

    game.run_loop()

    game.shutdown()


if __name__ == "__main__":
    main()