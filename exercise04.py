"""
2222222222222222222222
为sum_data,增加打印函数执行时间的功能.
        函数执行时间公式： 执行后时间 - 执行前时间
def sum_data(n):
    sum_value = 0
    form number in range(n):
        sum_value += number
    return su_value

print(sum_data(10))
print(sum_data(1000000))
"""
import time


def caculate_time():
    def wrapper(*args, **kwargs):


@caculate_time
def sum_data(n):
    sum_value = 0
    for number in range(n):
        sum_value += number
    return sum_value

print(sum_data(10))
print(sum_data(1000000))