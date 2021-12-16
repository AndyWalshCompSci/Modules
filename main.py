import Not_main

Not_main.hello()

def random_name(var1, var2, var3):
    number1 = var1 + 2
    print(number1)
    string1 = var2 * var1
    print(string1)
    if var3 == True:
        print("hello")
    else:
        print("world")
    return number1 , string1
    print("this is dead code")

random_name(80, "hello world", True)
