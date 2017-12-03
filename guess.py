import random

print "hello what is your name?"

name = input()
randomNum = random.randint(1,20)
print "hello ", name," think a number between 1 and 20"
#try only six
for guessNum in range(1,7):
    print "take a guess"
    guess = int(input())
    if guess < randomNum:
        print "it is too bit"
    elif guess > randomNum:
        print "too big"
    else:
        break

if guess == randomNum:
    print "greatt", name," bingo"
else:
    print "lost"
