from Postgres.etl import pg
from Postgres.db_credentials import datawarehouse_db_config


def test_songplays():
    """
        Fact table - songplays
    """
    try:
        conn = pg.connect(**datawarehouse_db_config)
        cur = conn.cursor()
        cur.execute('select songplay_id from songplays limit 1);')
        assert cur.rowcount == 1
    except (Exception, pg.DatabaseError) as error:
        print(f'{error}')
    finally:
        cur.close()
        conn.close()


def test_users():
    """
        Dimension table - users
    """
    try:
        conn = pg.connect(**datawarehouse_db_config)
        cur = conn.cursor()
        cur.execute('select user_id from users limit 1);')
        assert cur.rowcount == 1
    except (Exception, pg.DatabaseError) as error:
        print(f'{error}')
    finally:
        cur.close()
        conn.close()


def test_songs():
    """
        Dimension table - songs
    """
    try:
        conn = pg.connect(**datawarehouse_db_config)
        cur = conn.cursor()
        cur.execute('select song_id from songs limit 1);')
        assert cur.rowcount == 1
    except (Exception, pg.DatabaseError) as error:
        print(f'{error}')
    finally:
        cur.close()
        conn.close()


def test_artists():
    """
        Dimension table - artists
    """
    try:
        conn = pg.connect(**datawarehouse_db_config)
        cur = conn.cursor()
        cur.execute('select artist_id from artists limit 1);')
        assert cur.rowcount == 1
    except (Exception, pg.DatabaseError) as error:
        print(f'{error}')
    finally:
        cur.close()
        conn.close()


def test_time():
    """
        Dimension table - time
    """
    try:
        conn = pg.connect(**datawarehouse_db_config)
        cur = conn.cursor()
        cur.execute('select start_time from time limit 1);')
        assert cur.rowcount == 1
    except (Exception, pg.DatabaseError) as error:
        print(f'{error}')
    finally:
        cur.close()
        conn.close()
