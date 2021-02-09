#praise = "Archimedes is awesome"
#print(praise + " because he is calm.")

#print(praise.replace("awesome", "intelligent."))
#print(praise.index("i"))

#num = 2
#print(str(num) + " is my dearest number")

# functions involving numbers
#numb = -34.56
#print(abs(numb))

#raise_power = pow(5, 3 * pow(2, 2))
#print(str(raise_power) + " my second favorite number.")


# determining the maximum or minimum number
#determine = max(4, 6)
#print(determine)

#determine_one = range(0, 10)
#def bring():
    #for i in determine_one:
    #    print(i)
    
#bring()


# rounding numbers
#dec = 4.859
#print(round(dec))
#dec1 = 3.12
#print(round(dec1))


# other math functions can be accessed by importing 
#from math import *
#print(floor(dec1))
#print(ceil(dec1))

#print(complex(dec))

#square root
#print(sqrt(dec))


#input from user
#name = input("Enter your name: ")
#print("Welcome" + f"{name}")


#user_entry = input(int("Enter a number: "))
#sqrt = pow(user_entry, 3)
#print(sqt)

# adding numbers calculator
# int and float help in dealing with numbers be decimal or integers
# int handles whole numbers and float handles decimal numbers
#num = float(input("Enter a number: "))
#num1 = float(input("Enter a second number: "))
#result = num + num1
#print(result)

#if result > 1000:
#    print("We are rich now")
#else:
#    print("We need more cash for the job")


# list and accessing
#names = ["Belinda", "Angel", "Senam", "Tsikpo", "Elinam", "Evelyn", "Gifty"]

#print(names[:4])

#for name in names:
#    if name == "Evelyn":
#        print("She is my crush")
#        break
#    else:
#        print("Not my crush")


#print(names[-4])
#del names[0]
#print(names)
#names.insert("Belinda", names[0])
#print(names)

#names[0] = "Binidam"
#print(names)
#names.pop(1) 
#print(names)
#names1 = names[3:]
#print(names1)

# the function extend is the combination of two different list, this is also used in django templates
names = ["Belinda", "Angel", "Elinam", "Evelyn", "Gifty"]
age = [28, 30, 27, 29, 30]
#names.extend(age)
#print(names)  #['Belinda', 'Angel', 'Elinam', 'Evelyn', 'Gifty', 28, 30, 27, 29, 30]


#print(names.append(age)) #['Belinda', 'Angel', 'Elinam', 'Evelyn', 'Gifty', [28, 30, 27, 29, 30]]


# append actually takes an entire list and place it inside another list or just add a value to what you want to another list

# copy
#def nam():
#    carbon_copy = names.copy()
#    naming = [34, 39, 65, 28, 57]
#    carbon_copy.extend(naming)
#    carbon_copy.append(24)
#    if len(carbon_copy) < 10:
#        print("We need more space")
#    else: 
#        print("We are okay")
    

#print(nam())
   
# insert takes two arguments and the index and the value
#names.insert(0, "Charles")
#print(names)

#Remove also takes a value away
#names.remove("Charles")
#print(names)

# another method is clear, it gets rid of all values in the list
#names.clear()
#print(names)

#pop takes off value off the list the last item
#names.pop()
#print(names)

#index can be used to check if a value exist in a list
#print(names.index("Belinda"))

# count gives you the number of such values in the list
#carbon = names.copy()
#carbon.append("Belinda")
#carbon.append("Gifty")
#print(carbon)
#carbon.append("Belinda")
#print(carbon.count("Belinda"))

# the method sort actually place the list in ascending order
#names.sort()
#print(names)
#age.sort()
#print(age)

# reverse on the other hand turns the list upside down
#names.reverse()
#print(names)
#age.reverse()
#print(age)


# Tuples, they are immutable
coordinates = [(5, 6), (5, 67), (5, 9)]
for c in coordinates:
   print(c[1])


   #take note of how and not comparison signs are used in programming, to make ur programs smart
   


