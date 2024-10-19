import str_xy_lib  # 把这个库文件放在和main.py同一个目录下

str_to_get = ["1", "1", "4", "5", "1", "4"] # 需要处理的数
shift_x = 100 # x偏移量
shift_y = 800 # y偏移量
interval = 200 # 两个数之间的间隔

str_xy_lib.get_str_xy(str_to_get, shift_x, shift_y, interval)
# str_xy_lib.get_str_xy(str_to_get, shift_x, shift_y)
