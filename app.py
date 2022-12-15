from os import path
from request import get_playlist_time
from functions import get_input, get_mode
from functions import increments, extract, calculate, convert

new_playlist = input("Enter playlist ID: ")

mode = get_mode()

dirname = path.split(__file__)[0]
save_file = path.join(dirname, "save_info.txt")

if not path.isfile(save_file):
    file = open(save_file, "w")
    get_playlist_time(file, new_playlist)
    file.close()
else:
    file = open(save_file, "r")
    old_playlist = file.readline().split(": ")[1].strip()
    file.close()
    if old_playlist != new_playlist:
        file = open(save_file, "w")
        get_playlist_time(file, new_playlist)
        file.close()

with open(save_file, "r") as file:
    file.readline()
    time_table = extract(file)
    if mode == 1:
        time = calculate(time_table, 0, len(time_table), 1)
        time = convert(time)
        print(time)
    if mode == 2:
        start, end, step = get_input()
        time = calculate(time_table, start, end, step)
        time = convert(time)
        print(time)
    if mode == 3:
        increment = int(input("Enter an increment number: "))
        if increment <= 0:
            increment = len(time_table)
        times = increments(time_table, increment)
        for value in times:
            print(convert(value))
