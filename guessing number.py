#GUESSING THE NUMBER GAME
import random
def game():
    print("welcome to the guessing game ")
    level = input("Do you want to play easy 'E' or hard level 'h'").lower()
    if level == 'e':
        easy()
    elif level == 'h':
        hard()   
def easy():
    ans = random.randint(0, 101)
    lives = 10
    should_continue = True
    while should_continue:

        user = int(input("enter the number :  "))
        
        if user == ans:
            print("Yay you guessed correct you won ")
            should_continue = False
            restart = input("Do you want to play again Y or N :  ").lower()
            if restart == 'y':
                game()
            else:
                print("Game over Bye")
        elif user > ans:
            lives -=  1
            print(f"The guess is greater that answer and lives {lives}")
        elif user < ans:
            lives -= 1
            print(f"the guess is lesser than the answer and lives {lives} ")
        if lives == 0:
            should_continue = False
            print("game over ")
            
            if restart == 'y':
                game()
            else:
                print("game over Bye")
def hard():
    ans = random.randint(0, 101)
    lives = 5
    should_continue = True
    while should_continue:
        user = int(input("enter the number :  "))
        
        if user == ans:
            print("Yay you guessed correct you won ")
            should_continue = False
            restart = input("Do you want to play again Y or N :  ").lower()
            if restart == 'y':
                game()
            else:
                print("game over bye")
        elif user > ans:
            lives -=  1
            print(f"The guess is greater that answer and lives {lives}")
        elif user < ans:
            lives -= 1
            print(f"the guess is lesser than the answer and lives {lives} ")
        if lives == 0:
            should_continue = False
            print("game over ")
            restart = input("Do you want to play again Y or N :  ").lower()
            if restart == 'y':
                game()
            else:
                print("game over bye")
game()
            