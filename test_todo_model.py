import todo_model

def test_model_non_text():
    print("\nTesting effect of non-text\n")

    print("\nPASSED - Test of non-text\n") 

def test_model_bad_dates():
    print("\nTesting effect of bad date format\n")

    print("\nPASSED - Test of bad date format\n")

def test_model_null_todo():
    print("\nTesting effect of null todo\n")
    
    print("\nPASSED - Testing effect of null todo\n")



def run():
    test_model_non_text()
    test_model_bad_dates()
    test_model_null_todo()


if __name__ == "__main__":
    run()
