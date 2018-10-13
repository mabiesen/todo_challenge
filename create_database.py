import sqlite3
import subprocess

def create_todo_database():
    conn = sqlite3.connect('Todo.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE TodoList
		 (Todo text, CreationTime text, CreationDate text)''')

def remove_todo_database():
    try:
        _ = subprocess.call(['rm','Todo.db'])
    except:
        print("error removing database, it probably doesn't exist")


if __name__ == "__main__":
    remove_todo_dabase()
    create_todo_database()
