#!/usr/bin/env python

import psycopg2
from psycopg2 import Error
import itertools

try:
    connection = psycopg2.connect(user="alex",
                                  password="Peaks",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="vk-bot")

    cursor = connection.cursor()

    cursor.execute("SELECT name FROM category")
    categories = list(itertools.chain(*cursor.fetchall()))

    cursor.execute("SELECT name FROM goods WHERE category_id='1'")
    cat1 = list(itertools.chain(*cursor.fetchall()))

    cursor.execute("SELECT name FROM goods WHERE category_id='2'")
    cat2 = list(itertools.chain(*cursor.fetchall()))

    cursor.execute("SELECT name FROM goods WHERE category_id='3'")
    cat3 = list(itertools.chain(*cursor.fetchall()))

    cursor.execute("SELECT description FROM goods")
    descriptions = list(itertools.chain(*cursor.fetchall()))

    cursor.execute("SELECT name FROM goods")
    names = list(itertools.chain(*cursor.fetchall()))

    cursor.execute("SELECT image FROM goods ORDER BY image")
    images = list(itertools.chain(*cursor.fetchall()))

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
