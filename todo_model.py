import datetime
import time


class TodoItem():
    
    def __init__(self,todo,creationdate="",creationtime=""):
        self.todo = todo
        if creationdate == "" or creationtime == "":
            now = datetime.datetime.now()
            self.creationdate = time.strftime(now,"%Y%M%D")
            self.creationtime = time.strftime(now,"%h%m%s")
        else:
            self.creationdate = creationdate
            self.creationtime = creationtime

    def validate_data():
        if len(self.todo) < 4:
           raise Exception("Todo item doesnt look real, name of todo less than 4 letters")
          
        pass
