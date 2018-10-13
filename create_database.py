import sqlite3
import subprocess

def is_sqlite3_installed():
    x = subprocess.check_output(["sqlite3","--version"])
    if "NOT" in x.upper():
        raise Exception("SQLite must be installed") 

def create_todo_database():
    conn = sqlite3.connect('Todo.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE TodoList
		 (Todo text, CreationTime text, CreationDate text)''')

def remove_todo_database():
    try:
        _ = subprocess.check_output(['rm','Todo.db'])
    except:
        print("error removing database, it probably doesn't exist")

def confirm_database_creation():
    output = subprocess.check_output('ls')
    if "Todo.db" in output:
         pass
    else:
         print("Todo.db does not appear to be created!!")

if __name__ == "__main__" or __name__ == "install":
    remove_todo_database()
    create_todo_database()
    confirm_database_creation()
