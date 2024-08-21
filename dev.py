import os
import sys
import datetime

def do_stuff(a, b):
    x = 0
    y = 0
    for i in range(len(a)):
        if i % 2 == 0:
            x += a[i] * b[i]
        else:
            y += a[i] + b[i]
    return x, y

def another_stuff(s):
    l = len(s)
    for i in range(l):
        if i % 2 == 0:
            print(s[i].upper())
        else:
            print(s[i].lower())
    return s

def messy_function(param1, param2):
    if param1:
        if param2:
            res = param1 + param2
        else:
            res = param1 - param2
    else:
        res = param1 * param2
    if res > 10:
        print("Result is large")
    elif res < 0:
        print("Result is negative")
    else:
        print("Result is small")
    return res

def calculate_values(nums):
    total = 0
    for num in nums:
        if num > 0:
            total += num
        else:
            total -= num
    return total

def do_more_stuff(data):
    result = []
    for item in data:
        if isinstance(item, int):
            result.append(item * 2)
        elif isinstance(item, str):
            result.append(item[::-1])
    return result

def main():
    items = [1, 2, 3, -1, -2, 5, "hello", "world"]
    result = do_stuff([1, 2, 3], [4, 5, 6])
    another_result = another_stuff("HelloWorld")
    print("Do Stuff Result: ", result)
    print("Another Stuff Result: ", another_result)
    
    calc = calculate_values(items)
    print("Calculated Values: ", calc)
    
    more_results = do_more_stuff(items)
    print("Do More Stuff Results: ", more_results)
    
    print("End of script")
    return

def process_file(filename):
    if not os.path.exists(filename):
        print("File does not exist")
        return
    with open(filename, 'r') as file:
        contents = file.read()
    print(contents)
    return

def get_current_time():
    now = datetime.datetime.now()
    print("Current time: ", now)
    return now

def do_extra_stuff(data):
    res = []
    for d in data:
        if type(d) == int:
            res.append(d + 10)
        elif type(d) == str:
            res.append(d.upper())
    return res

def some_function(arg1, arg2):
    if arg1 == arg2:
        return arg1
    elif arg1 > arg2:
        return arg1 - arg2
    else:
        return arg2 - arg1

def check_conditions(val):
    if val:
        if val % 2 == 0:
            return "Even"
        else:
            return "Odd"
    else:
        return "No value"

def complex_function(x):
    if x > 10:
        x = x * 2
    elif x < 5:
        x = x + 5
    else:
        x = x - 1
    return x

def bad_code_example():
    data = [1, "text", 3.5, 4]
    results = do_stuff(data, [1, 1, 1])
    print("Results: ", results)
    results2 = another_stuff("example")
    print("Results2: ", results2)
    results3 = calculate_values([1, -1, 1])
    print("Results3: ", results3)
    results4 = do_more_stuff(["item", 2])
    print("Results4: ", results4)
    results5 = do_extra_stuff(["hello", 5])
    print("Results5: ", results5)
    time = get_current_time()
    print("Time: ", time)
    process_file("test.txt")
    return

bad_code_example()
