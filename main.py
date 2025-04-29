import sys
import os

def list_contents(parent_directory, indentation=""):
    try:
        for entry in os.listdir(parent_directory):
            full_path = os.path.join(parent_directory, entry)
            if os.path.isfile(full_path):
                print(f"{indentation}📄 File: {entry}")
            elif os.path.isdir(full_path):
                print(f"{indentation}📁 Directory: {entry}")
                list_contents(full_path, indentation + "    ")
            else:
                print(f"{indentation}❓ Other: {entry}")
    except PermissionError:
        print(f"{indentation}⛔ Permission denied: {parent_directory}")


def main():
    if len(sys.argv) != 2:
        print(f"Usage: test.py [Full directory path]")
    else:
        list_contents(sys.argv[1])

if __name__ == "__main__":
    main()
