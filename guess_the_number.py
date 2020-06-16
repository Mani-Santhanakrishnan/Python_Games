# Number Guessing Game
# Author : Mani Santhanakrishnan
# Version: 3.8

def get_string():
    return input("Is the guess, correct/high/low:")

numb=50
lnum=0
hnum=100
print('The number is ',numb)
feedb= get_string()

while feedb != "correct":
    if feedb== "high" :
        hnum=numb
        numb= int((lnum+hnum)/2)
        print('The number is=', numb)
        feedb = get_string()
    elif feedb== "low" :
        lnum=numb
        numb= int((lnum+hnum)/2)
        print('The number is=', numb)
        feedb = get_string()
            
print('The number is =',numb)
