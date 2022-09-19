# Реализовать функцию, которая выведет прибыль по таблице invoice_items.

import sqlite3


def get_profit():
    with sqlite3.connect('chinook.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT SUM(UnitPrice * Quantity) FROM invoice_items')
        return cursor.fetchone()[0]


print(get_profit())