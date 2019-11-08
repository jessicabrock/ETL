import etl
from main import main


def test_songplays():
    """
        Fact table - songplays
    """
    try:
        cur = etl.pg.cursor()
        cur.execute('select songplay_id from songplays limit 1);')
        assert cur.rowcount == 1
    except (Exception, etl.pg.DatabaseError) as error:
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
    if main.target_cnx is not None:
        main.target_cnx.close()
