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


if __name__ == '__main__':
    a = Natural('44')
    b = Natural('35')
    # Если вам нужно число без цифр длиной ноль, передайте пустую строку
    c = Natural('')
    print(COM_NN_D(a, b))
