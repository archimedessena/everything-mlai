# Translator language
#All vowles should be equal to q
def translate(phrase):
    trans = ""
    for i in phrase:
        if i.lower() in "aioue":
            if i.isupper():
                 trans = trans + "Q"
            else:
                 trans = trans + "q"
        else:
           trans =  trans + i
    return trans

print(translate(input("Enter a phrase: ")))