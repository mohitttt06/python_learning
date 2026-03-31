#functions -> are the block of reusable code. we can use the functions where we often need to reuse a piece of code. they make the code look more resuable,,flexible ,modular and understandable.


def darling():
    print("darling is on of the best telugu romcom")

darling()
darling()
darling()



#passing arguments into the function during function call. 


def driving(name,age):
    if(age>=18):
      print(f"Hello Mr {name} you are eligible because ur {age} yrs old")

    else:
      print(f"Hello Mr {name} you are noy eligible because ur {age} yrs old")
      

driving("jhon",19)
driving("ram",17)
driving("carl",10)



#Using return statement , return statement is a statement used to return some value to the caller of the function.


def add(a,b):
    c=a+b
    return c

print(add(1,3))
print(add(55,45))
print(add(1000,1567))