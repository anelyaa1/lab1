import psycopg2
from config import config


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        DROP TABLE IF EXISTS phones CASCADE;
        CREATE TABLE phones (
            phone_id SERIAL PRIMARY KEY,
            phone_name VARCHAR(255) NOT NULL
        )
        """,
        """ CREATE TABLE names (
                names_id SERIAL PRIMARY KEY,
                names_name VARCHAR(255) NOT NULL
                CONSTRAINT fk_phonebooks
                FOREIGN KEY(phonebook_id)
                REFERENCES phonebooks(id)
        )
        """)
    
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()
