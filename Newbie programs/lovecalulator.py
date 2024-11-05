name1 = input("Enter your name: ")
name2 = input("Enter their name: ")
name= name1+name2

t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")
love1= t+r+u+e

l = name.count("l")
o = name.count("o")
v = name.count("v")
e = name.count("e")
love2= l+o+v+e

score= int(str(love1)+str(love2))
if score<10 or score>90:
    print(f"your score is {score}, you are like coke and mentos to each other.")
elif score>40 and score<50:
    print(f"Your score is{score}, you are al right together.")
else:
    print(f"Your score is {score}")