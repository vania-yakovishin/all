list = [10, 20, 30, 40, 50]
while True:
    try:
        index = int(input("Введіть індекс елемента, який ви хочете отримати: "))
        if index < 0 or index >= len(list):
            raise IndexError("Введений індекс виходить за межі списку")
        print("Елемент з індексом", index, ":", list[index])
        break
    except ValueError:
        print("Будь ласка, введіть ціле число")
    except IndexError as e:
        print(e)