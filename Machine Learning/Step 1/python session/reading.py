# reading a file 
# you will have to use open function, r is for read, w write, r+ both read and write or appending
# the file some point in time should be close
#reading = open("res.txt", "r")
# print(reading.read()) # for reading
#print(reading.readable()) # checking if the files is readable
# print(reading.readlines()) # to read entire file or line readline
#print(reading.readlines())
#reading.close()
#accessing a particular line this can be done by using the index ()[3]
#zip_file = open("foot.csv", "r")
#print(zip_file.readable())
#print(zip_file.readlines()[3])

#for i in zip_file.readlines():
#    if i[6]:
#        print(i)
#    #print(i)
#        break
#    else:
#        print("DOne")
    

#zip_file.close()

person = open("person.sql", "r")
#print(person.readlines())

for people in person:
    print(people)

person.close()