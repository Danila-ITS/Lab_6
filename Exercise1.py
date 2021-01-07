#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решите задачу: создайте словарь, связав его с переменной school , и наполните данными,
# которые бы отражали количество учащихся в разных классах (1а, 1б, 2б, 6а, 7в и т. п.).
# Внесите изменения в словарь согласно следующему: а) в одном из классов изменилось
# количество учащихся, б) в школе появился новый класс, с) в школе был расформирован
# (удален) другой класс. Вычислите общее количество учащихся в школе.
from datetime import date
import sys

if __name__ == '__main__':
    i = 0
    School = {}
    while i < 4:
        name = input("Название класса ")
        quantity = int(input("Количество учащихся "))

        Class = {
            name: quantity,
        }

        print(Class)
        School.update(Class)
        print(School)
        i += 1
    name_change = input("Введите класс в котором нужно прибавить количество учеников ").split()
    change = int(name_change[1])
    School[name_change[0]] += change
    name_del = input("Введите название класса который нужно удалить ")
    School.pop(name_del)

    s = 0
    for item in School.values():
        s += item
    print(School)
    print("Количество учеников во всех классах", s)
