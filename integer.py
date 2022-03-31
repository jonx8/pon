class Integer():
    def __init__(self, num=""):
        """Принимает строку, выдает целое число. Малых Андрей"""
        if len(num) > 0:
            if num[0] == '-':
                self.b = 1
                num = num[1:]
            else:
                self.b = 0
        else:
            self.b = 0
        self.A = [int(i) for i in num]
        self.n = len(num)
