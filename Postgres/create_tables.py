from Postgres.etl import pg
from Postgres.db_credentials import datawarehouse_db_config


def all_tables():
    """
        create all tables for the datawarehouse
    """
    try:
        conn = pg.connect(**datawarehouse_db_config)
    except (Exception, pg.DatabaseError) as error:
        print(f"{error}")

    cur = conn.cursor()
    conn.set_session(autocommit=True)

    # create dimension table users
    commands = (
        # timestamps of records in songplays broken down into specific units
        """
        CREATE TABLE IF NOT EXISTS time (
            start_time timestamp,
            hour VARCHAR(2) NOT NULL,
            day  VARCHAR(10) NOT NULL,
            week VARCHAR(10) NOT NULL,
            month VARCHAR(15) NOT NULL,
            year VARCHAR(4) NOT NULL,
            weekday VARCHAR(10) NOT NULL,
            PRIMARY KEY start_time
        )
        """,
        # artists in music database
        """
        CREATE TABLE IF NOT EXISTS artists (
            artist_id VARCHAR(25),
            name VARCHAR(50) NOT NULL,
            location VARCHAR(35) NOT NULL,
            latitude NUMERIC, NOT NULL
            longitude NUMERIC NOT NULL
            PRIMARY KEY artist_id
        )
        """,
        # songs in music database
        """
        CREATE TABLE IF NOT EXISTS songs (
            song_id VARCHAR(25),
            title VARCHAR(50),
            artist_id VARCHAR(25) NOT NULL,
            year SMALLINT NOT NULL,
            duration NUMERIC NOT NULL,
            PRIMARY KEY song_id
            FOREIGN KEY artist_id
                REFERENCES artists (artist_id)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        # users in app
        """
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER,
            first_name VARCHAR(35),
            last_name VARCHAR(35),
            gender CHAR(1),
            level VARCHAR(10),
            PRIMARY KEY user_id
        )
        """,
        # records in log data associated with song plays
        """
        CREATE TABLE IF NOT EXISTS songplays (
            songplay_id,
            start_time,
            user_id,
            level,
            song_id,
            artist_id,
            session_id,
            location,
            user_agent,
            PRIMARY KEY songplay_id

        )
        """
    )
