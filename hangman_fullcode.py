import random
words = ['mango','orange','apple','fruit','banana','jack','litch','house','photo','hangman','black','deer','rabbit','computer','water','stick','city','tiger','lion','grape','snake','python','circle','dice','monker','book','school','paper','human','pencil','earth','light','moon','shine','river','tree','table','lamp','kite','women','fire']

def guessed_word():
    return words[random.randint(0,len(words)-1)].upper()
print("start the game")
print()
selected_word = guessed_word()
guesses = []
for i in range(len(selected_word)):
    guesses.append('_')
    print('_',end = ' ')
print()
chances = 6
while chances>0 :
    guess = input(' enter an alphabet  :  ').upper()
    if len(guess) == 1:
        if guess in selected_word:
            print('your guess is correct')
            for i in range(len(selected_word)):
                if guess == selected_word[i]:
                    guesses[i]=guess
            req_word = ''
            print(req_word.join(guesses))

        else:
            print('your guess is wrong')
            chances -= 1
        guess_str = ''
        if guess_str.join(guesses) == selected_word:
            chances=0
        else:
            print('you have',chances,'more chances')
        if chances == 6:
            print('______     ')
            print('|    |     ')
            print('|          ')
            print('|          ')
            print('|          ')
            print('|          ')
            print('|          ')
        elif chances == 5:
            print('______     ')
            print('|    |     ')
            print('|    o     ')
            print('|          ')
            print('|          ')
            print('|          ')
            print('|          ')
        elif chances == 4:
            print('______     ')
            print('|    |     ')
            print('|    o     ')
            print('|    |     ')
            print('|    |     ')
            print('|          ')
            print('|          ')
        elif chances == 3:
            print('______     ')
            print('|    |     ')
            print('|    o     ')
            print('|   /|     ')
            print('|  / |     ')
            print('|          ')
            print('|          ')
        elif chances == 2:
            print('______     ')
            print('|    |     ')
            print('|    o     ')
            print('|   /|\    ')
            print('|  / | \   ')
            print('|          ')
            print('|          ')
        elif chances == 1:
            print('______     ')
            print('|    |     ')
            print('|    o     ')
            print('|   /|\    ')
            print('|  / | \   ')
            print('|   /      ')
            print('|  /       ')
        elif chances == 0 and guess_str.join(guesses) != selected_word:
            print('______     ')
            print('|    |     ')
            print('|    o     ')
            print('|   /|\    ')
            print('|  / | \   ')
            print('|   / \    ')
            print('|  /   \   ')
    else:
        print('please enter single letter only')
print()
word = ''
word = word.join(guesses)
if word == selected_word:
    print('you won')
else:
    print('you lose')
    print('the correct word is: ',selected_word)
