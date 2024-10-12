# ADB_Write
**该项目是基于pyhton制作的adb模拟手写输入的程序**

****

### 食用方法：

**get_str_xy(input_str, shift_x, shift_y, more) # 函数将会返回可以直接在adb shell中运行的命令**

+ input_str：需要处理的字符（str类型，当 more 传入 True 时，需要传入列表）

+ shift_x：X偏移量（int类型，默认值为 0）

+ shift_y：Y偏移量（int类型，默认值为 0）

+ more：是否启用多字符处理（bool类型，默认值为 False）

**Tips：偏移量从屏幕左上角开始计算（左上角为（0, 0）向右为+X， 向下为+Y）**