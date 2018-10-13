import create_database as cd

def test_is_sqlite3_installed():
    print("\nTest for sqlite3 install\n")
    assert(cd.is_sqlite3_installed())
    print("\nPASSED - sqlite is installed")

def test_db_creation_destruction():
    print("\nTest for database creation/destruction\n")
    cd.remove_todo_database()
    cd.create_todo_database()
    assert(cd.confirm_database_creation())
    cd.remove_todo_database()
    assert not (cd.confirm_database_creation())
    print("\nPASSED - Test database creation/destruction complete\n")
   
def run():
    x = "-----------------------------"
    print("\nRUNNING DATABASE CREATION TESTS")
    test_is_sqlite3_installed()  
    print(x)
    test_db_creation_destruction()
    print(x)

if __name__ == "__main__":
    run()
