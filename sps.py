import random

def validate(res):
    if res < 0 or res > 2:
        return False
    else:
        return True
    
def pll(re,nm='You'):
    hand=['Stone','Paper','Scissor']
    print(nm+' selected '+hand[re])

def check(player,computer):
    
    if player == computer:
        return 'Draw'
    elif player == 0 and computer == 1:
        return 'Lose'
    elif player == 1 and computer == 2:
        return 'Lose'
    elif player == 2 and computer == 0:
        return 'Lose'
    else:
        return 'Win'


i=5
j=0
z=0
nam = input("Enter your name: ")
while(i>0):
    print('|0 : Stone| |1 : Paper| |2 : Scissor|')
    resp = int(input("Enter the response = "))
    if validate(resp):
        computer = random.randint(0,2)
        pll(resp,nam)
        pll(computer,'Computer')
        if check(resp,computer) == 'Win':
            j+=1
            print("You win in this round")
            print("Your score "+str(j)+" : "+"Computer score "+str(z))    
        elif check(resp,computer) == 'Lose':
            z+=1
            print("Computer win in this round")
            print("Your score "+str(j)+" : "+"Computer score "+str(z))
        else:
            print("Its a Draw in this round")
            print("Your score "+str(j)+" : "+"Computer score "+str(z))
        
    else:
        print('Please enter a valide number')

    if j == 5 or z == 5:
        break

if z > j:
    print("Computer wins : You loses"+" = "+str(z)+" : "+str(j))
else:
    print("You win : Computer loses"+" = "+str(j)+" : "+str(z))
