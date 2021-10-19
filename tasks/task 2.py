#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
в основной ветке программы вызывается функция cylinder(),
которая вычисляет площадь цилиндра.
В теле cylinder() определена функция circle(),
вычисляющая площадь круга по формуле. В теле cylinder() у пользователя
спрашивается, хочет ли он получить только площадь боковой поверхности,
которая вычисляется по формуле, или полную площадь цилиндра. В последнем
случае к площади боковой поверхности цилиндра должен
добавляться удвоенный результат вычислений функции circle().
"""

import sys
import math


# Функция вычисляет площадь цилиндра
def cylinder(radius, height, pick):

    # Вычисляет площадь круга
    def cylinder_circle(r):
        circle = math.pi * r ** 2
        return circle

    # Вычисляет боковую сторону цилиндра
    def cylinder_side(r, h):
        side = 2 * math.pi * r * h
        return side

    # Вычисляет площадь всего цилиндра
    def full_cylinder(r, h):
        full = cylinder_side(r, h) + cylinder_circle(r) * 2
        return full

    # Если выбор 1
    if pick == 1:
        print("Площадь всего цилиндра равна:")
        print(full_cylinder(radius, height))

    # Если выбор 2
    elif pick == 2:
        print("Площадь боковой стороны цилиндра равна:")
        print(cylinder_side(radius, height))

    # Недопустимый выбор
    else:
        print("Введено недопустимое значение", file=sys.stderr)
        exit(1)


if __name__ == '__main__':

    # Запрос радиуса и высоты
    rad = float(input("Введите радиус: "))
    hei = float(input("Введите высоту: "))

    # Запрос выбора
    print("Вычислить площадь всего цилиндра или только боковой стороны?")
    print("1 - всего цилиндра, 2 - только боковой стороны")
    choice = int(input())

    cylinder(rad, hei, choice)
