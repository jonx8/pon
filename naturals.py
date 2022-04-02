class Natural:
    def __init__(self, number):
        """Принимает строку, выдает натуральное число, Смирнов Иван"""
        self.A = list(int(i) for i in number)
        self.n = len(self.A)

    def __str__(self):
        """Возвращает строковое представление числа. Малых Андрей"""
        return "".join(map(str, self.A))


def COM_NN_D(a, b):
    """Сравнение натуральных чисел: 2 - если первое больше второго, 0, если равно, 1 иначе. Андрей Виноградов"""
    a.A.reverse()
    b.A.reverse()
    if a.n == b.n:
        for i in range(a.n):
            if a.A[i] > b.A[i]:
                return 2
            elif a.A[i] < b.A[i]:
                return 1
        return 0
    elif a.n > b.n:
        return 2
    else:
        return 1


def ADD_NN_N(a, b):
    """Сложение натуральных чисел. Андрей Виноградов"""
    Ifer = COM_NN_D(a, b)
    a.A.reverse()
    b.A.reverse()
    mind = 0
    D = Natural("")
    if Ifer == 0 or Ifer == 2:
        c1 = [0] * (a.n + 1)
        c2 = [0] * a.n
        last = (b.n) - 1
        for i in range (a.n):
            if i>last:
                if mind != 0:
                    c1[i] = a.A[i] + mind
                    mind = 0
                else:
                    c1[i] = a.A[i]
            else:
                if a.A[i] + b.A[i] <= 9 and mind == 0:
                    c1[i] = a.A[i] + b.A[i]
                elif a.A[i] + b.A[i] > 9 and mind == 0:
                    c1[i] = (a.A[i] + b.A[i]) % 10
                    mind = (a.A[i] + b.A[i]) // 10
                elif mind == 1:
                    if a.A[i] + b.A[i] + mind <= 9:
                        c1[i] = a.A[i] + b.A[i] + mind
                        mind = 0
                    else:
                        c1[i] = (a.A[i] + b.A[i] + mind) % 10
                        mind = (a.A[i] + b.A[i] + mind) // 10
        if mind != 0:
            c1[a.n] = mind
            c1.reverse()
            D.A = c1
            D.n = b.n
        else:
            for i in range(a.n):
                c2[i] = c1[i]
            c2.reverse()
            D.A = c2
            D.n = a.n
    else:
        c1 = [0] * (b.n + 1)
        c2 = [0] * b.n
        last = (a.n) - 1
        for i in range(b.n):
            if i>last:
                if mind != 0:
                    c1[i] = b.A[i] + mind
                    mind = 0
                else:
                    c1[i] = b.A[i]
            else:
                if a.A[i] + b.A[i] <= 9 and mind == 0:
                    c1[i] = a.A[i] + b.A[i]
                elif a.A[i] + b.A[i] > 9 and mind == 0:
                    c1[i] = (a.A[i] + b.A[i]) % 10
                    mind = (a.A[i] + b.A[i]) // 10
                elif mind == 1:
                    if a.A[i] + b.A[i] + mind <= 9:
                        c1[i] = a.A[i] + b.A[i] + mind
                        mind = 0
                    else:
                        c1[i] = (a.A[i] + b.A[i] + mind) % 10
                        mind = (a.A[i] + b.A[i] + mind) // 10
        if mind != 0:
            c1[b.n] = mind
            c1.reverse()
            D.A = c1
            D.n = b.n
        else:
            for i in range(b.n):
                c2[i] = c1[i]
            c2.reverse()
            D.A = c2
            D.n = b.n
    return D


def SUB_NN_N(a, b):
    """Вычитание из первого большего натурального числа второго меньшего или равного. Андрей Виноградов"""
    Ifer = COM_NN_D(a, b)
    D = Natural("")
    if Ifer == 2:
        c = [0] * a.n
        last = (b.n) - 1
        for i in range(a.n):
            k = i + 1
            if i > last:
                c[i] = a.A[i]
            else:
                if a.A[i] >= b.A[i]:
                    c[i] = a.A[i] - b.A[i]

                else:
                    while a.A[k] == 0:
                        a.A[k] = 9
                        k+=1
                    a.A[k] -= 1
                    c[i] = 10 + a.A[i] - b.A[i]
        c.reverse()
        k = 0
        j = 0
        while c[k] == 0:
            k+=1
        ans = [0] * (a.n - k)
        for i in range(k,a.n):
            ans[j] = c[i]
            j+=1
        D.A = ans
        D.n = a.n - k
    elif Ifer == 1:
        c = [0] * b.n
        last = (a.n) - 1
        for i in range(b.n):
            k = i + 1
            if i > last:
                c[i] = b.A[i]
            else:
                if b.A[i] >= a.A[i]:
                    c[i] = b.A[i] - a.A[i]

                else:
                    while b.A[k] == 0:
                        b.A[k] = 9
                        k += 1
                    b.A[k] -= 1
                    c[i] = 10 + b.A[i] - a.A[i]
        c.reverse()
        k = 0
        j = 0
        while c[k] == 0:
            k += 1
        ans = [0] * (b.n - k)
        for i in range(k, b.n):
            ans[j] = c[i]
            j += 1
        D.A = ans
        D.n = b.n - k
    else:
        D.A = '0'
        D.n = 1
    return D


if __name__ == '__main__':
    a = Natural('1895')
    b = Natural('44')
    # Если вам нужно число без цифр длиной ноль, передайте пустую строку
    c = Natural('')
    print(ADD_NN_N(a, b))
