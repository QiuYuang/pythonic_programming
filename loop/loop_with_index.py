"""
打印序号和数据
"""

print("***************序号打印一般写法*****************")
result_list = [1,2,3,4,5,6,7]
i = 0
for result in result_list:
    print(i, result)
    i += 1


##Pythonic
print("***************pythonic*****************")
for i, result in enumerate(result_list):
    print(i, result)