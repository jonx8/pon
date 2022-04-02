from rational import Rational


class Polynome:
    def __init__(self, number=""):
        """Принимает строку, в которой записана дробь
            в виде a/b, выдает рациональное число. Таланков Влад."""
        number = number.strip()
        self.C = []
        number = number.split(' ')
        self.m = len(number) - 1  # степень многочлена
        for i in range(self.m + 1):
            self.C.append(Rational(number[self.m - i]))  # массив с рац. числами

    def __str__(self):
        """Возвращает строковое представление числа
            с x^n и знаками. Таланков Влад."""
        str_out = ""
        for i in range(self.m + 1):
            if (i == 0) or self.C[self.m - i].numer.b:
                str_out = str_out + str(self.C[self.m - i]) + 'x^' + str(self.m - i)
            else:
                str_out = str_out + '+' + str(self.C[self.m - i]) + 'x^' + str(self.m - i)
        return str_out


def LED_P_Q(polynome):
    return polynome.C[polynome.m]  # возвращает старший коэффициент многочлена


def DEG_P_N(polynome):
    return polynome.m  # возвращает степень многочлена


if __name__ == '__main__':
    a = Polynome("-4/3 7/5 13/2 -5/3 2/4")
    b = Polynome("3/2 -13/7 -5/2")

    print(a)
    print(LED_P_Q(a))
    print(DEG_P_N(a))
