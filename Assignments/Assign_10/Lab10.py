import os.path
save_path = 'Assignments\Assign_10'
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
word_dict = {}

while True:
    filename = input("Enter the name of the file to open ")
    try:
        cname = os.path.join(save_path + '\\'+ filename)
        with open(cname, 'r') as file:
            lines = file.readlines()
            for line in lines:
                for x in line:
                    if x in punctuations:
                        line = line.replace(x, '')
        words = line.lower().split()
        for word in words:
            if len(word) <= 3:
                continue
            else:
                if word in word_dict.keys():
                        word_dict[word] = word_dict[word] + 1
                else:
                    word_dict[word] = 1


        word_count = [(word, count) for word, count in sorted(word_dict.items(), key=lambda item: item[1], reverse=True)[:10]]

        counter = 1
        print('Most frequently used words')
        print('{:>0}{:>15}{:>15}'.format('#', 'Word', 'Frequency'))
        print('{:>15}'.format('================================='))
        for key in word_dict:
            if counter > 10:
                break
            else:
                frequency = word_dict[key]
                print('{:>0}{:>15}{:>15}'.format(counter, key, frequency))
                counter += 1

        onceCounter = 0
        for key in word_dict:
            if word_dict[key] == 1:
                onceCounter += 1

        uniqueCounter = len(word_dict)

        print('There are {} words that occur only once'.format(onceCounter))
        print('There are {} unique words in the document'.format(uniqueCounter))

    except:
        print('Could not open file',filename)
        print('Please Try Again\n')
        continue
    else:
        break