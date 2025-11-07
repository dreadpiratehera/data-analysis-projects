my_string = "LaunchCode"


# a) Use string methods to remove the first three characters from the string and add them to the end.

beg_string = my_string[3:]
end_string = my_string[:3]
newstring = beg_string + end_string
print (newstring)

# Use a template literal to print the original and modified string in a descriptive phrase.

print(f"The original string is {my_string}, the modified string is {newstring}")



# b) Modify your code to accept user input. Query the user to enter the number of letters that will be relocated.


mod = 0
while mod == 0:
    mod = int(input("How many characters do you want to move to the end?"))

beg_string = my_string[(mod):]
end_string = my_string[:(mod)]
newstring = beg_string + end_string

print(f"The original string is {my_string}, the modified string is {newstring}")


# c) Add validation to your code to deal with user inputs that are longer than the word. 
# In such cases, default to moving 3 characters. Also, the template literal should note the error.

mod = 0
while mod == 0:
    mod = int(input("How many characters do you want to move to the end?"))

if mod >10:
    beg_string = my_string[3:]
    end_string = my_string[:3]
    newstring = beg_string + end_string
    print(f"Too many character selected. Default of 3 chosen insead.")


else:
    beg_string = my_string[(mod):]
    end_string = my_string[:(mod)]
    newstring = beg_string + end_string

print(f"The original string is {my_string}, the modified string is {newstring}")
