from etl import pg
from main import target_cnx


def test_songplays():
    """
        Fact table - songplays
    """
    try:
        cur = pg.cursor()
        cur.execute('select songplay_id from songplays limit 1);')
        assert cur.rowcount == 1
    except (Exception, pg.DatabaseError) as error:
        print(f'{error}')
    finally:
        cur.close()


def test_users():
    """
        Dimension table - users
    """
    pass


def test_songs():
    """
        Dimension table - songs
    """
    pass


def test_artists():
    """
        Dimension table - artists
    """
    pass


def test_time():
    """
        Dimension table - time
    """
    pass


if __name__ == "__main__":
    test_songplays()
    if target_cnx is not None:
        target_cnx.close()
