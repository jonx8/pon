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


if __name__ == '__main__':
    a = Polynome("-4/3 7/5 13/2 -5/3 2/4")
    b = Polynome("3/2 -13/7 -5/2")
    k = int(input())
    print(a)
    print(LED_P_Q(a))
    print(DEG_P_N(a))
    print(MUL_Pxk_P(a, k))
