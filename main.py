#!/usr/bin/env python3
# coding=utf-8

# Программа получает ввод чисел X A B C D, затем выводит значение Y согласно
# y = (((a * a) * c) + ((b * b)- d))/ (x) если x <= 5
# y = ((x * x) + 5) если x > 5
def main():
    try:
        a = float(input("Введите A: "))
        b = float(input("Введите B: "))
        c = float(input("Введите C: "))
        d = float(input("Введите D: "))
        x = float(input("Введите X: "))
        if x <= 5:
            y = (((a * a) * c) + ((b * b)- d))/ (x)
        else:
            y = ((x * x) + 5)
        print("y = %.2f" % y)
    except ValueError:
        print("Неверные входные данные!")
    except ArithmeticError:
        print("Нет решения!")


if __name__ == "__main__":
    main()
    input("Нажмите Enter для выхода")
