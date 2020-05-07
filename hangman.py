import random
print('H A N G M A N')
intro_word = input('Type "play" to play the game, "exit" to quit:')
print()
words = ['python', 'java', 'kotlin', 'javascript']

hint = random.choice(words)

#letters_total = len(hint)
#letters_to_hide = - (letters_total - 3)
#part_to_hide = hint[letters_to_hide:]
#tire = "-"
#hidden_part = part_to_hide.replace(part_to_hide,tire[letters_to_hide:])
#phrase = f'Guess the word {hint[:3]+ tire * (-letters_to_hide) }:'
#user_word = input(phrase)

#if user_word == hint:
#    print("You survived!")
#else:
#    print("You are hanged!")

hint_length = len(hint)
hidden_hint = hint.replace(hint, "-" * hint_length)


phrase = 'Input a letter:'
prev_letter = []
lives = 8
if intro_word == "play":
    while lives <= 8:
        print(hidden_hint)

        letter = input(phrase)

        if letter in prev_letter:
            print('You already typed this letter')
            print()
            continue

        if len(letter) > 1:
            print('You should print a single letter')
            print()
            continue

        if letter.isalpha() == 0:
            print('It is not an ASCII lowercase letter')
            print()
            continue

        if letter.islower() == 0:
            print('It is not an ASCII lowercase letter')
            print()
            continue

        if letter not in hint:
            print('No such letter in the word')
            lives = lives - 1
        if letter in hidden_hint:
            print('No improvements')
            lives = lives - 1

        x = 0
        while x < len(hint):
            if letter == hint[x]:
                hidden_hint = hidden_hint[:x] + letter + hidden_hint[x+1:]
            x = x + 1
        if lives == 0:
            if hidden_hint != hint:
                print('You are hanged!')
                print()
                intro_word = input('Type "play" to play the game, "exit" to quit:')
                break
        print()
        if hidden_hint == hint:
            print(hint)
            print('You guessed the word!')
            print('You survived!')
            break

        prev_letter.append(letter)
