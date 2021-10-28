import math 
def calc_avg(mylist): 
    leng=len(mylist) 
    tot=0
    for x in range(leng): 
        tot=tot+mylist[x] 
    return tot/leng 

def calc_std(mylist): 
    leng=len(mylist) 
    tot=0
    dev=0
    avg=calc_avg(mylist) 
    
    for x in range(leng): 
        dev=mylist[x]-avg 
        tot=tot+(dev * dev) 
        tot=tot/4 
        tot=math.sqrt(tot) 
    return tot 

test=[] 
program=[]
choice='7'

while choice!='Q': 
    print(" Grade Menu ") 
    print("1 - Add Test")
    print("2 - Remove Test")
    print("3 - Clear Tests")
    print("4 - Add Assignment")
    print("5 - Remove Assignment")
    print("6 - Clear Assignments")
    print("D - Display scores")
    print("Q - Quit")
    choice= input("Please enter your choice:") 

    if choice=='1': 
        score= int(input("Enter the new Test score 0-100 ==>"))
        if score<=0: 
            continue
        else:
            test.append(score) 
    elif choice=='2':
        r = int(input("Enter the test to remove ==>"))
        for x in range(len(test)): 
            if test[x] == r: 
                test.remove(r)
                break
            else:
                if x==len(test)-1:
                    print("Could not find that test to remove")
                    continue

    elif choice=='3': 
            test=[]
    elif choice=='4': 
        score= int(input("Enter the new Assignment score 0-100 ==>"))
        if score<=0: 
            continue
        else:
            program.append(score) 
    elif choice=='5':
        r = int(input("Enter the Assignment to remove ==>"))
        for x in range(len(program)): 
            if program[x]==r:
                program.remove(r)
                break
            else:
                if program[x]!= r:
                    print("Could not find that assignment to remove")
                continue
    elif choice=='6': 
        program=[]
    elif choice=='D' or choice=='d': 
        print("Type # min max avg std")
        print(" ")
        if len(test)==0 and len(program)==0: 
            print("Tests 0 n/a n/a n/a n/a")
            print("Programs 0 n/a n/a n/a n/a")
        elif len(test)!=0 and len(program)==0: 
            tmin=min(test) 
            tmax=max(test)
            tavg=calc_avg(test)
            tstd=calc_std(test)
            tlen=len(test)
            print("Test " + str(tlen) + " " + str(tmin) + " " + str(tmax) + " " + str(tavg) + " " + str(tstd))
            print("Programs 0 n/a n/a n/a n/a")
        elif len(test)==0 and len(program)!=0:
            pmin=min(program) 
            pmax=max(program)
            pavg=calc_avg(program)
            pstd=calc_avg(program)
            plen=len(program)
            print("Tests 0 n/a n/a n/a n/a")
            print("Program " + str(plen) + " " + str(pmin) + " " + str(pmax) + " " + str(pavg) + " " + str(pstd))
        elif len(test)!=0 and len(program)!=0: 
            tmin=min(test)
            tmax=max(test)
            tavg=calc_avg(test)
            tstd=calc_std(test)
            tlen=len(test)
            
            pmin=min(program)
            pmax=max(program)
            pavg=calc_avg(program)
            pstd=calc_avg(program)
            plen=len(program)
            
            print("Test " + str(tlen) + " " + str(tmin) + " " + str(tmax) + " " + str(tavg) + " " + str(tstd))
            print("Program " + str(plen) + " " + str(pmin) + " " + str(pmax) + " " + str(pavg) + " " + str(pstd))
    elif choice=='Q' or choice=='q': 
        break
else: 
    print("Invalid choice")