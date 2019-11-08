# variables
from db_credentials import datawarehouse_db_config
import sql_queries
# methods
from etl import etl_process, pg


def main():
    print('starting etl')

    # establish connection for target database
    try:
        target_cnx = pg.connect(**datawarehouse_db_config)
    except (Exception, pg.DataError) as error:
        print(f"{error}")

    # loop through credentials
    for config in datawarehouse_db_config:
        try:
            print("loading db: " + config['database'])
            etl_process(sql_queries, target_cnx, config, 'postgres')
        except Exception as error:
            print(f"etl for {config['database']}")
            print(f"{error}")
            continue

    if target_cnx is not None:
        target_cnx.close()


if __name__ == "__main__":
    main()
