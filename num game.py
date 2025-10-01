import random
target=random.randint(1,50)
guess=None
while guess!=target:
    guess=int(input('Guess a number between 1 and 50:'))
    if guess<target:
        print('To low!')
    elif guess>target:
        print('To high!')
print('Corerct! You have guessed the number.')