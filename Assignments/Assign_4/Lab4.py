def play_again() -> bool:
    play = input('Do you want to play again? ==>')
    while True:
        if play.upper() == 'Y' or play.upper() == 'YES': 
            return True
        if play.upper() == 'N' or play.upper() == 'NO':
            return False
        else:
            print('\nYou must enter Y/YES/N/NO to continue. Please try again')
            play = input('Do you want to play again? ==>')
    return True
print(play_again())
