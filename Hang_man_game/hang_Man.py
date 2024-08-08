#code :

import random
import words
import logos

chosen_word = random.choice(words.word_list)
lives = 6

print(logos.logo)

display = ""
len_word = len(chosen_word)
for x in range(len_word) :
    display += "_"
print(display)

correct_letters = []
game_over = False
while not game_over :

    print(f"************{lives}/6 lives left************")
    guess = input("Guess a letter : ").lower()
    display = ""

    if guess in correct_letters:
        print(f"You have already guessed {guess}")     
    
    for letter in chosen_word :
        if letter == guess :
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters :
            display += letter
        else :
            display += "_"
    if guess not in chosen_word :
        print(f"You guessed {guess},that`s not in the word .You Lose a Life")
        lives -= 1
    
    print(display)
    if '_' not in display :
        game_over = True
        print("**********************You Win!!**********************")
    elif lives == 0 :
        game_over = True
        print("************You Lose!************")
        print(f"The word is {chosen_word}")

    print(logos.stages[lives])




