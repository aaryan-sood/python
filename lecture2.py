str = 'This is a string.\nThis string was created in python.'   #\n new line escape sequence character
print(str)

new = 'aaryan sood'
print(new)
print(new[2])
new_str = 'u' + new[1 : ]   # slicing str[1 : ] means 1 to last(len(str))
#slicing str[startingIndex : endingIndex]
print(new_str)              #str[ : 3] means from 0  to 2
#characters can be accessed but not manipulated in the form of the indexes
print(new[1:4])
print(new[1:5])
print(new[ : 6])    #aaryan
print(new[7 : ])    #sood

arr = 'apple'
print(arr[-3 : -1])

inp = 'i am a coder.'
print(inp.endswith('er.'))
print(inp.endswith('sood'))
print(inp.capitalize())     #just capitalises the first character of the string passed does not changes the old string creates a new string 
print(inp)

newInp = 'i am studying python basics'
print(newInp.replace('python','c++'))
print(newInp)
print(newInp.find('python'))     #returns the first index of the word present
print(newInp.find('z'))          #returns -1 of it does not exists
print(newInp.count('a'))         #returns the count of a substr in a string

#Ques 
name = input('enter the first name of the user : ')
print(len(name))
str = 'Hi $I am the $ symbol $99.99'
print(f'the number of times $ appear is : {str.count('$')}')

# if-elif-else
age = int(input('enter your age : '))

if(age >= 18) : 
    print('can vote and apply for license')

color = input('enter the color of the light : ')
if(color == 'red') : 
    print('stop')
elif(color == 'yellow') : 
    print('get ready')
elif(color  == 'green') : 
    print('Go')
else : 
    print('enter a correct color')

#marks
marks = int(input('enter your marks : '))
grade = None
if(marks >= 90) : 
    grade = 'A'
elif(marks >=80 and marks < 90) : 
    grade = 'B'
elif(marks < 80  and marks >= 70) : 
    grade = 'C'
else : 
    grade = 'D'
print(grade)

#even or odd
num = int(input('enter a number : '))
if num %2 == 0 : 
    print('even')
else : 
    print('odd')

#greatest of three numbers
a = int(input('enter the first number : '))
b = int(input('enter the second number : '))
c = int(input('enter the third number : '))
if a >= b and a >= c : 
    print(f'{a} is greatest')
elif b >= c : 
    print(f'{b} is greatest')
else : 
    print(f'{c} is greatest')