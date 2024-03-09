# File: CS112_A1_T2_Game2_20230302
# Purpose: This game is played with a list of numbers between 1 and 9. Each player takes turns 
#          picking a number from the list. The number picked can't be picked again. If a player 
#          has picked three numbers that add up to 15, that player wins the game. If all numbers
#          are used and no player gets exactly 15, the is a draw.
# Author: Mary Magdy Kamal Iskander
# ID: 20230302

# Function to check if there is three numbers that add up to 15 in the player list
def has_sum_of_15(numbers):
    if len(numbers)<3:
        return False
    # going over the list of numbers of the player to calculate if there exist a three numbers that add up to 15, else return false
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            for k in range(j+1, len(numbers)):
                if numbers[i] + numbers[j] + numbers[k] == 15:
                    return True
    return False

available_numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9]
available_number_characters="123456789"
numbers_of_player1=[]
numbers_of_player2=[]
winner=False
print("Welcome to Number scrabble")
print("This game is played with a list of numbers between 1 and 9. Each player takes turns picking a number from the list. The number picked can't be picked again. If a player has picked three numbers that add up to 15, that player wins the game. If all numbers are used and no player gets exactly 15, the is a draw.")
while True:
    # if all the numbers are picked and there is no winner this means that the game is a draw
    if len(available_numbers)==0: 
        print("DRAW")
        break

    while True:
        print(available_numbers)
        number1=input("player1: please pick a number between 1 to 9\n")
        if number1 in available_number_characters:
            if int(number1) in available_numbers:
                numbers_of_player1.append(int(number1)) # to add the picked number to the player1 list
                if has_sum_of_15(numbers_of_player1):
                    print("player1 is the winner\n")
                    winner=True
                available_numbers.remove(int(number1)) # to remove the picked number from the available numbers list
                break
            else:
                print("please pick another number from:",available_numbers,'\n')
        else:
            print("please enter a valid number")
    if winner == True:
        break
    while True:
        print(available_numbers)
        number2=input("player2: please pick a number between 1 to 9\n")
        if number2 in available_number_characters:
            if int(number2) in available_numbers:
                numbers_of_player2.append(int(number2)) # to add the picked number to the player2 list
                if has_sum_of_15(numbers_of_player2):
                    print("player2 is the winner\n")
                    winner=True
                available_numbers.remove(int(number2)) # to remove the picked number from the available numbers list
                break
            else:
                print("please pick another number from:",available_numbers,'\n')
        else:
            print("please enter a valid number")
    if winner == True:
        break
