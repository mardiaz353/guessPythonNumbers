import random

game_on = None
guesses = None

secret = None

def difficulty_level_easy():
    global secret
    secret = float(random.randrange(0, 100))
    while game_on:
        guess = int(input('Guess a number. '))
        if guess > secret:
            print('your guess is too high. Try again')
        elif guess < secret:
            print('Your guess is too low. Try again.')
        elif guess == secret:
            print('You win!')
            print('You will get a premium crisp on dollar bill delivered to your house')
            play_again()
            

#start game

def start_game():
    global game_on
    game_on = True
    level = input("Welcome. Type easy, hard, or quit. *This is case sensitive. Type it as you see it on the screen.")
    if level == 'easy':
        difficulty_level_easy()
    elif level == 'hard':
        difficulty_level_hard()
    elif level == 'quit':
        game_on = False
        print('Thank you for playing')

def play_again():
    global game_on
    game_on = True
    play = input('Play again? Yes or No. *Case sensitive.')
    if play == 'Yes':
        start_game()
    else:
        game_on = 'false'
    start_game()

#difficult version

def difficulty_level_hard():
   
    global random
    global guesses
    guesses = 3
    secret = int(random.randrange(0, 100))
     for i in range(guesses):#the letter i is used to mean one single number.
        guess = float(input('Guess a number. Bleh. '))
        if i == 2:
            print('Game over. Too many guesses.')
            if guess > secret:
            print('your guess is too high. Try again')
        elif guess < secret:
            print('Your guess is too low. Try again.')
        elif guess == secret:
            print('You win!')
            play_again()
            
