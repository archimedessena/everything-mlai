#try:
#    #v = 10/0
#    number = int(input("Enter a number: "))
#    print(number)
#except ZeroDivisionError as err:
#    #print("Divided by zero")
#    print(err)
#except ValueError as k:
#    #print("Invalid input")
#    print(k)

try:
    name = int(input("Enter a nice number: "))
    v = name ** 2
    print(v)
except ValueError:
    print("Type a number not a letter")