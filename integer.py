from naturals import Natural


class Integer:
    def __init__(self, number=""):
        """Принимает строку, выдает целое число. Малых Андрей"""
        self.b = 0
        if len(number) > 0:
            if number[0] == '-':
                self.b = 1
                number = number[1:]
        self.A = [int(i) for i in number]
        self.n = len(number)

    def __str__(self):
        """Возвращает строковое представление числа. Малых Андрей"""
        return ('-' if self.b else '') + "".join(map(str, self.A))


def ABS_Z_N(z):
    """Возвращает абсолютное значение числа(модуль). Максимов Матвей"""
    nat.b = 0
    nat.A = z.A
    return nat


def MUL_ZM_Z(z):
    """Возвращает число с противоположным знаком(т.е умноженное на (-1). Максимов Матвей"""
    if z.b == 1:
        z.b = 0
    else:
        z.b = 1
    return z


def TRANS_N_Z(nat):
    """Преобразует натуральное число в целое. Максимов Матвей"""
    z.b = 0
    z.A = nat.A
    z.n = nat.n
    return z


def TRANS_Z_N(z):
    """Преобразует целое число в натуральное. Максимов Матвей"""
    nat.b = 0
    nat.A = z.A
    nat.n = z.n
    return nat


if __name__ == '__main__':
    z = Integer("-4")
    nat = Natural("6")
    print(z)
    print(ABS_Z_N(z))
    print(MUL_ZM_Z(z))
    print(TRANS_N_Z(nat))
    print(str(TRANS_N_Z(z)))
