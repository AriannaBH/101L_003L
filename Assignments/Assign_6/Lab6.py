while True:
    print('MAIN MENU')
    print('1) Encode a string')
    print('2) Decode a string')
    print('Q) Quit')
    choice = input('Enter your selection ==> ')

    if choice == '1':
        phrase = input('Enter (brief) text to encrypt: ')
        num = int(input('Enter the number to shift letters by: '))
        enc=""
        for i in phrase:
            if(i>='a' and i<='z'):
                enc+=chr((ord(i)-ord('a')+num)%26 + ord('a'))
            elif(i>='A' and i<='Z'):
                enc+=chr((ord(i)-ord('A')+num)%26 + ord('A'))
            else:
                enc+=i
        print('Encrypted:', enc.upper())
    if choice == '2':
        phrase = input('Enter (brief) text to decrypt: ')
        num = int(input('Enter the number to shift letters by: '))
        enc=""
        for i in phrase:
            if(i>='a' and i<='z'):
                enc+=chr((ord(i)-ord('a')-num)%26 + ord('a'))
            elif(i>='A' and i<='Z'):
                enc+=chr((ord(i)-ord('A')-num)%26 + ord('A'))
            else:
                enc+=i
        print('Decrypted:', enc.upper())
    if choice == 'Q' or choice == 'q':
        break
