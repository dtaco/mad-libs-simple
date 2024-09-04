import random
def play():
    user = input("What's you choice? 'r' for rock. 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer:
        return 'It\'s a tie'
    
    if is_win(user, computer):
        return f'The computer chose {computer}.You won!'
    
    return f'The computer chose {computer}. You lost!'
    
def is_win(player, opponent):
    
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
            return True

print(play())