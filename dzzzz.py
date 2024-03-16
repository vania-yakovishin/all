def Calculate():
    def Calculate2(expression):
        print(int(eval(expression)))
    return Calculate2
Calculator = Calculate()
Calculator(input('ведіть приклад: '))