import random
def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]
print("Would you like to play a game of Hangman?")
easy_words = ["boat", "flap", "trip", "flip", "port", "trap", "hose", "that", "kill", "more" ]
med_words = ["quite", "horse", "force", "loser", "deers", "worse", "hertz", "joule"]
hard_words = ["careful", "tinfoil", "nothing", "basement", "vermin"]
input1 = input()
yesv = ["yes","Yes", "y", "Y"]
yesvv = input1 in yesv
if yesvv == 1 :
    print("What difficulty would you like to play at: easy, medium, or hard")
    input2 = input()
else:
    print("woops")
if input2 == "easy":
    num = random.randint(0, len(easy_words) - 1)
    chosen_word = easy_words[num]
elif input2 == "medium":
    num = random.randint(0,len(med_words) - 1)
    chosen_word = med_words[num]
else:
    num = random.randint(0,len(hard_words) - 1)
    chosen_word = hard_words[num]
split_word = list(chosen_word)
bad_guesses = 0
#print(split_word)
while len(split_word) > 0 and bad_guesses < 5:
    print("There are" + " " + str(len(split_word)) + " letters left")
    print("Please guess a letter")
    #print(chosen_word)
    input3 = input()
    #print(input3)
    yesvvv = input3 in split_word
    #print(yesvvv)
    if yesvvv == 1:
        split_word = remove_values_from_list(split_word,input3)
        print("Yes, " + input3 + " is in the word")
    else:
        bad_guesses +=1
        print("Sorry, " + str(input3) + " is not in the word")
if len(split_word) == 0:
    print("Woo, You have guessed the word " + chosen_word + ", winner is you")
else:
    print("Sorry, you ran out of guesses and let the person die :(")
	
