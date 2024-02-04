#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from python_func import *

if __name__ == '__main__':
    help1.help1()
    # Список работников.
    aircrafts = []
    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()
        # Выполнить действие в соответствие с командой.

        match command:
            case 'exit':
                break

            case 'add':
                # Добавить словарь в список.
                i = add1.add1()
                aircrafts.append(i)
                # Отсортировать список в случае необходимости.
                if len(aircrafts) > 1:
                    aircrafts.sort(key=lambda item: item.get('name', ''))

            case 'list':
                list.list(aircrafts)

            case 'select':
                i = input('Введите тип:')
                select.select(i, aircrafts)

            case 'help':
                help1.help1()

            case _:
                error1.error1(command)
