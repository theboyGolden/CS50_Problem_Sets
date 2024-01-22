user_input = input("What is the name of the file whose extension you want to determine?\n")

# Extract the file extension (suffix) from the user input
file_extension = user_input.lower().split('.')[-1]

# In the line `file_extension = user_input.lower().split('.')[-1]`, the `split('.')` method is used to split the user input into a list of substrings using the dot ('.') as a separator. The `[-1]` is used to access the last element of the resulting list.

# Here's a breakdown:

#  `user_input.lower()`: Converts the user input to lowercase to handle case-insensitivity.
#  `split('.')`: Splits the user input into a list of substrings using the dot ('.') as a separator.
#  `[-1]`: Retrieves the last element of the resulting list.

# The purpose of using `[-1]` is to extract the file extension from the user input. For example, if the user enters "example.txt", after splitting the string using '.', you get `['example', 'txt']`. The `[-1]` ensures that you get the last element of the list, which is the file extension ('txt' in this case).

# In Python, negative indices are used to count elements from the end of a list. So, `[-1]` refers to the last element, `[-2]` would refer to the second-to-last element, and so on. This is a convenient way to access elements when you don't know the length of the list in advance.


if (file_extension  == 'gif' ):
    print ("The given file is a GIF image.")
elif (file_extension == 'jpg'):
    print("The given file is a jpg image.")
elif (file_extension == 'jpeg'):
    print("The given file is a jpeg image.")
elif (file_extension == 'png'):
    print("The given file is a png image.")
elif (file_extension == 'pdf'):
    print("The given file is a pdf file.")
elif (file_extension == 'txt'):
    print("The given file is a txt image.")
elif (file_extension == 'zip'):
    print("The given file is a zip image.")
else: 
    print ("application /octet-stream")