import COM_NN_D


def ADD_NN_N(a,b): #Функция N-4 Виноградов А.С.
    D = COM_NN_D(a, b) #Алгоритм функции: Ищем сначало более длинную цифру, далее соединяем поэлементно при помощи zip
    if D == 1 or D == 0:
        slen = a
    else:
        slen = b
    c = [x + y for x, y in zip(a, b)] + slen[min(len(a), len(b)):]
    return c