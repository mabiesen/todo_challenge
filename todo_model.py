import datetime
import time


class TodoItem():
    
    def __init__(self,todo="",creationdate="",creationtime=""):
        self.todo = todo
        self.creationdate = creationdate
        self.creationtime = creationtime
        self.validate_data()

    def validate_data(self):
        if len(self.todo) < 4 or self.todo.upper() == "NULL":
           raise Exception("Todo item doesnt look real,\n"
				"todo is %s"%(self.todo))
         
        now = datetime.datetime.now() 
        if self.creationdate == "":
            self.creationdate = now.strftime("%Y%m%d")
        if self.creationtime == "":
            self.creationtime = now.strftime("%H%M%S")

        
 
