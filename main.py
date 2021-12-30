from game_manager import GameManager


def start():
    print("Welcome to Tic Tac Toe!\n")
    game_on = True
    while game_on:
        game = GameManager()
        game.play_game()
        play_again = input("Would you like to play again? (y/n): ").strip().lower()
        if play_again == 'n' or play_again == 'no':
            print('Thanks for playing, Bye!')
            game_on = False
        else:
            continue


start()
