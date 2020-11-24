#!/usr/bin/python3
#迭代器
import sys  # 引入 sys 模块
List = [1, 2, 3, 4]
it = iter(List)    # 创建迭代器对象
for x in it:
    print(x, end=" ")

print('')
print('----------')
List = [1, 2, 3, 4]
it = iter(List)  # 创建迭代器对象

while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()

sys.path
