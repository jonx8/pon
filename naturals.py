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
    if a.n == b.n:
        for i in range(a.n):
            if a.A[i] > b.A[i]:
                return 2
            elif a.A[i] < b.A[i]:
                return 1
        return 0
    elif a.n > b.n:
        return 1
    else:
        return 2


def ADD_NN_N(a, b):
    """Сложение натуральных чисел. Андрей Виноградов"""
    Ifer = COM_NN_D(a, b)
    a.A.reverse()
    b.A.reverse()
    mind = 0
    D = Natural("")
    if Ifer == 0 or Ifer == 1:
        c1 = [0] * (a.n + 1)
        c2 = [0] * a.n
        last = b.n - 1
        for i in range(a.n):
            if i > last:
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
        last = a.n - 1
        for i in range(b.n):
            if i > last:
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


a = Natural(input())
b = Natural(input())
c = Natural('')  # Если вам нужно число без цифр длиной ноль, передайте пустую строку
print(str(ADD_NN_N(a, b)))
