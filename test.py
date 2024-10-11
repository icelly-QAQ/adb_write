import str_xy_lib  # 把这个库文件放在和main.py同一个目录下

# 单个数获取
print(str_xy_lib.get_str_xy("1"))

i_number = str_xy_lib.get_str_xy("2")
print(i_number)

# 多个数获取
print(str_xy_lib.get_str_xy(["1", "2", "3"], True))

# 将要获取的数以列表方式传入，在第二个参数位置传入一个bool值
# true为启用多个数获取，false或留空为关闭多个数获取
