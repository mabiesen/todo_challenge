import datetime
import time


class TodoItem():
    
    def __init__(self,todo="",creationdate="",
		 creationtime=""):
        self.todo = todo
        self.creationdate = creationdate
        self.creationtime = creationtime
        self.validate_data()

    def validate_data(self):
        '''
inputs: none
outputs: none
Purpose: Throw an error if data is invalid
Note: throwing error here means view did not control input,
which it should for real time feedback.
'''
        if isinstance(self.todo, int):
            raise Exception("Integer is not allowed for todo")
        if len(self.todo) < 4 or self.todo.upper() == "NULL":
           raise Exception("Todo item doesnt look real,\n"
				"todo is %s"%(self.todo))
         
        now = datetime.datetime.now() 
        if self.creationdate == "":
            self.creationdate = now.strftime("%Y%m%d")
        if self.creationtime == "":
            self.creationtime = now.strftime("%H%M%S")

        if not time.strptime(self.creationdate, "%Y%m%d"):
            raise Exception("Date provided in incorrect format")
        if not time.strptime(self.creationtime, "%H%M%S"):
            raise Exception("Time provided in incorrect format")
 
