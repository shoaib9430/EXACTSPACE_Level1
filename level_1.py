import os

def truncate_file(file_path, lines_to_keep=100):
    with open(file_path, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        file.truncate()
        file.writelines(lines[-lines_to_keep:])

def find_largest_log_file(directory):
    log_files = [f for f in os.listdir(directory) if f.endswith('.log')]
    if not log_files:
        print("No log files found in the directory.")
        return

    largest_size = 0
    largest_file = None

    for file in log_files:
        file_path = os.path.join(directory, file)
        file_size = os.path.getsize(file_path)
        if file_size > largest_size:
            largest_size = file_size
            largest_file = file_path

    return largest_file

directory = r"C:\Users\Shoaib\Desktop\sahinotes_complete\server\logs"
largest_log_file = find_largest_log_file(directory)

if largest_log_file:
    print(f"Largest log file: {largest_log_file}")
    truncate_file(largest_log_file, lines_to_keep=100)
    print("File truncated to 100 lines.")
