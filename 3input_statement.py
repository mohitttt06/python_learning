input("Enter ur name: ") #input function by default takes any value as only class<str> , so here the output is nothing 

name = input("Enter ur name: ") #here we are storing the input value in a variable caleld name

# print("Your name is: ",name) #the ouput is mohit,it is ok because names are always string so it is ok to use input function directly. but for taking other data type inputs the following is the correct way.

age = int(input("Enter ur age: ")) #the entered value is typecasted to <class 'int'>
print("the type is casted to: ",type(age)) #the type is casted to:  <class 'int'>
print("the age is: ",age) #the age is:  12
