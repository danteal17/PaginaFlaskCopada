file_path = "notas.txt"
try:
    file = open(file_path, "r")
    if not file.closed:
        print(f"File '{file_path}' is open in the current process.")
    else:
        print(f"File '{file_path}' is closed in the current process.")
    
except FileNotFoundError:
    print(f"File '{file_path}' not found.")



