while True:
    try:
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))
        if num2 == 0:
            raise ZeroDivisionError("Друге число не може бути нулем")
        result = num1 / num2
        print("Результат ділення:", result)
        break
    except ValueError:
        print("Будь ласка, введіть числа")
    except ZeroDivisionError as e:
        print(e)