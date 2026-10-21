print ("==========NUMBER GUESSING GAME==========")

print ("\nHINT : the number is between 0 and 100!")
number=67
total_guesses=5
guess_no=1

guess= int(input("Guess the MYSTERY number! : "))

for i in range (1,6,1):

 
    if guess==67 :
        print ("CORRECT ANSWER!!")
        print ("Lives left!")

    elif guess>=50 or guess>=75:
        print ("HOT", "Try again!")

    elif guess>=40 or guess>= 85:
        print ("WARM", "almost there, TRY AGAIN!")

    elif guess>=25 or guess>=95:
        print ("COLD", "Try again")

    else:
        print ("ICE COLD!!", "Try again!")

    print ("THE NUMBER WAS= 67")



    