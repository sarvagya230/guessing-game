import random 
answer=random.randint(1,10)

chances=3
guessCount=0
while guessCount<chances:
    guess=int(input("guess a number"))
    if(guess<answer):
        print("to low")
        guessCount+=1
    elif(guess>answer):
        guessCount+=1
        print("too high")
    else:
        print("YOU WON!!!")
        break    
if(chances<=guessCount):
    print("you lost answer was ",answer)    