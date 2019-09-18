height = int(input("Height: "))
counter = 0
leftspaces = height
lefthashes = 0
rightspaces = height
righthashes = 0
x = ' '
while (counter <= height):
    while (leftspaces > counter):
        print(x, end="")
        leftspaces-=1
    while (lefthashes < counter):
        print("#", end="")
        lefthashes+=1
    print (x, end="")
    while (righthashes < counter):
        print("#", end="")
        righthashes+=1
    while (rightspaces > counter):
        print(x, end="")
        rightspaces-=1
    print("\n")
    leftspaces = height
    lefthashes = 0
    rightspaces = height
    righthashes = 0
    counter += 1

