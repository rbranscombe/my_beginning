import random

x = random.randint(1, 14)

success = "You guessed it!"
guess_lo = "Guess too high!"
guess_hi = "Guess too low..."

guess_1 = int(input("Enter guess between 1 and 14 "))
#check if guess 1 is correct

if guess_1 == x:
    print(f"{success}  Got it on first try!")
else:
    if guess_1 > x:
        print(f"{guess_lo}")
    else:
        print(f"{guess_hi}")
        
    guess_2 = int(input("2nd guess..."))

    #check guess 2

    if guess_2 ==x:
        print(f"({success}  Got it on 2nd try!")
    else:    

        if guess_2 > x:
            print(f"{guess_lo}")
        else:
            print(f"{guess_hi}")
        
        guess_3 = int(input("Final guess..."))

        #check guess 3

        if guess_3 == x:
            print(f"{success}  Phew...well done!")
        else:
            print("WWWWAaaahhhhh.....ah....    luck for next time....")
            print(f"Number was {x} ")

