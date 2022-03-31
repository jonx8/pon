import COM_NN_D


def ADD_NN_N(a, b): #Функция N-4 Виноградов А.С.
    D = COM_NN_D(a, b) #Алгоритм функции:
    mind = 0
    if D == 0 or D == 1:
        c1 = [0] * (len(a) + 1)
        c2 = [0] * (len(a))
    else:
        c1 = [0] * (len(b) + 1)
        c2 = [0] * (len(b))
    a.reverse()
    b.reverse()
    for i in range(len(b)):
        if a[i] + b[i] <=9 and mind == 0:
            c1[i] = a[i] + b[i]
        elif a[i] + b[i] > 9 and mind == 0:
            c1[i] = (a[i] + b[i])%10
            mind = (a[i] + b[i])//10
        elif mind == 1:
            if a[i] + b[i] + mind <= 9:
                c1[i] = a[i] + b[i] + mind
                mind = 0
            else:
                c1[i] = (a[i] + b[i] + mind) % 10
                mind = (a[i] + b[i] + mind) // 10
    if mind != 0 and (D == 0 or D == 1):
        c1[len(a)] = mind
        c1.reverse()
        return c1
    elif mind != 0 and D == 2:
        c1[len(b)] = mind
        c1.reverse()
        return c1
    elif mind == 0 and (D == 0 or D == 1):
        for i in range(len(a)):
            c2[i] = c1[i]
        c2.reverse()
        return c2
    elif mind == 0 and D == 2:
        for i in range(len(b)):
            c2[i] = c1[i]
        c2.reverse()
        return c2
