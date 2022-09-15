def say_hello():
    print("hello")

def say_bye():
    print("bye")

say_hello()

def say_hello(name):
    print(name, " hello")

say_hello("Noah")

def say_hello(index, name):
    print("[", index, "]", name, "hello")

say_hello( 1, "Noah")