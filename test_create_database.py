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
    print("\n PASSED - Test database creation/destruction complete\n")
   
def run():
    test_is_sqlite3_installed()  
    test_db_creation_destruction()

if __name__ == "__main__":
    run()
