#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def add1():
    """"
    Функция для добавления информации о новых рейсах
    """
    # Запросить данные о работнике.
    name = input("Название пункта назначения рейса? ")
    number = int(input("Номер рейса? "))
    tip = input("Тип самолета? ")
    # Создать словарь.
    i = {
        'name': name,
        'number': number,
        'tip': tip,
    }

    return i