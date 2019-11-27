# WORK IN PROGRESS

import pandas as pd
import os


postgres_extract = ('''
  SELECT column_1, column_2, column_3
  FROM postgres_table
''')

postgres_insert = ('''
  INSERT INTO table (column_1, column_2, column_3)
  VALUES (?, ?, ?)
''')

# exporting queries


class SqlQuery:
    def __init__(self, extract_query, load_query):
        self.extract_query = extract_query
        self.load_query = load_query


# create instances for SqlQuery class
postgres_query = SqlQuery(postgres_extract, postgres_insert)

# store as list for iteration
postgres_queries = [postgres_query]
