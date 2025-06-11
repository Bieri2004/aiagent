from functions.run_python import run_python_file

if __name__ == "__main__":
    print("Test 1: main.py")
    print(run_python_file("calculator", "main.py"))
    
    print("\nTest 2: tests.py")
    print(run_python_file("calculator", "tests.py"))
    
    print("\nTest 3: ../main.py (außerhalb)")
    print(run_python_file("calculator", "../main.py"))
    
    print("\nTest 4: nonexistent.py")
    print(run_python_file("calculator", "nonexistent.py"))
