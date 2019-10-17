import random
name_1 = input("what is your name? ")
name_2 = input("what is the other persons name? ")
percentage = random.randint(0, 101)

if percentage == 0:
    print("Your friendship is terrible, break up")
elif percentage > 0 and percentage < 26:
    print("Ehhhh ya need some work......a lot of work")
elif percentage > 25 and percentage < 51:
    print("Your friendship is decent, but it still needs work")
elif percentage > 50 and percentage < 76:
    print(".......Okay")
elif percentage > 75 and percentage < 91:
    print("Pretty good!")
else:
    print("Best friends!")



