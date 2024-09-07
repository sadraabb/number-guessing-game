# Developer : Sadra Abbaszadeh
# The future awaiting us is beyond these words!

# Library imports
import random #----> Random library
import threading #----> Threading library (parallel processing)

# Lock used in parallel processing
lock = threading.Lock()

# Welcome message
print("Welcome")

# Game rules section
def rules():
    lock.acquire()
    print("""Game Rules:
       1. You only have 7 chances to guess
       2. For each correct guess, you receive 1 point
       3. The computer has 5 chances to guess your number
       4. Any attempt to cheat will result in disqualification
       """)
    lock.release()

# Registration section
def game():
    # global keyword to make variables global within the game function
    global name
    global player_number
    global number
    
    # User choice to play or not
    select = input("Hello, would you like to participate in the game? (please Type Yes Or No) ")
    
    # Checking user choice, if 'yes'
    if select.lower() == "yes":
        # Assigning a player number between 1 and 10
        player_number = random.randint(1, 10)
        # User entering their name
        name = input("Please enter your name: ")
        # Welcome message with the user's name
        print(f"{name}, welcome to the game! Hope you win :)")
        # Displaying the player number with the user's name
        print(f"Player {name}, Your Number: {player_number}")
        # Game preparation message
        print("Your game is now ready")
        # User's chosen number for the computer to guess
        number = int(input("Please send a number in the range (20, 60): "))
        # Checking if the chosen number is within the specified range
        if number not in range(20, 61):
            # Displaying an error message
            print("Error")
        elif number in range(20, 61):
            print(f"Your chosen number: {number}. Are you ready? You will guess first and then the computer :)")
            guess_user()
            guess_computer()
    # Checking user choice before entering the number
    elif select.lower() == "no":
        print("Sorry to hear that. Maybe next time :)")
    else:
        print("Please type a valid text")

## Computer guessing section
# Function for computer guessing
def guess_computer():
    # Number of chances for the computer to guess
    chances_computer = 6
    # Number of guesses made by the computer
    guesses_made_computer = 0
    
    # Loop until the number of guesses is less than the number of chances
    while guesses_made_computer < chances_computer:
        # Random number chosen by the computer
        pc_random = random.randint(20, 61)
        # Incrementing the number of guesses made by the computer
        guesses_made_computer += 1
        if pc_random < number: #-----> Checking condition for the computer
            print("< number")
        elif pc_random > number:
            print("> number")
        elif pc_random == number:
            points_computer = 1
            print(f"PC received {points_computer} point(s)") # -----> If the computer wins, it gets one point
            break #-----> Exiting the loop after receiving a point
    else:
        print("Computer lost")

## User guessing section
# Function for user guessing
def guess_user():
    # Number of chances available
    chances = 6
    # Number of guesses made
    guesses_made = 0
    # Random number chosen by the computer for the user to guess
    number2 = random.randint(1, 50)
    
    # Loop until the number of guesses is less than the number of chances
    while guesses_made < chances:
        guess = int(input(f"Please send your guess in the range (1,50). Note that you only have {chances} chances left: "))
        guesses_made += 1
        if guess < number2:
            print(f"Your number: {guess}, Your guess is smaller than the computer's number")
        elif guess > number2:
            print(f"Your number: {guess}, Your guess is larger than the computer's number")
        elif guess == number2:
            points = 1
            print(f"{name}, you won with number {player_number} and received {points} point(s)")
            break
    else:
        print(f"{name}, you lost :( The computer's number was {number2}")

# This section checks if the program is being run as the main module or just imported
if __name__ == "__main__":
    # Defining two threads to run the code in parallel
    thread1 = threading.Thread(target=rules)
    thread2 = threading.Thread(target=game)
    
    # Starting the threads
    thread1.start()
    thread2.start()
    
    # Waiting for the threads to finish
    thread1.join()
    thread2.join()
