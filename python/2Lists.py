# list = ["item" , "item2", "item3", "item4", "item5"] 

# print(list)  # ['item', 'item2', 'item3', 'item4', 'item5'] 

# for item in list:
#     print(item)

# print(len(list))
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)  # ['apple', 'banana', 'cherry']
print(list2)  # [1, 5, 7, 9,    3]
print(list3)  # [True, False, False]

mixed_list = ["apple", 1, True, 3.14]
print(mixed_list)  # ['apple', 1, True, 3.14

print(type(mixed_list)) 

## list contructor : 



print(list1[1:3])  # apple

numbers= []
for i in range (0,10):
        numbers.append(i)
print(numbers)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[5:len(numbers)])  # [0, 1, 2, 3, 4] 
print(numbers[5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(thislist[4:])

if "banana" in thislist:
        print("Yes, 'banana' is in the fruits list")  # Yes, 'banana' is in the fruits list
else:
        print("No, 'banana' is not in the fruits list")

thislist[1:3]=["value 1" , "value 2"]
print(thislist) 

thislist[1:]= ["updated values"]
print(thislist)
tropical = ["mango", "pineapple", "papaya"]

list1.extend(tropical)
print(list1)  # ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']
list1.append("bananana")
print(list1)  # ['apple', 'banana', 'cherry', 'mango 


list1.pop(5) 
list1.remove("banana")
print(list1)

del list1[0]  # delete first item
del list1[2]
print(list1)  # ['cherry', 'mango', 'papaya', 'bananana']
print(list1)  # NameError: name 'list1' is not defined 


newList = ["apple", "banana", "cherry"]
newList.extend(["orange", "kiwi", "melon"])
newList.extend(["grape", "pear"])
newList.extend(["peach", "plum"])

print(newList)  # ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'grape', 'pear', 'peach', 'plum']


# for i in range(15):
#         print(newList[i]) 

for item in newList:
        print(item)  # apple, banana, cherry, orange, kiwi, melon, grape, pear, peach, plum


while i < len(newList):
        print(newList[i])
        i+=1

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [] 

for fruit in fruits:
        if "a" in fruit:
                newlist.append(fruit)
print(newlist)  

newlist = [fruit for fruit in fruits if "m" in fruit]
print(newlist) 

newList.sort(reverse=True)
print(newList)  # ['plum', 'peach', 'pear', 'orange', 'melon', 'kiwi', 'grape', 'cherry', 'banana', 'apple']
newList.reverse()  # Reverse the order of the list
print(newList)  # ['apple', 'banana', 'cherry', 'kiwi', 'mango']

numbers = [1, 2, 3, 4, 5]
def myfunc(x):
        return abs(x-3)
numbers.sort(key=myfunc)
print(numbers)  # [5, 4, 3, 2, 1

newList= ["apple", "Banana", "cherry"]
newList.sort(key=str.lower)  # Sort the list in a case-insensitive manner
print(newList)  # ['apple', 'Banana', 'cherry']