import json
import sqlite3

con = sqlite3.connect('db.sqlite3')
cur = con.cursor()

sql_query = """
            INSERT INTO categories_categories
            VALUES (?, ?)
            """

sql_query_ads = """
                INSERT INTO ads_ads
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """

with open('datasets/categories.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    for i in data:
        data_i = [
            i['id'],
            i['name']
        ]
        with con:
            cur.execute(sql_query, data_i)

with open('datasets/ads.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    for i in data:
        data_i = [
            i['id'],
            i['name'],
            i['author'],
            i['price'],
            i['description'],
            i['address'],
            i['is_published']
        ]
        with con:
            cur.execute(sql_query_ads, data_i)
