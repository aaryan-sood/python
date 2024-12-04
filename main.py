# input = [1,2,3,4]

# for i in range(len(input)):
#     print(input[i])

# Basic Data Structures in Python

print('===List===')
fruits = ['apples','oranges','papaya','watermelon']
print('before appending')
for i in range(len(fruits)):
    print(fruits[i])
fruits.append('kiwi')
print('after appending')
for i in range(len(fruits)):
    print(fruits[i])
print(fruits[1])

print('===tuples===')
numbers = (4,5)
for i in range(len(numbers)) : 
    print(numbers[i])

print(numbers[1])

# 3. Dictionary: Unordered, mutable, key-value pairs
# print("\n=== Dictionary ===")
# student = {
#     "name": "John",
#     "age": 21,
#     "subjects": ["Math", "Science"]
# }
# print("Student details:", student)
# print("Student's name:", student["name"])  # Access value by key

# # Add a new key-value pair
# student["grade"] = "A"
# print("After adding grade:", student)

print('===Dictionary===')
student = {
    "name" : "aaryan",
    "age" : "21",
    "subjects" : ['Maths','Science']
}
print('Student detail : ',student)
print(student["name"])
print('Student details through a loop : ')
for key,value in student.items() : 
    print(f"{key} : {value}")


# 4. Set: Unordered, mutable, no duplicate elements
print("\n=== Set ===")
numbers = {1, 2, 3, 3, 4}
print("Set of numbers (duplicates removed):", numbers)
numbers.add(5)  # Add an element
print("After adding 5:", numbers)

# 5. Loops and Control Statements
print("\n=== Loops and Control Statements ===")
print("Using a for loop to print numbers from 1 to 5:")
for i in range(1, 6):
    print(i)

print("\nUsing a while loop to print numbers from 5 to 1:")
count = 5
while count > 0:
    print(count)
    count -= 1

print("\nUsing if-else to check even or odd:")
for num in range(1, 6):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

# 6. Functions: Reusable blocks of code
print("\n=== Functions ===")


def greet(name):
    return f"Hello, {name}!"


print(greet("Alice"))

# 7. List comprehension: A concise way to create lists
print("\n=== List Comprehension ===")
squared_numbers = [x ** 2 for x in range(1, 6)]
print("Squares of numbers 1 to 5:", squared_numbers)
