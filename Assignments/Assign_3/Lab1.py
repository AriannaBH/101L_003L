#Title
print('Welcome to the Flarsheim Guesser!\n')

#Users Choice to play again
play = 'Y'

#While Loop
while(play == 'y' or play == 'Y'):
    print('Please think of a number between and including 1 and 100.\n')

    #Remainders Initialized
    rthree = 0
    rfive = 0
    rseven = 0

    #Question asking for remainder of 3
    rthree = int(input('What is the remainder when your number is divided by 3?'))
    while(rthree < 0 or rthree >= 3):
        if rthree < 0:
            print('The value entered must be 0 or greater')
        elif rthree >= 3:
            print('The value entered must be less than 3')
        rthree = int(input('What is the remainder when your number is divided by 3?'))

    #Question asking for the remainder of 5      
    rfive = int(input('\nWhat is the remainder when your number is divided by 5?'))
    while(rfive < 0 or rfive >= 5):
        if rfive < 0:
            print('The value entered must be 0 or greater')
        elif rfive >= 5:
            print('The value entered must be less than 5')
        rfive = int(input('What is the remainder when your number is divided by 5?'))
    
    #Question asking for the remainder of 7
    rseven = int(input('\nWhat is the remainder when your number is divided by 7?'))
    while(rseven < 0 or rseven >= 7):
        if rseven < 0:
            print('The value entered must be 0 or greater')
        elif rseven >= 7:
            print('The value entered must be less than 7')
        rseven = int(input('What is the remainder when your number is divided by 7?'))

    #Guessing their number
    #Based on the remainders
    for i in range(1, 101):
        if i%3 == rthree and i%5 == rfive and i%7 == rseven:
            print('Your number was', i)
            print('How amazing is that?')

    #Asking User to play again
    #Using while to loop back 
    #Using if no it will break and not loop         
    play = input('\nDo you want to play again? Y to continue, N to quit ==> ')
    while(play != 'Y' and play != 'y' and play != 'N' and play != 'n'):
        play = input('\nDo you want to play again? Y to continue, N to quit ==> ')
        if play == 'N' or play == 'n':
            break



               
                
