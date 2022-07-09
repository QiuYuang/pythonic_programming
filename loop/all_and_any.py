"""
判断数据中存在success或者判断全部是success时
"""
def is_success(msg):
    print(msg)
    return msg=="success"


result_list = ["success","success","fail","success"]
def is_all_success(results):
    for result in results:
        if not is_success(result):
            return False
    return True

def is_all_success_all(results):
    return all(is_success(result) for result in results)

print("***************判断是否全部success*****************")
print(is_all_success(result_list))
print("***************pythonic*****************")
print(is_all_success_all(result_list))




result_list = ["success","success","fail","success"]
def exist_success(results):
    for result in results:
        if is_success(result):
            return True
    return False

def exist_success_any(results):
    return any(is_success(result) for result in results)

print("***************判断是否存在success*****************")
print(exist_success(result_list))
print("***************pythonic*****************")
print(exist_success_any(result_list))