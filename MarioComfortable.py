height = int(input("Height: "))
counter = 0
leftspaces = height
lefthashes = 0
rightspaces = height
righthashes = 0
x = ' '
height = int(input("Height: "))
counter = 0
leftspaces = height
rightspaces = height
for counter in range(1, height+1):
    print(' '*(leftspaces-counter), end='')
    print('#'*(counter),end='')
    print(' ', end='')
    print('#'*(counter), end='')
    print(' '*(rightspaces-counter), end='')
    print()
