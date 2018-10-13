import todo_model

def test_model_non_text():
    print("\nTesting effect of non-text\n")
    try:
        x = todo_model.TodoItem(9999999999,10101010,10101010)
    except:
        print("Todo creation broke program as expected")
        assert(True)
    print("\nPASSED - Test of non-text\n") 


def test_model_bad_dates():
    print("\nTesting effect of bad date format\n")
    x = "nada"
    try:
        x = todo_model.TodoItem("stuffy","123-32-12","123-321-23")
    except:
        print("Bad dates broke as expected")
        assert(True)
    print(x)

    try:
        x = todo_model.TodoItem("stuffy","20180705","101010")
    except:
        print("Good dates should not have broken")
        assert(False)
    assert(True)

    print("\nPASSED - Test of bad date format\n")


def test_model_null_todo():
    print("\nTesting effect of null todo\n")
    try:
       x = todo_model.TodoItem()
    except:
       print("\nNull Todo broke as expected\n")
       assert(True)
       print("\nPASSED - Testing effect of null todo")
       return
    print("\nNull entry for todo did not break as it should\n")
    assert(False)
    
    
def run():
    x = "--------------------------------"
    print("\nRUNNING TODO MODEL TESTS")
    test_model_non_text()
    print(x)
    test_model_bad_dates()
    print(x)
    test_model_null_todo()
    print(x)


if __name__ == "__main__":
    run()
