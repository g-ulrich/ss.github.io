
from datetime import datetime
import time

DN = datetime.now()
TIME = DN.strftime("%H.%M")
DAY = DN.strftime("%d")

TEMP_FILE = 'tmp_files/temp.txt'
TEMP_FILE_OUTPUT = "tmp_files/output.txt"
TRANSACTION_HISTORY = "transactions/history.txt"



def clear_record(file_path_and_name):
    time_now = datetime.now().strftime("%H.%M")
    if time_now >= "16.00":
        print("!CLEARED! " + file_path_and_name)
        open(file_path_and_name, 'w').close()
        file, txt = open(file_path_and_name, "r"), ("DontDelete" + "\n")
        readFile = file.readlines()
        readFile.insert(1, txt)
        file.close()
        file = open(file_path_and_name, "w")
        file.writelines(readFile)
        file.close()


def clear_records():
    clear_record(TEMP_FILE)
    time.sleep(1)
    print_to_temp("---")
    print_to_temp("---")
    print_to_temp("---")
    print_to_temp("---")
    clear_record(TEMP_FILE_OUTPUT)
    time.sleep(1)
    print_to_output("[data cleared]")

def read_temp_str():
    data = [line.rstrip('\n') for line in open(TEMP_FILE)]
    data.remove(data[0])
    return [str(i) for i in data]


def print_to_temp(input_string):
    file, txt = open(TEMP_FILE, "r"), (str(input_string) + '\n')
    readFile = file.readlines()
    readFile.insert(1, txt)
    file.close()
    file = open(TEMP_FILE, "w")
    file.writelines(readFile)
    file.close()


def print_to_output(input_string):
    TIME = datetime.now().strftime("%H.%M")
    file, txt = open(TEMP_FILE_OUTPUT, "r"), (TIME + ": " + str(input_string) + '\n')
    readFile = file.readlines()
    readFile.insert(1, txt)
    file.close()
    file = open(TEMP_FILE_OUTPUT, "w")
    file.writelines(readFile)
    file.close()


def read_output_str():
    data = [line.rstrip('\n') for line in open(TEMP_FILE_OUTPUT)]
    data.remove(data[0])
    return [str(i) for i in data]


def count_lines_in_temp():
    count = 0
    with open(TEMP_FILE, 'r') as f:
        for line in f:
            count += 1
    return count

print(TIME)