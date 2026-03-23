a=10
b=a
print(id(a)) #140728054392008
print(id(b)) #140728054392008

#id() ,is used to get memory address
# both share the same memory cause basically b is pointing to some thing which a is pointing already.
# in python the values are stored like objects in the memory.
# where the variable name like x is just a thing pointing to our object in the memory

a = 10 
b = a 
a = 20
print(id(a)) #old address-> 140727837533384
#new address-> 140727837533704.
print(id(b)) #140727837533384

#the address of b was the initial address of a , means b still points to 10
#but after we assigned a=20 , then the address of a was changed
#and it now points to 20 now.