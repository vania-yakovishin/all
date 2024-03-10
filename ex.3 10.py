while True:
    try:
        num_str = input("Введіть число: ")
        num = float(num_str)
        print("Введене число:", num)
        break
    except ValueError:
        print("Введене значення не може бути перетворено у число. Будь ласка, спробуйте знову.")
