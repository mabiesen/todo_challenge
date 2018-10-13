import datetime
import time


class TodoItem():
    
    def __init__(self,todo="",creationdate="",creationtime=""):
        self.todo = todo
        self.creationdate = creationdate
        self.creationtime = creationtime
        validate_data()

    def validate_data():
        if len(self.todo) < 4 or self.todo.upper() == "NULL":
           raise Exception("Todo item doesnt look real,\n"
				"todo is %s"%(self.todo))
         
        now = datetime.datetime.now() 
        if self.creationdate == "":
            self.creationdate = time.strftime(now,"%Y%M%D")
        if self.creationtime == "":
            self.creationtime = time.strftime(now,"%h%m%s")

        
 
