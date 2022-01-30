#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 09:05:08 2022

@author: lenovo
"""

# pip install cryptocompare
import cryptocompare
import datetime
import sqlite3


def btc_price():
    btc_price = (cryptocompare.get_price('BTC', currency='USD')['BTC']['USD'])
    return btc_price


def date():
    data = (datetime.date.isoformat(datetime.date.today()))
    return data


def sql_connector(path):
    cnx = sqlite3.connect(path)
    corsor = cnx.cursor()
    return cnx, corsor


def create_table(cnx, cursor):
    query = 'CREATE TABLE IF NOT EXISTS btc (date text, price int);'
    cursor.execute(query)
    cnx.commit()


def insert_data(date, price):
    query = "INSERT INTO btc VALUES (\'%s\', \'%s\')"%(date, price)
    cursor.execute(query)
    cnx.commit()


path = 'Bitcoin.db'
cnx, cursor = sql_connector(path)
create_table(cnx, cursor)
price = btc_price()
date = date()
insert_data(date, price)
