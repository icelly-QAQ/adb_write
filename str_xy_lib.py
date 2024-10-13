from functools import lru_cache
import subprocess

commands = []
base_coordinates = {
    "1": [[10, 10], [7, 100]],
    "2": [[10, 50], [50, 10], [100, 50], [10, 90], [100, 90]],
    "3": [[10, 50], [50, 10], [100, 50], [50, 80], [100, 110], [50, 160], [10, 110]],
    "4": [[50, 10], [10, 50], [110, 50], [90, 50], [90, 20], [90, 110]],
    "5": [[10, 10], [10, 60], [60, 80], [10, 110], [60, 80], [10, 60], [10, 25], [80, 25]],
    "6": [[80, 10], [10, 90], [50, 130], [100, 90], [50, 70]],
    "7": [[10, 10], [60, 10], [30, 90]],
    "8": [[10, 40], [50, 80], [25, 110], [10, 80], [50, 40], [25, 15], [10, 40]],
    "9": [[50, 10], [10, 10], [10, 50], [50, 50], [50, 10], [50, 110]],
    "0": [[25, 10], [10, 25], [10, 75], [25, 100], [50, 75], [50, 25], [25, 10]],
    ">": [[10, 10], [50, 50], [10, 100]],
    "<": [[50, 10], [10, 50], [50, 100]],
    "=": [[1284, 1122], [1700, 1122], [1280, 1300], [1700, 1300]]
}


def get_str_xy(input_str, shift_x: int = 0, shift_y: int = 0):
    for i in range(len(base_coordinates[input_str]) - 1):
        commands.append(f"input swipe {(base_coordinates[input_str][i][0]) + shift_x} {(base_coordinates[input_str][i][1]) + shift_y} {(base_coordinates[input_str][i + 1][0]) + shift_x} {(base_coordinates[input_str][i + 1][1]) + shift_y} 0")
    for i in range(len(commands)):
        print(commands[i])
        awa = subprocess.run(["adb", "shell", commands[i]])
    return awa

'''
基准分辨率（1080 x 2880）

使用方法在test.py
分辨率浮动在 +-20px 以内
'''

if __name__ == "__main__":
    str_to_get = ">"
    shift_x = 100
    shift_y = 500
    get_str_xy(str_to_get, shift_x, shift_y)