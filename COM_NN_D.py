def COM_NN_D(a, b):  # Функция N-1 Виноградов А.С.
    if len(a) == len(b):  # Алгоритм функции: поиск сначало элемента большего по длине, далее по величине каждого элемента
        for i in range(len(a)):
            if a[i] > b[i]:
                return 1
            elif a[i] < b[i]:
                return 2
        return 0
    elif len(a) > len(b):
        return 1
    else:
        return 2
