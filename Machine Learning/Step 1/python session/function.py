#def nt(a, b):
#    if a > b:
#        return b
#    else:
#        return a
#
#n = nt(4, 3)


#def greeting(name, age):
#    return (name + " is " + str(age))

#gret = greeting("Archimdes", 45)
#print(gret)



#def cube(num):
#    numb = pow(num, 3)
#    return numb

#ans = cube(3)
#print(ans)


# combining funcitons, if, else, or , and, boolean

# COVID prevention measures
#is covid available
#if yes
#wash hands
#use sanitizer
#social distance yourelf

from play_safe import *

covid_available = True

def precautions():
    if covid_available:
        wash_hand()
        use_sanitizer()
        social_distant()
    else:
        feel_feel()


pre = precautions()
print(pre)


