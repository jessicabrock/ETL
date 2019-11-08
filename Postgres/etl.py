import psycopg2 as pg
import os


def etl(query, source_cnx, target_cnx):
    # extract data from source db
    source_cursor = source_cnx.cursor()
    source_cursor.execute(query.extract_query)
    data = source_cursor.fetchall()
    source_cursor.close()

    # load data into warehouse db
    if data:
        target_cursor = target_cnx.cursor()
        target_cursor.execute(f"USE {os.environ['datawarehouse_name']}")
        target_cursor.executemany(query.load_query, data)
        print('data loaded to warehouse db')
        target_cursor.close()
    else:
        print('data is empty')


def etl_process(queries, target_cnx, source_db_config, db_platform):
    # establish source db connection
    try:
        if db_platform == 'postgres':
            source_cnx = pg.connect(**source_db_config)
    except (Exception, pg.DatabaseError) as error:
        print(f"{error}")

    # loop through sql queries
    for query in queries:
        etl(query, source_cnx, target_cnx)

    # close the source db connection
    if source_cnx is not None:
        source_cnx.close()
