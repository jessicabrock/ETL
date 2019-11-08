import os


datawarehouse_db_config = {
    "host": 'localhost',
    "database": f"{os.environ['datawarehouse_name']}",
    "user": 'postgres',
    "password": 'postgres'
}

source_db_config = {
    "host": 'localhost',
    "database": 'emps',
    "user": 'postgres',
    "password": 'postgres'
}
