i = int(input())
while i != 0:
    a, b, c, d = (int(i) for i in input().split())
    if ((a % b) == d or (a % b) == c and (a > b)) or ((b % a) == d or (b % a) == c and (b > a)):
        print("YES")
    else:
        print("NO")
    i -= 1
