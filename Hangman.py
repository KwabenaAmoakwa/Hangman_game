import random

print("WELCOME TO HANGMAN!")

word_list = ["orange","apple","seed","fruit","game","leader","ladder","pencil","sword","coconut","isreal","palace"]
word = random.choice(word_list)
losses = 0
empt_list= ["_" for c in word]

hang = [
        '''
        +---+
        |   |
            |
            |
            |
            |
        =========
        ''',
        '''
        +---+
        |   |
        O   |
            |
            |
            |
        =========
        ''',
        '''
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========
        ''',
        '''
        +---+
        |   |
        O   |
       /|   |
            |
            |
        =========
        ''',
        '''
        +---+
        |   |
        O   |
       /|\\  |
            |
            |
        =========
        ''',
        '''
        +---+
        |   |
        O   |
       /|\\  |
       /    |
            |
        =========
        ''',
        '''
        +---+
        |   |
        O   |
       /|\\  |
       / \\  |
            |
        =========
        '''
    ]




while empt_list != list(word):
    
    print(empt_list)
    i = input("Guess a letter: ")
    count = 0
    for x in range(len(word)):
        if i == word[x]:
            empt_list[x] = i 
        else:
            count+=1
            
    if count == len(word):
        losses+=1
    print(hang[losses])
            
    if losses == 6:
        break        
    
fin = "YOU WON" if losses != 6 else "YOU LOST"
print(f"\n{list(word)}\n{fin}")
