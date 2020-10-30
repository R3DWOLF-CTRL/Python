# If you want to put the text in your string into lowercase, uppercase or titlecase
# We can use these methods .lower() for lowercase, .upper() for uppercase and
# .title() for titlecase which just puts the first letter of your string into a capital
# letter.

# Eg of titlecase
message = "i love chefette"
print(message.title())

# Eg of lowercase
message = 'HELLO WORLD'
print(message.lower())

# Eg of uppercase
message = "how are you shamona?"
print(message.upper())

# Count method counts the specific item that we input and gives us back a value.
message = 'Hello World'
print(message.count('Hello'))

# Here it is counting how many l's do we have in our message variable "hello world!"
message = "hello worlddd!"
print(message.count('l'))

# Find method gives us the index for the value which we ask to find.
message = 'hello world'
print(message.find('hello'))


message = 'hello world'
print(message.find('world'))

# Here we're trying to find 'Universe' but Universe isn't in our string.
message = " HELLO world"
print(message.find('Universe'))

greeting = " how are you mane"
name = "pluto"
message = f'{greeting} {name}. Welcome'

print(message)

# help() function gives us info on a method or function.
greeting = 'hello'
name = 'elias'

print(help(str.lower))
