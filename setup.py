import psycopg2

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

con = psycopg2.connect(user='postgres', password='postgres')

con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

cursor = con.cursor()

name_Database = "targetxdb"

sqlCreateDatabase = f"create database {name_Database};"

sqlCreateTable = f"""
CREATE TABLE message (
    id serial PRIMARY KEY,
    sender VARCHAR ( 50 ) NOT NULL,
    receiver VARCHAR ( 50 ) NOT NULL,
    timestamp INT NOT NULL,
    text TEXT,
    uuid uuid
);
"""

if __name__ == '__main__':
    try:
        cursor.execute(sqlCreateDatabase)
    except Exception as e:
        print(e)
    cursor.close()
    con.close()
    con = psycopg2.connect(
        user='postgres', password='postgres',
        dbname='targetxdb'
    )
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = con.cursor()
    try:
        cursor.execute(sqlCreateTable)
    except Exception as e:
        print(e)
    cursor.close()
    con.close()
