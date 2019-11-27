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
            songplay_id SERIAL,
            start_time TIMESTAMP,
            user_id INTEGER,
            level VARCHAR(10),
            song_id VARCHAR(25),
            artist_id VARCHAR(25),
            session_id INTEGER,
            location VARCHAR(35),
            user_agent VARCHAR(512),
            PRIMARY KEY songplay_id,
            FOREIGN KEY start_time
                REFERENCES time(start_time)
                ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY user_id
                REFERENCES users(user_id)
                ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY level
                REFERENCES users(level)
                ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY song_id
                REFERENCES songs(song_id)
                ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY artist_id
                REFERENCES artists(artist_id)
                ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY location
                REFERENCES artists(location)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
    )

    try:
        for command in commands:
            cur.execute(command)
        cur.close()
    except (Exception, pg.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    if __name__ == '__main__':
        all_tables()
