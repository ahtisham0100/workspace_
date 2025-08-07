print("getting started with python !")
#this is a single line comment 

""" 
this is a multiple
line comment
"""
print("Hello World after multiple line comment") 


# Variables and Data Types
x= 5; 
name = "AHTISHAM" 
ISOPEN = False
pi =  30.15
isture =  True
print(x, isture , name , ISOPEN , pi)

print(f"NAME IS  :  {name} and x is : {x}")

#data types  

complexnum =  3 + 4j

print(type(complexnum) , complexnum)  # <class 'complex'>


msg =  "this is the first message" 

msg2 = msg.capitalize()
print(msg2)  # This is the first message 
msg3 = msg.upper()
print(msg3)  # THIS IS THE FIRST MESSAGE
msg4= msg.partition("the") # partition splits the string into three parts based on the first occurrence of the separator which is "the" in this case and returns a tuple where separator is at the middle
print(msg4) 
msg5 =  msg.split(" ")  # splits the string into a list of words based on the space separator
# print(msg5)  # ['this', 'is', 'the', 'first', 'message']
# msg6 = msg.replace("first", "second")  # replaces the first occurrence of "first" with "second"
# print(msg6)  # this is the second message
# msg7 = msg.find("first")  # finds the index of the first occurrence of "first"
# print(msg7)  # 10
# msg8 = msg.index("first")  # finds the index of the first occurrence of "first", raises an error if not found

# print(msg10)  # this is the first message
print(msg2.count("is"))  # counts the number of occurrences of "is" in the string
print(msg2.startswith("this"))      # checks if the string starts with "this"