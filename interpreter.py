expression = input ("Input your expression. Leave a space between the operator and the values e.g 1 + 1.\n ")

x, y, z = expression.split()

if y == "+":
    print (int(x) + int(z))
elif y == "-":
    print (int(x)- int(z))
elif y == "*":
    print (int(x) * int(z))
elif y == "/":
    print (int(x) / int(y))
else:
    print ("Enter a valid arithmetic expression")
