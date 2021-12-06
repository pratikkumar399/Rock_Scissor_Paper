import random 

def play ():
    user = input ("Pick a choice : 'r' for rock , 's' for scissors , 'p' for paper  ")
    computer = random.choice(['r','s','p'])

    if user == computer :
        return "It\'s a Tie"

    if is_win(user, computer ):
        return "You won!"

    return "You lost!" # the computer won 



def is_win(player,opponent):
   # return true if computer wins 
   #r>s,s>p,p>r
   if(player =='r' and opponent == 's')  or (player=='p' and opponent == 'r') or (player == 's' and opponent=='p'):
       return True
print(play())