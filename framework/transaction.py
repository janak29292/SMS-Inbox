import psycopg2
from psycopg2 import extras

config = {
    'user': 'postgres',
    'password': 'postgres',
    'dbname': 'targetxdb'
}

# Open a cursor to perform database operations


def run_query(query):
    def wrap(*args, **kwargs):
        conn = psycopg2.connect(**config)
        cur = conn.cursor(cursor_factory=extras.RealDictCursor)
        cur.execute(query(*args, **kwargs))
        try:
            response = cur.fetchall()
        except:
            response = None
        conn.commit()
        cur.close()
        conn.close()
        return response
    return wrap
