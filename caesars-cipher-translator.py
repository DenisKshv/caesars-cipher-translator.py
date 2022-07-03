import re

while True:

    # Let's get the string we have to translate and make sure it contains at least one letter.
    while True:
        un_translated_text = str(input("Please input the text you would like to translate: "))
        if not(re.search('[a-zA-Z]', un_translated_text)):
            print("Enter at least one letter.")
        else:
            break

    # Now we want to get a direction we will be shifting in (left or right). And then convert it to either -1 or 1 to ake it easier later.
    while True:
        shifting_direction = str(input("Now how do you want to shift ('r' for right or 'l' for left): "))
        shifting_direction = shifting_direction.strip()
        if shifting_direction == "l":
            shifting_direction = -1
            break
        elif shifting_direction == "r":
            shifting_direction = 1
            break
        else:
            print("Please enter either 'r' or 'l'.")

    # And finally we want to find out by how much does user want to shift the letters. And make sure this number is less then 26 by using '%' operator.
    while True:
        shifting_amount = input("Now by how much do you want to shift (positive digit): ")
        if shifting_amount.isdigit():
            shifting_amount = int(shifting_amount)
            if shifting_amount >= 25:
                shifting_amount = shifting_amount % 26
            break
        else:
            print("Please enter a positive digit.")

    # And now to make calculations even more easier we will make variable "shifting vector" to store information about direction and amount of shifting in one variable.
    shifting_vector = shifting_direction * shifting_amount

    # Now we will establish english alphabet to understand where and from where to shift the letter.
    english_alphabet = ['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z']

    translated_text = ''    # Start with translated text set to nothing.

    # Now here's the best part. It is responsible for creating translated text.
    for current_symbol in un_translated_text:   # Loop through every symbol in the user-inputed string.
        if re.search('[a-zA-Z]', current_symbol):   # Check if the symbol we're on is a letter.
            translated_letter_index = english_alphabet.index(current_symbol) + shifting_vector * 2   # If yes - we need to find it's index in the alphabet. And then shift it by shifting vector (it is multiplied by two to get the letter of the same upper/lower case )
            if translated_letter_index >= 52:    # Check if we try to access past letter 'Z'. Variable translated_letter_index is at most 104. 
                translated_letter_index -= 52    # If yes - we have to set it back in range of 'english_alphabet' array by deducting 52 from it.
            translated_text += english_alphabet[translated_letter_index]     # Add translated letter into translated text.
        else:   # If symbol we're on is not a letter - just add this symbol into transtlated text
            translated_text += current_symbol

    # Finally print the translated text
    print("Here is the result:")
    print(translated_text)

    while True:
        print("Would you like to try to translate something else? (type only 'yes' or 'no')")
        continue_or_not = str(input("Your answer: "))
        if continue_or_not == "no":
            print("In that case, goodbye!")
            exit()
        elif continue_or_not == "yes":
            print("Ok, we'll start again!")
            break
        else:
            pass