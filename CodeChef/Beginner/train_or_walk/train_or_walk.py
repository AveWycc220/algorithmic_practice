i = int(input())
while i != 0:
    n, a, b, c, d, p, q, y = map(int,input().split( ))
    x = list(map(int,input().split( )))
    if ((x[a-1] > 0 and x[b-1] < 0) or (x[a-1] < 0 and x[b-1] > 0)):
        time_p = abs(abs(x[b-1])+abs(x[a-1]))*p
    else:
        time_p = abs(abs(x[b-1])-abs(x[a-1]))*p
    if ((x[a-1] > 0 and x[c-1] < 0) or (x[a-1] < 0 and x[c-1] > 0)):
        time_to_c = abs(abs(x[c-1])+abs(x[a-1]))*p
    else:
        time_to_c = abs(abs(x[c-1])-abs(x[a-1]))*p
    if ((x[d-1] > 0 and x[c-1] < 0) or (x[d-1] < 0 and x[c-1] > 0)):
        time_c_to_d = abs(abs(x[c-1])+abs(x[d-1]))*q
    else:
        time_c_to_d = abs(abs(x[c-1])-abs(x[d-1]))*q
    if ((x[d-1] > 0 and x[b-1] < 0) or (x[d-1] < 0 and x[b-1] > 0)):
        time_to_b = abs(abs(x[b-1])+abs(x[d-1]))*p
    else:
        time_to_b = abs(abs(x[b-1])-abs(x[d-1]))*p
    if(abs(abs(time_to_c > y))):
        print ("{}".format(time_p))
    elif(time_p < time_to_c + (y - time_to_c) + time_c_to_d+time_to_b):
        print ("{}".format(time_p))
    else:
        print ("{}".format(time_to_c + (y - time_to_c) + time_c_to_d+time_to_b))
    i -= 1