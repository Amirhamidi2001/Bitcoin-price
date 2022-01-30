#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 13:16:02 2022

@author: lenovo
"""

import sqlite3

def sql_connector(path):
    cnx = sqlite3.connect(path)
    corsor = cnx.cursor()
    return cnx, corsor

    
def create_table(cnx, cursor):
    query = "CREATE TABLE IF NOT EXISTS person (id integer PRIMARY KEY, name text, age int);"
    cursor.execute(query)
    cnx.commit()


def insert_data(cnx, cursor):
    query = "INSERT INTO person VALUES(3, 'ali', 20);"
    cursor.execute(query)
    cnx.commit()

path = 'mydatabase.db'
cnx, cursor = sql_connector(path)
create_table(cnx, cursor)
insert_data(cnx, cursor)
