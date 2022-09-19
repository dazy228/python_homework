# Реализовать функцию, которая выведет FirstName из таблицы customers и кол-во их вхождений в таблицу.

import sqlite3


def get_customers():
    with sqlite3.connect('chinook.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT FirstName, COUNT(FirstName) FROM customers GROUP BY FirstName')
        return cursor.fetchall()


print(get_customers())