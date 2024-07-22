import psycopg2
import sys
import os


# Adding the database directory so that I can import load_config function from config module
current_dir = os.path.dirname(os.path.abspath(__file__))
external_modules_path = os.path.join(current_dir, '../database')
if external_modules_path not in sys.path:
    sys.path.insert(0, external_modules_path)


from config import load_config


class Users:
    def __init__(self):
        self.config = load_config()
    
    def connect(config):
        """ Connect to the PostgreSQL database server """
        try:
            # connecting to the PostgreSQL server
            with psycopg2.connect(**config) as conn:
                print('Connected to the PostgreSQL server.')
                return conn
        except (psycopg2.DatabaseError, Exception) as error:
            print(error)
    
    def getUsers(self):
        with psycopg2.connect(**self.config) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM users ORDER BY id;")
                record = cursor.fetchall()

                return record
    
    def getById(self, id):
        with psycopg2.connect(**self.config) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"SELECT * FROM users WHERE id={str(id)};")
                record = cursor.fetchone()

                return record
    
    def createUser(self, name, email, password):
        with psycopg2.connect(**self.config) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"INSERT INTO users(name, email, password) VALUES('{name}', '{email}', '{password}');")
    
    def getId(self, email, password):
        with psycopg2.connect(**self.config) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"SELECT id FROM users WHERE email='{email}' AND password='{password}';")

                record = cursor.fetchone()

                # if the record exists, convert it from tuple to string
                if record: 
                    record = record[0] 

                return record