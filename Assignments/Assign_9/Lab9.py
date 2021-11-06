import csv


def month_from_number(n):
    months = {'1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May', '6': 'June', '7': 'July', '8': 'August', '9': 'September', '10': 'October', '11': 'November', '12': 'December'}
    return months[str(n)]


def read_in_file(filename):
    with open(filename,'r',encoding='utf-8') as file:
        content = []
        reader = csv.reader(file)
        for row in reader:
            content.append(row)
        file.close()
        return content

def create_reported_date_dict(content):
    date_count = {} 
    try:
        for row in content:
            key = row[1]
            date_count[key] = date_count.get(key,0) + 1
    except KeyError:
        date_count[key] = 1
    return date_count

def create_reported_month_dict(content):
    mon_count = {}
    try:
        for line in content[1:]:
            m = line[1][0:2]
            if m in mon_count:
                mon_count[m] += 1
    except KeyError:
        mon_count[m] = 1
    return mon_count

def create_offense_dict(content):
    o_count = {}
    try:
        for line in content[1:]:
            m = line[1][0:2]
            if m in o_count:
                o_count[m] += 1
    except KeyError:
        o_count[m] = 1
    return o_count

def create_offense_by_zip(content):
    z_count = {}
    for zip in content[1:]:
        key = zip[7]
        if key in z_count:
            oz_dict = z_count[key]
            if zip[13] in oz_dict:
                oz_dict[zip[13]]+=1
            else:
                oz_dict[zip[13]] = 1
        else:
            z_count[key] = {zip[13]:1}
    return z_count

def main():
    while(True):
        try:
            filename = input('Enter the name of the crime data file ==> ')
            data = read_in_file(filename)   

            month = create_reported_month_dict(data)
            print(month)
            mx = max(month,key=month.get)
            print('The month with the highest # of crimes is ' + month_from_number(mx)+ ' with ' + str(month[mx]) + ' offenses')
            offense = create_offense_dict(data)
            mx = max(offense,key=offense.get)
            print('The offense with the highest # of crimes is '+ mx + ' with ' + str(offense[mx]) + ' offenses')
            offense = create_offense_by_zip(data)
            print()
            while(True):
                off = input('Enter an offense : ')
                if off not in offense:
                    print('Not a valid offense, please try again')
                else:
                    break
            print(off + ' offense by Zip Code')
            print('Zip Code\t\t\t# Offenses')
            print('==========================================')
            for k,v in offense[off].items():
                print(k+"\t\t\t\t\t"+str(v))

        except FileNotFoundError:
            print('Sorry, ' + filename + ' not found')

if __name__ == "__main__":
    main()