#Getting Started with Python
#CIS103 Introduction to Programming
#Professor - MD Ali
#Ndubuisi Mbamalu

my_dict={"age":41, "city":"chicago", "profession":"teacher"}
print(my_dict["city"])

#1
#Working with Lists
#the list 'fruits' created below
fruits = []
#Adding particular fruits to the list
fruits.append("apple")
fruits.append("banana")
fruits.append("orange")
fruits.append("grape")
#Printing the list of fruits
print("List of fruits:", fruits)
#Removing "banana" from the list
fruits.remove("banana")
#Printing the updated list
print("Updated list after removing 'banana':", fruits)
#Adding "strawberry" to the list
fruits.append("strawberry")
#Printing the final list
print("Final list of fruits:", fruits)

#2
#Using tuples
#creating the tuple 'clrs' with values
clrs = ("red", "green", "blue", "yellow")

#Printing the whole tuple
print("The entire tuple:", clrs)
#Accessing and printing the first and last elements of the tuple
print("First element:", clrs[0])
print("Last element:", clrs[-1])

#Trying to change the second element of the tuple
try:
    clrs[1] = "purple" # that would cause an error msg.
except TypeError as e:
    print("Error occurred:", e)

# Tuples are immutable, meaning that once a tuple is created,
# its elements cannot be modified or reassigned. Attempting to do so will
# result in a TypeError, that is displayed in the code above.

#3
#Working with sets
# Creating a set called 'student_names' with particular names
student_names = {"John", "Emma", "Sophia", "James"}

#Printing the initial set
print("Initial set of student names:", student_names)
#Adding "Oliver" to the set
student_names.add("Oliver")
#Printing the set after adding 'Oliver'
print("Set after adding 'Oliver':", student_names)
#Removing 'Sophia' from the set
student_names.remove("Sophia")
#Printing the set after removing 'Sophia'
print("Set after removing 'Sophia':", student_names)
#Trying to add 'John' again
student_names.add("John")
#Printing the set after trying to add 'John' again
print("Set after trying to add 'John' again:", student_names)

#Sets in Python do not allow duplicate elements. When we tried to add "John"
#again, the set remained unchanged because "John" was already present in the set.
#no error msg occurred and no change occurred.

#4
#Creating a dictionary called 'student_scores' with the particular key-value pairs
stdt_scs= {"John": 85,"Emma": 92,"Sophia": 78,"James": 89}
#Printing the dictionary
print("student scores:", stdt_scs)
#Accessing and printing Emma's score
print("Emma score:", stdt_scs["Emma"])
#Adding a new student 'Oliver' with a score of 95
stdt_scs["Oliver"] = 95
#Updating Sophia's score to 82
stdt_scs["Sophia"] = 82
#Printing the updated dictionary
print("new student scores:", stdt_scs)

