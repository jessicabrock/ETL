# WORK IN PROGRESS

import pandas as pd
import os
import json


root_song = 'data/song_data/A'
root_log = 'data/log_data/2018/11'


def get_data():
    for subdir, dirs, files in os.walk(root_song):
        for file in files:
            parsed = json.loads(file)
            print(json.dumps(parsed, indent=4, sort_keys=True))

# STOPPED HERE


# postgres_extract = ('''
#   SELECT column_1, column_2, column_3
#   FROM postgres_table
# ''')

# postgres_insert = ('''
#   INSERT INTO table (column_1, column_2, column_3)
#   VALUES (?, ?, ?)
# ''')

# # exporting queries


# class SqlQuery:
#     def __init__(self, extract_query, load_query):
#         self.extract_query = extract_query
#         self.load_query = load_query


# # create instances for SqlQuery class
# postgres_query = SqlQuery(postgres_extract, postgres_insert)

# # store as list for iteration
# postgres_queries = [postgres_query]
