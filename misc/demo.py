import math
#print('Test, test, test!')

# single-line comment

'''
    multi-line
    comment
'''

def demo_print_greeting():
    print("Hello, boss!")

def demo_local_variable():
    var = 7
    var = 'The name is 007'
    print(var)

def demo_global_variable():
    global name
    name = "Paul"
    print(name + "y")

def demo_arithmetic():
    print("Demo Arithmetic")
    print("7 + 2 = ", 7+2)
    print("7 - 2 = ", 7-2)
    print("7 * 2 = ", 7*2)
    print("7 / 2 = ", 7/2)
    print("7 % 2 = ", 7%2)
    print("7 ** 2 = ", 7**2)
    print("7 // 2 = ", 7//2)
    print("math.floor(7/2) = ", math.floor(7/2))
    print("math.ceil(7/2) = ", math.ceil(7/2))

def demo_function_params(first:str, last:str):
    print("The name is " + first + " " + last)

def demo_function_calls():
    demo_function_params("James","Bond")

name = "unknown"
def main():
    #demo_print_greeting()
    #demo_local_variable()
    #demo_global_variable()
    #print(name)
    demo_arithmetic()
    #demo_function_calls()

if __name__ == "__main__":
    main()

