from rational import Rational


class Polynome:
    def __init__(self, number=""):
        """Принимает строку с коэффециентами через пробел в виде a/b. Таланков Влад."""
        number = number.strip()
        self.C = []
        number = number.split(' ')
        self.m = len(number) - 1  # степень многочлена
        for i in number:
            self.C.append(Rational(i))  # массив с рац. числами

    def frontZerosDel(self):
        """Удаление нулевых коэффициентов перед старшим членом. Малых Андрей"""
        while self.C[0].numer.A == [0] and len(self.C) > 1:
            self.C.pop(0)
        self.m = len(self.C) - 1

    def __str__(self):
        """Возвращает строковое представление многочлена. Малых Андрей."""

        def sign(num):
            """Определяет, какой знак выводить перед членом. Малых Андрей"""
            if num:
                if num == '-':
                    return ''
                else:
                    return '' if num.numer.b else '+'
            return '+'

        def deg(i):
            """Принимает степень икса, возвращает строковое представление x^i. Малых Андрей"""
            if i > 1:
                return f'x^{i}'
            elif i == 1:
                return 'x'
            return ''

        res = ''
        for i in range(self.m, -1, -1):
            j = self.m - i  # Номер коэффициента
            koeff = self.C[j]   # Вид коэффициента при выводе

            if koeff.numer.A == [1] and koeff.denom.A == [1] and i != 0:
                koeff = '-' if koeff.numer.b else ''

            if self.C[j].numer.A != [0]:
                res += sign(koeff) + f'{koeff}{deg(i)}'

        if not res:
            return '0'
        elif res[0] == '+':
            res = res[1:]
        return res


def LED_P_Q(polynome):
    """Старший коэффициент многочлена. Таланков Влад."""
    return polynome.C[0]


def DEG_P_N(polynome):
    """Степень многочлена. Таланков Влад."""
    return polynome.m


def MUL_Pxk_P(a, k):
    """Умножение полинома на x^k. Угрюмов Михаил."""
    a.m = a.m + k
    for i in range(k):
        a.C.append(Rational("0/1"))
    return a


def ADD_PP_P(poly1, poly2):
    """Сложение многочленов. Малых Андрей"""
    if DEG_P_N(poly1) < DEG_P_N(poly2):
        poly1, poly2 = poly2, poly1
    for i in range(DEG_P_N(poly2) + 1):
        poly1.C[i] = ADD_QQ_Q(poly1.C[i], poly2.C[i])
    poly1.frontZerosDel()
    return poly1


def SUB_PP_P(poly1, poly2):
    """Вычитание многочленов. Малых Андрей"""
    if DEG_P_N(poly1) < DEG_P_N(poly2):
        poly1, poly2 = poly2, poly1
    for i in range(DEG_P_N(poly2) + 1):
        poly1.C[i] = SUB_QQ_Q(poly1.C[i], poly2.C[i])
    poly1.frontZerosDel()
    return poly1


def MUL_PQ_P(polynome, num):
    """Умножение многочлена на число. Малых Андрей"""
    for i in range(DEG_P_N(polynome) + 1):
        polynome.C[i] = MUL_QQ_Q(polynome.C[i], num)
    polynome.frontZerosDel()
    return polynome


if __name__ == '__main__':
    a = Polynome("0 0 0")
    a.frontZerosDel()
    print("0000000000")
    for i in a.C:
        print(i)
