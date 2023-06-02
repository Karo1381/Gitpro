string = input("inter the string:")

for i in range(len(string)):
    if i+1<len(string):

        print(string[i:i+2])
        if i+2 < len(string):

            print(string[i:i+3])
            if i+3<len(string):

                print(string[i:i+4])
