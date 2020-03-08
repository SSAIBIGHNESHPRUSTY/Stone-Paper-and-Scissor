import random

def validate(res):
    if res < 0 or res > 2:
        return False
    else:
        return True
    
def pll(re,nm='Guest'):
    hand=['Stone','Paper','Scissor']
    print(nm+' selected '+hand[re])

def check(p,c):
    
    if p == c:
        return 'Draw'
    elif p == 0 and c == 1:
        return 'Lose'
    elif p == 1 and c == 2:
        return 'Lose'
    elif p == 2 and c == 0:
        return 'Lose'
    else:
        return 'Win'
    
print('|0 : Stone| |1 : Paper| |3 : Scissor|')
resp = int(input("Enter the response = "))
name = input("Enter the name = ")
if validate(resp):
    computer = random.randint(0,2)
    pll(resp,name)
    pll(computer,'Computer')
    print(check(resp,computer))
else:
    print('Please enter a valide number')
