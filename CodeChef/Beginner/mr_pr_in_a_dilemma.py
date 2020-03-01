i = int(input())
while i != 0:
    a, b, c, d = map(int,input().split( ))
    if (a == b):
        print("YES")
    elif (c != d):
        if (abs(a - b) % abs(c - d) == 0):
            print("YES")
        else:
            print("NO")
    else: 
        print("NO")
    i -= 1