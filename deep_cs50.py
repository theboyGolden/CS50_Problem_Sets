user_input = input("What is the answer to the Great Question of Life, the Universe and Everything?\n")

if user_input == '42':
    print("Yes")
elif user_input.lower() == 'forty-two':
    print("Yes")
elif user_input.lower() == 'forty two':
    print("Yes")
else:
    print("No")
