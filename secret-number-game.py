import random

def selector():
    
    selection = ''
    
    while selection not in {'1', '2'}:
        selection = input('Select: 1 - guess what the computer thinks OR 2 - the computer guesses your number ')
        
    if selection == '1':
        guess(10)
    elif selection == '2':
        x = int(input('The computer will guess between 1 and what number? : '))
        computer_guess(x)
        
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
    
    print(f'Awesome! That is the number {random_number} correctly!!')    

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L) or correct (C)?').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print('Nice! Your number, {guess}, was guessed correctly!')
    
    
selector()

            
    