from game import Game

def main():
    vax_man = Game()

    if vax_man.initialized:
        vax_man.run_loop()

    vax_man.shutdown()

if __name__ == "__main__":
    main()