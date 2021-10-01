import random

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
 
def get_wager(bank : int) -> int:
    wager = int(input('How many chips do you want to wager? ==>'))
    while bank >= 0:
        if wager > bank:
            print('The wager amount cannot be greater than how much you have. ', bank)  
            wager = int(input('How many chips do you want to wager? ==>'))
        if wager <= 0:
            print('The wager amount must be greater than 0. Please enter again.')
            wager = int(input('How many chips do you want to wager? ==>'))
        else:
            return wager


def get_slot_results() -> tuple:
    reela = random.randint(1, 10)
    reelb = random.randint(1, 10)
    reelc = random.randint(1, 10)
    return reela, reelb, reelc

def get_matches(reela, reelb, reelc) -> int:
    matches = 0
    if reela == reelb:
        matches += 2
        if reela == reelc:
            matches += 1
    elif reela == reelc:
        matches += 2
        if reela == reelb:
            matches += 1
    elif reelb == reelc:
        matches += 2
        if reelb == reela:
            matches += 1
    return matches


def get_bank() -> int:
    num = 0 
    while num == 0:
        bankStart = int(input('How many chips do you want to start with?\n'))
        if bankStart <= 0:
            print('Too low a value, you can only choose between 1 - 100 chips')
        elif bankStart > 100:
            print('Too high a value, you can only choose between 1 - 100 chips')
        else:
            num = 1
    return bankStart

def get_payout(wager, matches):
    if matches == 3:
        x = (wager * 10) - wager
    elif matches == 2:
        x = (wager * 3) - wager
    elif matches == 0:
        x = wager - wager - wager
    return x   

if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()

        while bank > 0:
            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()

            if bank == 0:
                print("You lost all", bank, "in", matches, "spins")
                print("The most chips you had was", payout)
                playing = play_again()