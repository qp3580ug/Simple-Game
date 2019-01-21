play = False
letter_list = []

while play == False:
    play_game = input("Would you like to play a game of hangman?(y/n) ")

    if play_game.lower() == "y":
        play = True

while play == True:
    hangman_phrase = input("Enter a phrase to guess: ")
    correct_phrase = hangman_phrase

    for char in hangman_phrase:
        if char != " ":
            hangman_phrase = hangman_phrase.replace(char, "0") 
    playing_game = True
    strikes = 1
    print(hangman_phrase)
    

    while playing_game == True:

        letter_guess = input("Guess a letter: ")
        correct_letter = correct_phrase.upper()
        letter_list.append(letter_guess.upper())

        if letter_guess.lower() in correct_phrase.lower():
            print('That was a correct letter!')
            for i in correct_letter:
                if i != " ":
                    if i not in letter_list:
                        correct_letter = correct_letter.replace(i, "0")
            print(correct_letter)
            
        else:
            print("That is not correct! Strikes: " + str(strikes))
            strikes += 1
            if strikes == 7:
                print("Game Over!!!")
                playing_game = False
                play = False

