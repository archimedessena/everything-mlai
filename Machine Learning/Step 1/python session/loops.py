#j = 0
#n = 0
#while j < 9:
#    n = j + j
#    print(n)
#    j += 1

# while loop for a song playing in a playlist
# check if the user wants to put the song on repeat
# if yes 
# let the song play until the user takes it from repeat
#repeat_song = False
#while repeat_song:
#    print("Continue playing until the user ask no more")
#else:
#    print("Song is changed")


# more on while
#i = 1
#j = 0
#while i <= 10:
#    j = j + i
#    print(j)
#    i += 1

#print("Done with loop")   


#Guessing game
#secret_word = str(2579)
#guess = ""
#guess_count = 0
#guess_limit = 3
#out_of_guess = False
#while guess != secret_word and not(out_of_guess):
#    if guess_count < guess_limit:
#        guess = input("Enter guess: ")
#        guess_count += 1
#    else:
#        out_of_guess = True

#if out_of_guess:
#    print("Out of Guesses, YOU LOSE!")
#else:
#    print("You win!")
       


# for loop
#friends = ["lof", "men"]

#for i in range(len(friends)):
#    #print(friends[i])
#    print(friends[0])


# exponential function
#def raise_to_power(base, power):
#    answer = 1
#    for i in range(power):
#        answer = answer + base
#    return answer


#print(raise_to_power(2, 5))




#def a():
#    num = int(input("Enter: "))
#    var = 0
#    ad = 0
#    while var < num:
#        for i in range(num):
#            ad = ad + i
#        return ad
#        var += 1


#print(a())



real_name = "Archimedes"
initial_answer = 0
answer = ""
number_of_limit = 5
out_of_answer = False
while answer != real_name and not(out_of_answer):
    if initial_answer < number_of_limit:
        answer = input("What is your name?: ")
        initial_answer += 1
    else:
        out_of_answer = True

if out_of_answer:
    print("You are really lying")
else:
    print("I love your name,", answer)