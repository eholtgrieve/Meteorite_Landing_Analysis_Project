#!/usr/bin/python3

import config
import sqlalchemy

database = 'meteorite'

engine = sqlalchemy.create_engine(f'postgresql://{config.username}:{config.password}@localhost:5432/{database}')

connection = engine.connect()

query = sqlalchemy.text("SELECT * FROM meteorites")
data = engine.execute(query)


for record in data:
    print(record)