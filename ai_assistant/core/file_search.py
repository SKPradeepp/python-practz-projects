import os

def find_file(filename, search_path="C:\\Users\\Pradeepp"):

    filename = filename.lower()

    print("Searching in:", search_path)

    for root, dirs, files in os.walk(search_path):

        for file in files:

            if "notes" in file.lower():
                print("Found notes file during scan:", os.path.join(root, file))

            if filename in file.lower():
                print("Matched:", os.path.join(root, file))
                return os.path.join(root, file)

    return None