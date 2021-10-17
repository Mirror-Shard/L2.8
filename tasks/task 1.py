#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
основная ветка программы, не считая заголовков функций,
состоит из двух строки кода. Это вызов функции test()
и инструкции  if __name__ ==
'__main__' . В ней запрашивается на ввод целое число.
Если оно положительное, то
вызывается функция positive(), тело которой содержит
команду вывода на экран слова
"Положительное". Если число отрицательное, то вызывается функция negative(),
ее тело содержит выражение вывода на экран слова "Отрицательное".
"""


def positive():
    print("Число положительное")


def negative():
    print("Число отрицательное")


def test(a):
    if a >= 0:
        positive()
    else:
        negative()


if __name__ == '__main__':
    num = float(input("Введите число: "))
    test(num)
