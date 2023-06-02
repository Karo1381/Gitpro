import random

i=3
j=4
k=5
A=[[[0 for x in range(k)]
    for y in range (j)]for z in range (i)]
for x in range (i):
    for y in range (j):
        for z in range (k):
            A[x][y][z] =random.randint(0,4)
            count =0
            for x in range (i):
                for y in range (j):
                    for z in range (k):
                        if A[x][y][z] == 0:
                            count += 1
                            print("num zero arry:", count)
                            
