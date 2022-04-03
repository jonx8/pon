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
        """Возвращает строковое представление коэффициентов. Таланков Влад."""
        str_out = []
        for i in self.C:
            str_out.append(str(i))
        return ' '.join(str_out)


def LED_P_Q(polynome):
    """Старший коэффициент многочлена. Таланков Влад."""
    return polynome.C[0]


def DEG_P_N(polynome):
    """Степень многочлена. Таланков Влад."""
    return polynome.m


def MUL_Pxk_P(a, k):
    """Умножение на x^k. Угрюмов Михаил."""
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
