def extract(fv):
    """Extracts the information from fv and puts it into time_list"""
    time_list = []
    for value in fv:
        new_value = value.split(", ")
        new_value[1] = float(new_value[1].strip())
        time_list.append(new_value)
    return time_list

def calculate(input_list, start, end, step=1):
    """Calculates the total seconds"""
    step = 1 if step == 0 else step
    new_time_list = input_list[start:end:step]

    total_seconds = 0
    for value in new_time_list:
        total_seconds += value[1]
    return total_seconds

def convert(total_seconds):
    """Converts total seconds to hours, minutes, seconds and a string rep"""
    total_seconds = int(total_seconds)
    minutes, seconds = divmod(total_seconds, 60)
    hours, minutes = divmod(minutes, 60)
    time_string = f'{hours}:{minutes}:{seconds}'
    return time_string

def get_mode():
    """Gets input and returns mode"""
    print("Select a Mode: ")
    print("----------------------------------")
    print("1: Print total time")
    print("2: Print one increment")
    print("3: Print all increments")
    mode = int(input("Enter a number from above: "))
    return mode

def get_input():
    """Gets input for start end and stop"""
    start = int(input("Enter start number: "))
    end = int(input("Enter end number: "))
    step = int(input("Enter step number: "))
    return start, end, step

def increments(time_list, increment):
    """
    Returns time for a given increment
    for ex. given an increment of 10
    it'll produce times for 10 videos at a time 
    until completely through the list
    """
    page = 0
    times = []
    while (page * increment) < len(time_list):
        start = (page * increment)
        end = ((page + 1) * increment)
        if ((page + 1) * increment) > len(time_list):
            end = len(time_list)
        seconds = calculate(time_list, start, end)
        times.append(seconds)
        page += 1
    return times