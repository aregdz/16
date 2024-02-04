#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def select(command, aircrafts):
    """""
    Функция для получения номера рейса и пункта назначения по заднному типу самолёта.
    """
    # Разбить команду на части для выделения номера года.
    parts = command
    # Проверить сведения работников из списка.
    count = 0

    for i in aircrafts:
        for k, v in i.items():

            if v == parts:
                print("Пункт назначения - ", i["name"])
                print("Номер рейса - ", i["number"])
                count += 1
    # Если счетчик равен 0, то работники не найдены.

    if count == 0:
        print("Рейс с заданным типом самолёта не найден.")