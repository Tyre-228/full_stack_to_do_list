import psycopg2
import sys
import os


# Adding the database directory so that I can import load_config function from config module
current_dir = os.path.dirname(os.path.abspath(__file__))
external_modules_path = os.path.join(current_dir, '../database')
if external_modules_path not in sys.path:
    sys.path.insert(0, external_modules_path)


from config import load_config


class Tasks:
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
    
    def getTasks(self):
        with psycopg2.connect(**self.config) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM tasks;")
                record = cursor.fetchall()

                return record
    
    def getById(self, id):
        with psycopg2.connect(**self.config) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"SELECT * FROM tasks WHERE id={str(id)};")
                record = cursor.fetchone()

                return record

    
    def getByUserId(self, user_id):
        with psycopg2.connect(**self.config) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"SELECT tasks.id, tasks.text, tasks.completed FROM tasks INNER JOIN user_task_relationship ON user_task_relationship.task_id = tasks.id WHERE user_task_relationship.user_id = {str(user_id)};")
                record = cursor.fetchall()

                return record

    def createTask(self, text, user_id):
        with psycopg2.connect(**self.config) as conn:
            with conn.cursor() as cursor:
                # insert task in the tasks table
                cursor.execute(f"INSERT INTO tasks(text, completed) VALUES('{text}', 'false');")
                # get id of the task
                cursor.execute(f"SELECT id FROM tasks ORDER BY id DESC LIMIT(1);")
                task_id = cursor.fetchone()[0]
                # insert task and user id into user_task_relationship table
                cursor.execute(f"INSERT INTO user_task_relationship(user_id, task_id) VALUES({str(user_id)}, {str(task_id)});")
    
    def deleteTask(self, id):
        with psycopg2.connect(**self.config) as conn:
            with conn.cursor() as cursor:
                # delete task from tasks table
                cursor.execute(f"DELETE FROM tasks WHERE id = {str(id)};")
                # delete task from user_task_relationship table
                cursor.execute(f"DELETE FROM user_task_relationship WHERE task_id = {str(id)};")
    
    def updateTask(self, id, text, completed):
        with psycopg2.connect(**self.config) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"UPDATE tasks SET text = '{text}', completed = {str(completed)} WHERE id = {id};")