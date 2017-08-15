"""Antonio Hernandez"""

username = input("Please enter a username: ")
while username == "":
    username = input("Invalid Username. Please enter a valid username: ")

print("hello {}".format(username[::2]))
