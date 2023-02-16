# Kibo FPWP Final Project

import cowsay

name = input("Please Enter a nickname for your adventure: \n")

# To display a cow
if len(name) >= 1:
    cowsay.cow("hello, " + name)

if len(name) >= 1:
    cowsay.trex("hello, " + name)

start = input("Press Enter to start this Awesome Animal Adventure")
if start == "":
    print(f"WELC0ME TO MY ANIMAL GUESSING GAME {name}.\nIN THIS GAME, I'M GOING TO ASK YOU SOME COOL STUFF ABOUT ANIMALS")


print("")


# Defining the function
def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0

    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print(f"Correct Answer, You're Awesome {name}")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input(f"Sorry Wrong Answer, try again and think harder this time. You can do this {name} ")
            attempt = attempt + 1
    if attempt == 3:
        print("Sorry, the Correct answer is ",answer )
    
score = 0
print("Guess the Animal")

guess1 = input("Which bear lives at the North Pole? \n")
check_guess(guess1, "polar bear")

print("")

guess2 = input("Which is the fastest land animal? \n")
check_guess(guess2, "Cheetah")

print("")

guess3 = input("Which is the largest animal? \n")
check_guess(guess3, "Blue Whale")

print("")

guess4 = input("What's the name of the first animal that was displayed? \n")
check_guess(guess4, "Cow")

print("")

guess5 = input("What's the name of the second animal that was displayed? \n")
check_guess(guess5, "Trex")

print("")

# Printing the results
if score >=3:
    print(f"Congrats {name}, You Passed!. Your Score is "+ str(score), "out of 5")
else:
    print(f"{score} is not a good score, try again another time.")

print("THANK YOU FOR PLAYING MY GAME. COME AGAIN ANOTHER TIME.🤗")



