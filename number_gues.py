import random
logo = '''                                                     
 /  _____/ __ __   ____   ______ ______ \__    ___/|  |__   ____    \      \  __ __  _____\_ |__   ___________  
/   \  ___|  |  \_/ __ \ /  ___//  ___/   |    |   |  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \ 
\    \_\  \  |  /\  ___/ \___ \ \___ \    |    |   |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ 
 \______  /____/  \___  >____  >____  >   |____|   |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|    
        \/            \/     \/     \/                  \/     \/          \/            \/    \/     \/        
         
         '''
print(logo)
print("Welcome number guessing game")
print("I am thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty level: type 'easy' or 'hard' ")
number = random.choice(range(1, 100))
print(number)
def choose_difficulty():
    attempts = 0
    if difficulty == 'easy':
        attempts = 10
    else:
        attempts = 5
    return attempts
def play_game():
    attempt = choose_difficulty()
    for i in range(attempt):
        print(f"you have {attempt} attempts to guess the number")
        guess = int(input("Make a guess: "))
        if guess == number:
            print(f"you got it the answer is {number}")
            break
        elif guess < number:
            print("Too low")
        elif guess > number:
            print("Too high")
        elif attempt < 1:
            print("You have ran out of attempts. Refresh the page to run again")
        else:
            print("you lose")
        attempt = attempt - 1

play_game()