Versions guide

Version example: 0.5.3
1) 0/1 - before/after release
2) 0-inf - update that happens after adding a new feature
3) 0-inf - bug fix, small changes

Commit example: "some changes v0.4.2"


Version history:

0.3.1
An error in users class has been fixed. Method create user(line 50). You don't need command conn.commit().

0.3.0
Tasks class has been created. The class contains these methods:

connect(config): Connects to the PostgreSQL database server using the provided configuration.
getTasks(self): Retrieves all tasks from the tasks table.
getById(self, id): Retrieves a task by its ID from the tasks table.
getByUserId(self, user_id): Retrieves tasks assigned to a specific user by joining the tasks and user_task_relationship tables.
createTask(self, text, user_id): Creates a new task and associates it with a user in the user_task_relationship table.
deleteTask(self, id): Deletes a task by its ID from both the tasks and user_task_relationship tables.
updateTask(self, id, text, completed): Updates the text and completion status of a task by its ID in the tasks table.


0.2.0
Users class has been created. The class contains these methods:

connect(config): Connects to the PostgreSQL database server using the provided configuration.
getUsers(self): Retrieves all users from the database and returns them.
getById(self, id): Retrieves a user by their ID from the database.
createUser(self, name, email, password): Creates a new user in the database with the given name, email, and password.
getId(self, email, password): Retrieves the ID of a user by their email and password from the database.

0.1.0
Database has been initialised. 
App folder that contains all project subfiles has been created.
.gitigrone file has been created.
Virtual envirounment has been created.
Flask and Psycopg2 have been installed

0.0.0
First commit