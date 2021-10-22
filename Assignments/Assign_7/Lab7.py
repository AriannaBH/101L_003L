def get_min_mpg():
    while True:       
        #getting the min mpg from user
        try:
            min_mpg = int(input('Enter the minimum mpg ==> '))
            if min_mpg < 0:
                print('Fuel economy given must be greater than 0')
            elif min_mpg > 100:
                print('Fuel economy must be less than 100') 
            else:
                return min_mpg     
        except ValueError:
            print('You must enter a number for the fuel economy')

def get_input():    
    while True:
        #getting the file the user wants
        ifname = input ('Enter the name of the input vehicle file ==> ')
        try:    
            text = open(ifname, 'rb')
            rows = []
            for line in text:
                rows.append(line.strip().split('\t'))
                return rows
        except FileNotFoundError:
            print ('Could not open file', ifname)
            
def get_output(min_mpg, ifname):
    while True:
        try:
            ofname = input('Enter the name of the output to ==>')
            text = open(ofname, 'w')
            for data in ifname:
                try:
                    if min_mpg >= float(data[7]):
                        text.write('{0:<5}{1:<40}{2:<40}{3:>10}\n'.format(data[0],\
                                data[1],data[2],data[7]))
                except:
                    print('Could not convert value invalid for vehicle', data[0], data[1], data[2])
        except IOError:
            print('There is an IO Error ', ofname)

    
def main():
    min_mpg = get_min_mpg()
    ifname = get_input()[1:]
    get_output(min_mpg, ifname)

main()