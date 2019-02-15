




# Decorator
# def plus_if(f):
#     def inner(n):
#         if n > 10:
#             return n+10
#
#         else:
#             return n
#     return inner
#
#
# @plus_if
# def plus(num):
#     return num
#
#
# print(plus(8))




























# import math
#
# # 3-D and n-Dim vector
#
#
# class Vector:
#     def __init__(self, *args):
#         self.dims = args
#
#     def length(self):
#         return sum(map(lambda x: x**2, self.dims))**0.5
#
#     def __add__(self, other):
#         dims = map(lambda a: sum(a), zip(self.dims, other.dims))
#         return Vector(*dims)
#
#     def __repr__(self):
#         return f"n-dim Vec :::: {self.dims}"
#
#
# v1 = Vector(1, 2, 3)
# v2 = Vector(1, 2, 3)
#
# v3 = v1 + v2
# print(v1, v2, v3)
# print(v3.length())
#
#



















# from flask import Flask
# app = Flask(__name__)
#
#
# @app.route("/")
# def hello():
#     return "Hello world :)))!"
#
#
# @app.route("/greeting/<string:name>")
# def greeting(name):
#     return f"Hello {name}!"
#
#
# app.run()




























# def new_sal(f):
#     def inner(salary):
#         if salary > 1000:
#             return f(salary)
#         else:
#             return salary
#
#     return inner
#
#
# @new_sal
# def salary_tex(salary):
#     salary = salary - (salary * 0.05)
#     return salary
#
#
# print(salary_tex(1500))























# try:
#     num = int(input("Enter number:"))
#     num += 1
#     print(num)
# except TypeError:
#     num = int(num) + 1
# except ValueError:
#     num = input("enter name:")
#     num = str(num)
#     print(num)
#
# else:
#     num = num - 10
# finally:
#     print("done")
#     print(num)











# name = "ali"
# print("%10s is me" % name)
#



# scores = [["ali", 20, 19, 17.5], ["mohammad", 20, 19, 18]]
# for score in scores:
#     for person in score:
#         print(f"{person:10} |", end=" ")
#     print()
#

# x = 1
# print(globals())
# print(locals())
#
#

# class Computer:
#
#     count = 0
#
#     def __init__(self, ram, hard, cpu):
#         self.ram = ram
#         self.hard = hard
#         self.cpu = cpu
#
#     def value(self):
#         return self.ram + self.hard + self.cpu
#     # def __del__(self):


# Computer.size = 32

# pc_1 = Computer(24, 2, 8)
# pc_2 = Computer(8, 1, 4)
# print(pc_1.value())
# print(pc_2.value())
#












# class Person:
#     count = 0
#
#     def __init__(self, name, age):
#         self.age = age
#         self.name = name
#         Person.count += 1
#
#     def get_name(self):
#         print("The name is %s" % self.name)
#
#     def get_age(self):
#         print("The age is %s" % self.age)
#
#     def get_info(self):
#         print(f"The name is {self.name} and the age is  {self.age}")
#
#     def birthday(self):
#         self.age += 1
#         print(f"Happy birthday {self.name} ")
#
#     def number(self):
#         return Person.count
#
#
# ali = Person("ali", 20)
#
# ali.birthday()
# print(ali.number())
#

