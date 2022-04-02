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
