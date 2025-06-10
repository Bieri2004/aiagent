from functions.get_files_info import get_files_info

if __name__ == "__main__":
    print("Test 1: Aktuelles Verzeichnis")
    print(get_files_info("calculator", "."))
    print("\nTest 2: pkg")
    print(get_files_info("calculator", "pkg"))
    print("\nTest 3: /bin (außerhalb)")
    print(get_files_info("calculator", "/bin"))
    print("\nTest 4: ../ (außerhalb)")
    print(get_files_info("calculator", "../"))
