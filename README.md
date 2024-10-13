# ADB_Write
**该项目是基于pyhton制作的adb模拟手写输入的程序**

****

### 食用方法：

**get_str_xy(input_str, shift_x, shift_y, more) # 函数将会直接运行ipnut swipe *** *** *** *** 0**

+ ***在调用该函数前请提前连接您要输出的设备，并在该函数运行期间保持连接***

+ input_str：需要处理的字符（str类型）

+ shift_x：X偏移量（int类型，默认值为 0）

+ shift_y：Y偏移量（int类型，默认值为 0）

+ ~~more：是否启用多字符处理（bool类型，默认值为 False）~~

**Tips：偏移量从屏幕左上角开始计算（左上角为（0, 0）向右为+X， 向下为+Y）**

后续更新可能会加入处理分数的功能，敬请期待吧 awa