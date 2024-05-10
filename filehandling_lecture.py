# FILE HANDLING
# options for file handling
# "r" - reading the file - accessing information from the file - throw an error if the files doesn't exist
# "w" - writing to the file - allows us to send information to the file - create the file if it doesnt exist
# this will overwrite any information currently in the file
# "a" append to the file - doesnt interfere with what already exists - creat the file if it doesn't exist
# it just adds to the file

# opening a file
file = open("my_garden.txt", "w") # my_garden.txt does not exist, because im writing, it creates the file
file.close() # close the file for writing
# writing to a folder outside of the current directory
# ============================ RELATIVE PATH ================================
# Relative Path to another folder
# is the path the file from the current directory
# file = open("garden\\my_garden.txt", "w") # pc double \ because \ escapes characters so we're escaping the python escape character
# file = open("garden/my_garden.txt", "w") # mac

# ============================ ABSOLUTE PATH ======================
# absolute path is the full address to that location
# file = open("C:\\Users\\rrhoa\\OneDrive\\Documents\\CodingTempleBECore\\week_2\\day_5\\another_gardedn.txt", "w")
# be mindful when using the absolute path becuase this is going to be different
# across different computers

# closing a a file after its been opened
file = open("my_garden.txt", "r") #open my_garden.txt for reading - reassigning the variable with open for reading and close the previous operation for writing
# perform file operations looping and what not
file.close() # close the file
# file.closed <- attribute that will be true or false depending on if the file is open or closed
print(file.closed)


# using with to open files and automatically close those files 
# after the block of code
with open("my_garden.txt", "r") as file:
    pass    
    #read the file
    # do file reading stuff like looping
# the file is automatically closed here

# open two files at the same time with different operations and work within those files
with open("my_garden.txt", "r") as file1, open("garden_notes.txt", "w") as file2:
    # read from one file1
    # write to file2
    pass

# writing text to a file
with open("my_garden.txt", "w") as file:
    # file.write("thing we're writing to the file")
    flower = "sunflowers"
    file.write(f"Today, I planted new {flower}.") #write text to the file (puts text in the file)
# closes outside of the code block
# write to a file after closing, it will overwrite the file
# with open("my_garden.txt", "w") as file:
#     # file.write("thing we're writing to the file")
#     file.write("Today, I planted new begonias.")
# closes outside

print("\nHello") #example of printing a new line character

# appending to a text file
# "a" as second argumetn tells the file we're appending to it
with open("my_garden.txt", "a") as file:
    # \n for formatting because otherwise this just adds to the back of the current
    file.write("\nNote: Water the sunflowers daily!")
# writing to files will often require some kind of formatting
# \n will bump us down to the next line in the text file

from datetime import date
with open("my_garden.txt", "a") as file:
    file.write(f"\n{date.today()}: Pruned the rose bushes")


# reading lines from a text file
with open("my_garden.txt", "a+") as file:
    file.write("\nDid some garden stuff")
    file.write("\npruned some bushes")    
    file.seek(0) # resets the position of the cursor in the text file - offsets by 0 positions
    for line in file:
        print(line)

# looping with readlines()
with open("my_garden.txt", "r") as file:
    # for line in file:
    #     print(line.strip())    
    my_lines = file.readlines() # return a list of each of the lines from my text file
    print(my_lines)
    for line in my_lines:
        print(line.strip())

# .read() - takes the whole file as one single string
with open("my_garden.txt", "r") as file:
    content = file.read()
    print(type(content)) # str
    print(content)
    for letter in content:
        print(letter)

# conditionals with our file content
with open("my_garden.txt", "r") as file:
    for line in file:
        if "sunflowers" in line:
            print(line.strip())

# looping through lists and adding the content to a text file
flowers = ["Sunflower", "Rose", "Lavender"]
with open("my_garden_flowers.txt", "w") as file:
    for flower in flowers:
        file.write(flower+"\n")

# adding contents from a text file to a list
flowers = []
with open("my_garden_flowers.txt", "r") as file:
    for line in file:
        flowers.append(line.strip())
print(flowers)
# EXPORT - adding to a text file from a dictionary
garden_care = {'Sunflower': 'full sun', 'Rose': 'prune regularly', 'Lavender': 'well-drained soil'}
with open("garden_care.txt", "w") as file:
    for plant, care in garden_care.items():
        file.write(f"{plant}: {care}\n")

#IMPORT from a text file to a dictionary
garden_care = {}
with open("garden_care.txt", "r") as file:
    for line in file:
        plant, care = line.strip().split(": ")
        garden_care[plant] = care
print(garden_care)

# EXPORT with nested dictionaries
garden_care = {"Sunflower": {"sunlight": "full sun", "water": "it needs some water", "pruning": "prune it"},
               "Rose": {"sunlight": "full sun", "water": "it needs some water", "pruning": "prune it"}}
with open("garden_care.txt", "w") as file:
    for plant, care in garden_care.items():
        file.write(f"{plant}:\n")
        for care_type, quantity in care.items():
            file.write(f"   {care_type}: {quantity}\n")

# EXPORT - adding to a text file from a dictionary
garden_care = {'Sunflower': 'full sun', 'Rose': 'prune regularly', 'Lavender': 'well-drained soil'}
with open("garden_care.txt", "w") as file:
    for plant, care in garden_care.items():
        file.write(f"{plant}: {care}\n")


# EXCEPTION HANDLING with FILES
try:
    with open("my_garden.txt", "r") as file:
        for line in file:
            print(line.strip())
except Exception as e:
    print(f"An error occurred: {e}")

# if we try to read a file that does not exist this will throw an exception
# without stopping the code from running
try:
    with open("my_cool_garden.txt", "r") as file:
        for line in file:
            print(line.strip())
except Exception as e:
    print("please make sure that file exists")
    print(f"An error occurred: {e}")
# with open("my_cool_garden.txt", "r") as file:
#     for line in file:
#         print(line.strip())
print("hello")

# Common errors you may encounter with file handling
# FileNotFoundError - trying to read a file that doesnt exist
# PermissionError - our script does not have permission to access the file
# IOError - some kind of interruption happens or file corruption

# file = open("my_garden.txt", "w")
# file.close()
# file.write("Hello")
# Trying to write to a closed file gives a ValueError


# ========== Finding our location in a file ===============
with open("my_garden.txt", "r") as file:
    print(file.read(32)) # can take an integer as arguemtn and will read up to that position
    position = file.tell() #Tell us our current position in the file
    print(f"We are at position: {position}")
    print(file.read())
# each .read() call will pick up where the last one left off
with open("my_garden.txt", "r") as file:
    first_part = file.read(7)
    position = file.tell() # current position in file
    print(f"we're at position: {position}")
    first_part = file.read(25)
    position = file.tell() # current position in file
    print(f"we're at position: {position}")
    first_part = file.read(46)
    position = file.tell() # current position in file
    print(f"we're at position: {position}")

# .seek() - take us to a specifc position in the file
# takes an integer as an arugment which represents a position in the file
with open("my_garden.txt", "r+") as file:
    file.seek(0) #move to the beginning of the file
    first_line = file.readline() # read the first moving my position to the end
    print(f"The first line of the file is: {first_line}")
    file.seek(0)
    print(file.readlines())
    print(file) # file object
    for line in file:
        print(line)

# making an edit at a specific position with seek
# with open("my_garden.txt", "r+") as file:
#     file.seek(14) # moving my marker to position 14
#     # make a change at that specific location
#     file.write("\nGARDENING IS SO FUN OMG")

# with open("my_garden.txt", "r+") as file:
#     file.seek(150)
#     file.write("\nandy pls")
# ^ the file is going to increase in size to accomadte the extra space
# the spaces that exist between the new position and the last position 
# will be filled with null bytes so that the file can expand

# a little bit of regex for your files
import re
with open("garden_care.txt", "r") as file:
    content = file.read()
    print(content)
    matches = re.findall(r"Rose", content)
    print("Occurrences of Rose", matches)

# EXAMPLE FOR FUNCTION OF EXPORTING TO A FILE 
# using a function for file handling
def add_garden_log(filename, entry):
    with open(filename, "a") as file:
        file.write(entry)

# calling the function with the text file and string to enter into the text file
add_garden_log("my_garden.txt", "\nDay 23: The plants have come alive. I've lost the big toe on my right foot. Please send help")


# os module - allows us to interact with the file structure of our computer
# we can add folders
# we can rename folders
# create files in those folders

# import os #imports the os module from python
# os.makedirs("my_garden_files", exist_ok=True)
# print("Created a new directory")

# variable for my_garden.txt file
# old_file = "my_garden.txt"
# # crfeating a path between the my_garden_files folder and the my_garden.txt file
# new_path = os.path.join("my_garden_files", old_file)
# # move my file from its current location to the new path
# # renaming the location?
# os.rename(old_file, new_path)




# EXPORT with nested dictionaries
garden_care = {"Sunflower": {"sunlight": "full sun", "water": "it needs some water", "pruning": "prune it"},
               "Rose": {"sunlight": "full sun", "water": "it needs some water", "pruning": "prune it"}}
with open("garden_care.txt", "w") as file:
    for plant, care in garden_care.items():
        file.write(f"{plant}:\n")
        for care_type, quantity in care.items():
            file.write(f"----{care_type}: {quantity}----\n")




with open("goobs.txt", "a") as file:
    print("hello")





        




    
    











