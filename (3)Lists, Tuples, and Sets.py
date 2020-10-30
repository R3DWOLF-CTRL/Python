# What is a list?
# A list us a collection of iteems in a particular order.
# You can make a list that includes the letters of the alphabet, the digits from 0-9, or
# the names of all the people in your family. You can put anything you want into a
# list, and the items don't have to be related in any particular way. Because a
# list usually contains more than one element, it's a good idea to make a name of
# your list plural, such as letters, digits, or names.
# In Python, square brackets ([]) indicate a list, and individual elements in the
# list are seperated by commas.

# Eg:
courses = ['Music', 'Math', 'POB', 'History', 'Physics', 'CompSci']

print(courses)


# Accessing Elements in a List - Lists are orded collections, so you can access
# any element in a list by telling Python the position, or the index, of the item desired.
# To access an element in a list, writ the name of the list followed by the index of the
# item enclosed in square brackets. Indexes always starts at 0 not 1.

# for example:
courses = ['Music', 'Math', 'POB', 'History', 'Physics', 'CompSci']

print(courses[5])

# This output will be CompSci since the fifth index is the last item in our List
# They're six items in our list but since the first index is always 0, the 5th
# index is CompSci, so total amount of items in your list and subtract 1. This will
# give you your max index range. 6 - 1 = 5 is our max value. Range = [0:5]

# Let's see what happens when we go out of this Range
courses = ['Music', 'Math', 'POB', 'History', 'Physics', 'CompSci']

print(courses[5])
# print(courses[8])
# Python - (3)Lists, Tuples, and Sets.py:22
# ['Music', 'Math', 'POB', 'History', 'Physics', 'CompSci']
# Traceback (most recent call last):
# File "E:\Python tutorials\(3)Lists, Tuples, and Sets.py", line 22, in <module>
# print(courses[8])
# IndexError: list index out of range

# Using individual values from a list - You can use individual values from a list
# just as you would any other variable. For example you can use concatecation to
# create a message based on a value from a list.
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = "My first bicycle was a " + bicycles[3].title() + "."
print(message)

# Here we're grabbing everything from the first index[0] all the way to second index [2]
# but not including anything past index [2]
# So from 'Music' to 'POB' from the list by using [:2] in Python you don't have
# to put the 0 because Python is assuming that you want to start from the
# first index which is 0.
courses = ['Music', 'Math', 'POB', 'History', 'Physics', 'CompSci']

print(courses[:2])

# Here we're grabbing everything from the second index to the last index in the list,
# by using [2:] once again python assumes you want to go to the last item in the list.
courses = ['Music', 'Math', 'POB', 'History', 'Physics', 'CompSci']

print(courses[2:])

# Changing, Adding, and Removing Elements
# Most lists you create will be dynamic, meaning you'll build a list and then add and remove
# elements from it as your program runs its course. For example, you might want to create a
# game in which a player has to shoot aliens out of the sky. You could store the initial set
# of aliens in a list and then remove an alien from the list each time one is shot down.
# Each time a new alien appears on the screen, you add it to the list. Your list of aliens
# will decrease and increase in length throughout the course of the game.

# Modifying Elements in a List
# The syntax for modifying an element is similar to the syntax for accessing an element in
# a list. To change an element, use the same name of the list followed by the index
# of the element you want to change, and then provide the new value you want the item to
# have. For example, let's say we have a list of motorcycles, and the first item in the
# list 'honda'. How would we change the value of this first item?
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# NOTE you can change the value of any item of the list, not just the first item.

# Adding Elements to a List
# You might wnat to add a new element to a list for many reasons. For example, you
# might want to make aliens appear in a game, add new data to a visualization, or add new
# registered users to a website you've built. Python provides several ways to add new data
# to existing lists.

# Appending Elements to a list
# The simplest way to add a new element to a list is to append the item to the list.
# When you append an item to the list, the new element is added to the end of the list.
# Using the same list we had in the previous example, we'll add the new element 'ducati'
# to the end of our list:
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

# The append() method makes it easy to build lists dynamically. For example, you can
# start with an empty list and then add items to the list using a series of append()
# statements. Using an empty list, let's add the elements 'honda', 'yamaha', and 'suzuki'
# to the list:
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

# The resulting list looks exactly the same as the lists in the previous examples:
motorcycles = ['honda', 'yamaha', 'suzuki']

# Building a list this way is very common, because often won't know the data your
# users want to store in a program until after the program is running. To put your
# users in control, start by defining an empty list that will hold the users' values.
# Then append each new value proviided to the list you just created.

# Inserting Elements to a List
# You can add a new element at any position in your list by using the insert()
# method. You do this by specifying the index of the new element and the value of the
# new item.
motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati')
print(motorcycles)

# In this example, the code at 1 inserts the value 'ducati' at the beginning of the
# list. The insert() method opens a space at position 0 and stores the value 'ducati'
# at that location. This operation shifts every other value in the list one position to the right.
motorcycles = ['ducati', 'honda', 'yamaha', 'suzuki']


# Finally the last way to add an item to the list is to use the extend method
# .extend() with this method you can't do what the insert and append methods can do.
courses = ['Music', 'Math', 'POB', 'History', 'Physics', 'CompSci']
courses_2 = ['Art', 'Education']

courses.extend(courses_2)

print(courses)

# Removing Elements from a List
# Often, you'll want to remoge an item or a set of items from a list. For example,
# when a player shoots down an alien from the sky, you'll most likely want to remove
# it from the list of active aliens. Or when a user decides to canel their account
# on a web application you created, you'll want to remove that user from the list
# of active users. You can remove an item according to its position in the list
# or according to its value.

# Removing an Item Using the del Statement
# If you know the position of the item you want to remove from a list, you can
# use the del statement.

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

# The code at 1 uses del to remove the first item, 'honda', from the list of
# motorcycles:
['honda', 'yamaha', 'suzuki']
['yamaha', 'suzuki']

# You can remove an item from any position using the del statement if you know
# its index. For example, here's how to remove the second item, 'yamaha', in the
# list:

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[1]
print(motorcycles)

# The second motorcycle is deleted from the list:
['honda', 'yamaha', 'suzuki']
['honda', 'suzuki']
# In both examples you can no longer access the value that was removed from the
# list after the del statement is used.

# Removing an Item Using the pop() Method
# Sometimes you'll want to use the value of an item after you remove it from a
# list. For example, you might want to get the x and y position of an alien that
# was just shot down, so you can draw an explosion at that position. In a web
# application, you might want to remove a user from a list of active members and
# then add that user to a list of inactive members.
# The pop() method removes the last item in the list, but it lets you work with
# that item after removing it. The term pop comes from thinking of a list as a
# stack of items and popping one item off the top of the stack. In this analogy,
# the top of a stack corresponds to the end of a list.
# Let's pop a motorcycle from the list of motorcycles:

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# We start by defining and printing the list motorcycles at 1. At 2 we pop a
# value from the list and store that value in the variable popped_motorcycle. We
# print the list at 3 to show that a value has been removed from the list. Then
# we print the popped value at 4 to prove that we still have access to the value
# that was removed.
['honda', 'yamaha', 'suzuki']
['honda', 'yamaha']
['suzuki']

# How might this pop method be useful? Imagine that the motorcycles in the list
# are stored in choronlogical order according to when we owned them. If this is
# case, we can use the pop() method to print a statement about the last motorcycle
# we bought:

motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

# The output is a simple sentence about the most recent motorcycle we owned:

# The last motorcycle I owned was a Suzuki.

# Popping Items from any Position in a List
# You can actually use pop() to remove an item in a list at any position by
# including the index of the item you want to remove in parentheses.

motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + ".")

# We start by popping the first motorcycle in the list at 1, and then we print
# a message about that motorcycle at 2. The output is a simple sentence
# describing the first motorcycle I ever owned:

# The first motorcycle I owned was a Honda.

motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(1)
print('The first motorcycle I owned was a ' + first_owned.title() + ".")

# Result: The first motorcycle I owned was a Yamaha.

# Remember each time you use pop(), thee item you work with is no longer stored
# in the list.
# If you're unsure whether to use the del statement or the pop() method, here's
# a simple way to decide: when you wnat to delete an item from a list and not
# use that item in any way use the del statement; if you want to use an item as
# you remove it, use the pop() method.

# Removing an Item by Value
# Sometimes you won't know the position of the value you want to remove from the
# list. If you only know the value of the item you want to remove, you can use
# the remove() method. For example, let's say we want to remove the value 'ducati'
# from the list of motorcycles.

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

# The code at 1 tells Python to figure out where 'ducati' appears in the list
# and remove that element

['honda', 'yamaha', 'suzuki', 'ducati']
['honda', 'yamaha', 'suzuki']

# You can also use the remove() method to work with a value that's being removed
# from a list. Let's remove the value 'ducati' and print a reason for removing
# it from the list:

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

# After defining the list at 1, we store the value 'ducati' in a variable called
# too_expensive 2. We then use this variable to tell Python which value to remove
# from the list at 3. At 4 the value 'ducati' has been removed from the list
# but is still stored in the variable too_expensive, allowing us to print a
# statement about why we removed 'ducati' from the list of motorcycles:

['honda', 'yamaha', 'suzuki', 'ducati']
['honda', 'yamaha', 'suzuki']

# A Ducati is too expensive for me.

# NOTE- The remove() method deletes only the first occurrence of the values you
# specify. If there's a possibility the value appears more than once in the list,
# you'll need to use a loop to determine if all occurrences of the value have
# been removed. You'll learn how to detemine this in Chapter 7.
