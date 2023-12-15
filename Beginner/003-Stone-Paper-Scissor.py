import random
choices = ['stone', 'paper', 'scissor']
while True:
    computerC = random.choice(choices)
    userC = input('Enter your choice (stone/paper/scissor): ').lower()
    if userC =='exit':
        break
    while userC not in choices:
        print('Please enter a valid choice!!')
        userC = input('enter your choice (stone/paper/scissor): ').lower()
    print('user:', userC)
    print('computer:', computerC)

    if userC == computerC:
        print('Its a tie')
    elif ((userC == 'stone' and computerC == 'scissor')
            or (userC == 'paper' and computerC == 'stone')
            or (userC == 'scissor' and computerC == 'paper')):
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
