# print('my name is aaryan.','my age is 22')
# print(23)
# print(23+32)

name = "aaryan"
age = 22
number = 25.99
isOld = False
a = None
print('my name is : ',name)
print('my age is : ',age)
print('the price of oranges',number)

#data type
# print('data type')
# print(type(name))
# print(type(age))
# print(type(number))
# print(isOld)
# print(a)

#sum of two numbers
a = 3
b = 2
sum = a+b
print(sum)
print(a/b) # / always return a float even if the answer is an integer
print(a ** b) # ** is the power operator(a ^ b)

# type conversion
a = 2
b = 4.25
print(a + b) # 2.0 + 4.25 = 6.25

#type casting
a = float("2")
b = 3.25
print(a + b)

#input in python
name = input('enter the name : ')      #input from the input statement is always a string so need to convert it to a integer or float by int() or float()
age  = int(input('enter your age : '))
print(f'Hi {name}')
print(f'{type(name)} {name}')
print(f'you entered your age as : {age}')

#average
num1 = float(input('enter the first number : '))
num2 = float(input('enter the second number : '))
avg = (num1 + num2)/2.0
print(f'the average is : {avg}')