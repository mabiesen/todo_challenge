import sqlite3

def create_todo_database():
    conn = sqlite3.connect('Todo.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE TodoList
		 (Todo text, CreationTime text, CreationDate text)''')




if __name__ == "__main__":
    create_todo_database()
