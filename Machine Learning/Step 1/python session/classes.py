#class Journalist:
#    def __init__(self, company=None, first_name=None, salary=None):
#        self.first_name = first_name
#        self.company = company
#        self.salary = salary
#        
#        
#    def your_name(self):
#        name = input("Please what is your name?: ")
#        print("Oh you are the" + name)
#        print("You are welcome to the club", name)
#    
#
#    def which_company(self):
#        name_of_company = input("What is the name of your name company?: ")
#        if name_of_company == "Joy" or "Adom" or "TV3"  or "Citi" or "Peace":
#            print("I can grant you this interview")
#        if name_of_company == name_of_company:
#            print("I can't grant you this interview because you are not from credible company")
#    
#  
#    def how_much(self):
#        pay = input("How much is your pay?: ")
#        usage = input("How do u use your pay?: ")
#        if pay == 3000 and usage == "School fees":
#            print("You are born to be a great person")
#            keep = []
#            print(keep.append(pay))
#            keeps = []
#            print(keeps.extend(keep))
#            
#        else:
#            print("You will be useless in no time")
#

#class Banker(Journalist):
#    pass
   

#journ = Journalist("")
#print(journ.how_much())
#bank = Banker("Joy", "Miss Odetee", "4000")
#print(bank.how_much())



class Student:


    def __init__(self, name, gpa, major, is_on_probation):
        self.name = name
        self.gpa = str(gpa)
        self.is_on_probation = is_on_probation
        self.major = major



student2 = Student("Arc", 4.0, "Science", False)

print(student2.name())

    