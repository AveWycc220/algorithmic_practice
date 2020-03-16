i = int(input())
while i != 0:
    words = [input(), input()]
    count_b = 0; count_o = 0
    h = 0
    if len(words[0]) >= 3 and len(words[1]) >= 3:
        for k, j in zip(words[0],words[1]):
            if (k == "b" or j == "b"):
                count_b += 1
            if (k == "o" or j == "o"):
                count_o += 1
            if (k != "o" and k != "b" and j != "o" and j != "b"):
                count_b = 0; count_o = 0
                break
            h += 1
            if (h == 3): 
                break
    if (count_b >= 2 and count_o >= 1):
        print("yes")
        count_b = 0; count_a = 0
    else:
        print("no")
        count_b = 0; count_a = 0
    i -= 1