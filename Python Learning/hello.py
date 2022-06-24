from ast import Str


def hello(name: Str):
    print("Hello, %s!" % name)

hello(input("What is your name? "))

