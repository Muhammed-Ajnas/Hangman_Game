import random
import hangman_words
import hangman_art
end_of_game = False
wl = hangman_words.word_list
chosen_word = random.choice(wl)
word_length = len(chosen_word)
lives=6
logo=hangman_art.logo
print(logo)
display = []
right_guess=[]
wrong_guess=[]
guess=""
for _ in range(word_length):
    display += "_"
while not end_of_game:
  if lives>0:
    guess = input("Guess a letter: ").lower()
    if guess not in right_guess and guess not in wrong_guess:
      if guess in chosen_word:
        right_guess+=guess
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
        print(f"{' '.join(display)}")
        if "_" not in display:
            end_of_game = True
            print(hangman_art.win)
      else:
        wrong_guess+=guess
        lives-=1
        print(f"The letter '{guess}' is not present in the word, Guess again you have {lives} lives left.\n{hangman_art.stages[lives]}")
    else:
      if guess in right_guess:
        print(f"You have already guessed this letter '{guess}',Try another letter.")
      else:
        print(f"You have already been punished for this wrong letter '{guess}',Try another letter.")
  else:
     end_of_game = True
     print("You lose.")