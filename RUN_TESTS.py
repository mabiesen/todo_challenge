import test_create_database
import test_todo_model
import subprocess

output = subprocess.check_output(["ls","-la"])
if ".swp" in output:
    raise Exception("Not all files have been properly saved")

x = "==============================================="
print("RUNNING ALL TESTS")
test_create_database.run()
print(x)
test_todo_model.run()
print(x)
