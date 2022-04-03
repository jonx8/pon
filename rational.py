from naturals import Natural
from integer import Integer


class Rational:
    def __init__(self, number=""):
        """Принимает строку, в которой записана дробь
           в виде a/b, выдает рациональное число. Малых Андрей."""
        number = number.strip().split('/')
        number.append('')

        self.numer = Integer(number[0])  # Числитель
        self.denom = Natural(number[1])  # Знаменатель

    def __str__(self):
        """Возвращает строковое представление числа. Малых Андрей."""
        if self.denom.A == [1] or self.numer.A == [0] or not self.denom.A:
            return str(self.numer)
        return str(self.numer) + '/' + str(self.denom)


def INT_Q_B(a):
    """Проверка на целое. Если рациональное число является целым, то True, иначе False. Щелочкова Екатерина."""
    if a.denom.A[0] == 1 and a.denom.n == 1:
        return True
    return False


def TRANS_Q_Z(a):
    """Преобразование дробного в целое(если знаменатель равен 1). Щелочкова Екатерина."""
    if a.denom.A[0] == 1 and a.denom.n == 1:
        return a.numer


def TRANS_Z_Q(с):
    """Преобразование целого в дробное. Щелочкова Екатерина."""
    a.numer = с
    a.denom = Natural('1')
    return a


if __name__ == '__main__':
    # Создание чисел:
    a = Rational("-65/32")
    b = Rational("0/53")
    c = Rational("63/1")
    d = Integer("54")

    print(a.denom.A)  # Вывод цифр знаменателя
    print(a.numer.b)  # Вывод знака числителя
    print(INT_Q_B(a))
    print(TRANS_Q_Z(c))
    print(TRANS_Z_Q(d))
