import random
import os
import hangman_words
import hangman_art

chosenWord  = random.choice(hangman_words.word_list)
stages = hangman_art.stages
lives = 6
guessedWord = ""
guessedLetters = 0

for i in range(0, len(chosenWord)):
  guessedWord += "_"
guessedWord = list(guessedWord)
allLetters = []

print(hangman_art.logo, end = "\n\n")
while lives > 0:
  guess = input("Guess a letter: ")
  guess = guess.lower()

  while allLetters.count(guess) > 0 or len(guess) > 1:
    guess = input("Invalid or Already guessed! Guess another letter: ")
    guess = guess.lower()

  os.system('cls' if os.name == 'nt' else 'clear')
  print(hangman_art.logo, end = "\n\n")
  allLetters.extend(guess)
  
  if(chosenWord.find(guess) != -1):
    print(f"Nice! You guessed '{guess}'. It is in the word\n")
    print("Guessed Word:", end = " ")
    for i in range(0, len(chosenWord)):
      if chosenWord[i] == guess:
        guessedWord[i] = guess
        guessedLetters += 1
        print(guessedWord[i], end = " ")
      else:
        print(guessedWord[i], end = " "),
    print(f"\n{stages[lives]}")
    if guessedLetters == len(chosenWord):
      print(f"Congratulations! You have guessed the word: {chosenWord}")
      lives = -1
  else:
    lives -= 1
    print(f"Sorry! You guessed '{guess}'. It is not in the word\n")
    print("Guessed Word:", end = " ")
    print(" ".join(map(str, guessedWord)))
    print(stages[lives])

if lives != -1:
  print(f"Out of lives! You lost. Correct word: {chosenWord}\n")    