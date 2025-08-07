print("tuples")
t1 = (1, 2, 3,3,4,6,4,6,1,2,3) 
print (t1) 
t2 = 4,5,6
print(t2) 
t3=(7,)
print(t3)
t4=()   
print(t4) 

print(t1.count(1)) # counts the number of occurrences 
print(t1.index(4))   # index()  returns the first index of occurance of the value
print(t1.__len__())  # returns the length of the tuple
print(t1[0])  # accessing the first element 

a,b= 10,20
b,a = a,b  # swapping values using tuple unpacking
print(a, b)  # prints the unpacked values 


#tuple packing and unpacking 

person =  ("Ahtisham" , 21 , "Pakistan") 
name , age , country =  person # unpacking the tuple
print(name)  # prints "Ahtisham"
print(age)   # prints 21    
print(country)  # prints "Pakistan" 


#named tuples 
from collections import namedtuple 
person = namedtuple("user", ["name" , "status" , "country"])
user1 = person("Ahtisham" , "active" , "pakistan")
print(user1.name)
print(user1.status)
print(user1.country) 

user2 =  person("Ali" , "inactive" , "Pakistan") 
print(user2.name)
print(user2.status)
print(user2.country) 


list1 = ["ahtisham", "ali", "usman", "ahmed", "sara", "sana", "sami", "sara", "sana", "sami"]
print(list1.__len__())
print(list1[3:list1.__len__()])
