# import math

# print(math.sqrt(1234))


"""
number = 0

message = "positive." if number > 0 else "Zero or negative."
print(message)

if number > 0:
     print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
"""

# --------------------------------------------------------

"""
numbers = [1,2,3,4,5,-1,-23]

numbers.sort()
numbers.pop()
numbers.reverse()
numbers.append(54)

del numbers[0:3]

# list = [1,1,1] = [1,1,1]
# set = {1,1,1} = {1} and the order is not guaranteed

print(numbers)
"""

# --------------------------------

"""
letterA = {"A", "B", "C"}
letterB = {"C", "D"}

print(f"letterA{letterA}")
print(f"letterB{letterB}")


union = letterA | letterB
print(f"Union{union}")

intersection = letterA & letterB
print(f"Intersection{intersection}")

difference = letterA - letterB
print(f"Difference{difference}")
"""

# --------------------------------

"""
person = {
    "name": "Jamal",
    "age": 20,
    "address": "USA"
}

print(person["age"])
print(person.keys())
print(person.values())
person["age"]=100
print(person)


letterA = {"A", "B", "C"}

for letter in letterA:
    print(letter)

"""


person = {
    "name": "Jamal",
    "age": 20,
    "address": "USA"
}

# for key in person:
#     print(f"Key:{key} value:{person[key]}")

# for key,value in person.items():
#     print(f"Key:{key} value:{value}")

"""
all_numbers = [1, 3, 5, 6, 7, 9]
my_sum = 0

for item in all_numbers:
    my_sum += item

print(f"Sum is {my_sum}")

while len(all_numbers) < 100:
    all_numbers.append(5)
    if len(all_numbers) > 15:
        print("Reached 15 length")
        continue
    print(len(all_numbers))
else:
    print("while loop ended")

print(len(all_numbers))
"""
"""
def greet(name, age = -1):
    print(f"Hello {name}, your age is {age}!")

greet("Yehia", 14)
greet("Ahmed")
greet("Omar", 1)


def is_adult(name, age = -1):
    print(f"Hello {name}, your age is {age}!")
    return age >= 45

result = is_adult("Yehia", 44)
print(result)
"""

def greet(name, age = -1):
    print(f"Hello {name} my age is {age}")
    print("I need to sleep")


from calculator import div
print(div(4,6))


import calculator

print(calculator.add(4,6))
print(calculator.sub(4,6))
print(calculator.mul(4,6))
print(calculator.div(4,6))

# greet("Ahmed", 50)
