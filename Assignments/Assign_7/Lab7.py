while True:
    
    #getting the min mpg from user
    try:
        min_mpg = int(input('Enter the minimum mpg ==> '))
        if min_mpg < 0:
            print('Fuel economy given must be greater than 0')
            continue
        elif min_mpg > 100:
            print('Fuel economy must be less than 100')      
            continue
    except ValueError:
        print('You must enter a number for the fuel economy')
        continue    
        
    #getting the file the user wants
    try:
        fname = input ("Enter the name of the input vehicle file ==> ")
        text = open (fname, 'r')
    except FileNotFoundError:
        print ("Could not open file", fname)
    except IOError:
        print('There is an IO Error ', fname)

    #Taking away the tabs
    text_in = text.read().lower()
    for ch in '\t':
        text_in = text_in.replace(ch, ' ')
    #words = text_in.split() - might not need this