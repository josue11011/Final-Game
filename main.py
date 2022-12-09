def game_intro():
    print("Welcome Detective.")

def main():
    game_intro()
    player_name = input("What is your name?")
    answer = input ("Hi, {} will you start this game? (y/n)".format(player_name))
    if answer.upper() == 'Y':
        print("Starting Chapter 1")

    else:
        print ('Goodbye now the game is closing')
        quit()
main()
import Chapter1
import Chapter2
import Chapter3
import Chapter4
import Chapter5
