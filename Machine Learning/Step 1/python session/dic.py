#dic = {
#    "name": "Archimedes",
#    "age": 32,
#    "interest": "music",
#    "occupation": "Soft Developer"
#}

#print(dic["name"])
#dic["name"] = "Sena"
#print(dic["name"])


num_of_days_in_month = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

#i = num_of_days_in_month.values() 
k = num_of_days_in_month.keys()

for i in num_of_days_in_month:
    if i == 30:
        print(num_of_days_in_month)
