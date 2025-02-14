row = int(input("enter number of rows = "))

for i in range(0, row): #outer loops is representing row
    for j in range(0, i+1): #inner loops is representing column
        print("*", end=" ")

    print()