import random
choices = ['stone', 'paper', 'scissor']
while True:
    computer_choice = random.choice(choices)
    user_choice = input('Enter your choice (stone/paper/scissor): ').lower()
    if user_choice =='exit':
        break
    while user_choice not in choices:
        print('Please enter a valid choice!!')
        user_choice = input('enter your choice (stone/paper/scissor): ').lower()
    print('user:', user_choice)
    print('computer:', computer_choice)

    if user_choice == computer_choice:
        print('Its a tie')
    elif ((user_choice == 'stone' and computer_choice == 'scissor')
            or (user_choice == 'paper' and computer_choice == 'stone')
            or (user_choice == 'scissor' and computer_choice == 'paper')):
        print('You win🤩!')
    else:
        print('Computer win🤖')
            
    play_again =input('Do you want to play again (yes/no): ').lower()
    if play_again == "yes":
        continue
    while (play_again != "no" and play_again != "yes"): 
        print("Invalid input. Please enter either 'yes' or 'no'.")
        play_again =input('Do you want to play again (yes/no):').lower()
        if (play_again == "yes" or play_again == "no"):
            break
    if play_again == "no":
        break
