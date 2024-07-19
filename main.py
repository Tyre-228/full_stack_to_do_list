from app.models.users import Users
from app.models.tasks import Tasks

users = Users()
tasks = Tasks()


if __name__ == '__main__':
    print(tasks.deleteTask(26))