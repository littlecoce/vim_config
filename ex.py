def def_test():
    print("This is just a def function")
    return True

def return_test():
    print("Does it autointend after a return statement?")
    print("This was indented automaticly")
    return False

test = "test"
test2 = 'test';

dictionary = {'param1': 1, 'param2': '2'}
addString = "";

for p in dictionary:
    print(str(p))
    addString = addString + p

print(test + " " + addString)

age = input("How old are you? ")
print(age)
