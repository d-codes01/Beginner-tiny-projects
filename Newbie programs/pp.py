#day2

# w=input("enter the weight:")
# h=input("enter the height")
# BMI= int(w)/float(h)**2
# print(BMI)

# score = 2
# height = 3
# is_winning = True
# print(f"your score is {score}, your height is {height} and your winning is {is_winning}")

# age = input("Enter your age:")
# 32850
#4680
#1080
# days= 32850 - (int(age)*365)
# weeks= 4680 -(int(age)*52)
# months= 1080-(int(age)*12)
# print(f"you have {days} days, {weeks} weeks and {months} months.")67

# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill?"))
# per = float(input("How much percent tip would you like to give?"))
# num = int(input("How many people to split the bill?"))
# total= bill+per*bill/100
# each = total/num
# exact  = round(each,2)
# print(f"Each person should pay {exact}")

#day3

# height = int(input("Enter the height "))
# if height<120:
#     print ("Can't ")
# else:
#     print("can")

# number=int(input("Enter the number: "))
# if number%2==0:
#     print("It is an even number")
# else:
#     print("It is an odd number")
    
# weight = int(input("Enter your weight: "))
# height = float(input("Enter your height: "))
# bmi = weight/height**2
# if bmi<18.5:
#     print(f"Your bmi is {bmi}, you are underweight.")
# elif bmi<25:
#     print(f"Your bmi is {bmi}, your weight is normal.")
# else:
#     print(f"Your bmi is{bmi},you are an obese.")


# year = int(input("Enter the year: "))
# if year%4!=0:
#     print("Not a leap year.")
# else:
#     if year%100==0:
#         if year%400==0:
#             print("Leap year")
#         else:
#             print("Not a leap year")
#     else:
#         print("Leap year")

# size= input("Enter the size of pizza: ")
# if size=="L":
#     price=25
# elif size=="M":
#     price=20
# elif size=="S":
#     price=15
# pep = input("Do you want pepperoni? ")
# if pep=="Y":
#     if size=="S":
#         price+=2
#     elif size=="L":
#         price+=3
# extra = input("Do you want extra cheese? ")
# if extra== "Y":
#     price+=1
#     print(f"Your total bill is ${price}")
# elif extra== "N":
#     print(f"Your total bill is ${price}")
        
# name1 = input("Enter your name: ")
# name2 = input("Enter their name: ")
# name11 = name1.lower()
# name22= name2.lower()

# l1 = int(name11.count("l"))
# o1 = int(name11.count("o"))
# v1 = int(name11.count("v"))
# e1 = int(name11.count("e"))
# love1= l1+o1+v1+e1

# l2 = int(name22.count("l"))
# o2 = int(name22.count("o"))
# v2 = int(name22.count("v"))
# e2 = int(name22.count("e"))
# love2= l2+o2+v2+e2

# score= int(str(love1)+str(love2))

# if score<10 or score>90:
#     print(f"your score is {score}, you are like coke and mentos to each other.")
# elif score>40 and score<50:
#     print(f"Your score is{score}, you are al right together.")
# else:
#     print(f"Your score is {score}")

# name1 = input("Enter your name: ")
# name2 = input("Enter their name: ")
# name= name1+name2

# t = name.count("t")
# r = name.count("r")
# u = name.count("u")
# e = name.count("e")
# love1= t+r+u+e

# l = name.count("l")
# o = name.count("o")
# v = name.count("v")
# e = name.count("e")
# love2= l+o+v+e

# score= int(str(love1)+str(love2))
# if score<10 or score>90:
#     print(f"your score is {score}, you are like coke and mentos to each other.")
# elif score>40 and score<50:
#     print(f"Your score is{score}, you are al right together.")
# else:
#     print(f"Your score is {score}")

# print('''                                      /
#                         _,.------....___,.' ',.-.
#                      ,-'          _,.--"        |
#                    ,'         _.-'              .
#                   /   ,     ,'                   `
#                  .   /     /                     ``.
#                  |  |     .                       \.\
#        ____      |___._.  |       __               \ `.
#      .'    `---""       ``"-.--"'`  \               .  \
#     .  ,            __               `              |   .
#     `,'         ,-"'  .               \             |    L
#    ,'          '    _.'                -._          /    |
#   ,`-.    ,".   `--'                      >.      ,'     |
#  . .'\'   `-'       __    ,  ,-.         /  `.__.-      ,'
#  ||:, .           ,'  ;  /  / \ `        `.    .      .'/
#  j|:D  \          `--'  ' ,'_  . .         `.__, \   , /
# / L:_  |                 .  "' :_;                `.'.'
# .    ""'                  """""'                    V
#  `.                                 .    `.   _,..  `
#    `,_   .    .                _,-'/    .. `,'   __  `
#     ) \`._        ___....----"'  ,'   .'  \ |   '  \  .
#    /   `. "`-.--"'         _,' ,'     `---' |    `./  |
#   .   _  `""'--.._____..--"   ,             '         |
#   | ." `. `-.                /-.           /          ,
#   | `._.'    `,_            ;  /         ,'          .
#  .'          /| `-.        . ,'         ,           ,
#  '-.__ __ _,','    '`-..___;-...__   ,.'\ ____.___.'
#  `"^--'..'   '-`-^-'"--    `-^-'`.''"""""`.,^.`.--' mh
#  ''')
# print("Welcome to the game.\nYour mission is to find the treasure.")
# choice1=input("Which turn do you wanna take right or left? ").lower()
# if choice1== "right":
#     print("you lose")
# elif choice1== "left":
#     choice2= input("Do you want to swim or wait?").lower()
#     if choice2== "swim":
#         print("Game over!!")
#     elif choice2== "wait":
#         choice3= input("Which door do you wanna go blue, yellow or red? ").lower()
#         if choice3== "blue":
#             print("Game over!!")
#         elif choice3== "yellow":
#             print("Game over!!")
#         else:
#            print("You won!!")

# day 4

# import random
# num_seed = int(input("Create a seed."))
# random.seed(num_seed)
# rand_num= random.randint(0,1)
# if rand_num== 1:
#     print("Heads")
# else:
#     print("Tails")

# import random
# seedn = int(input("Enter the seed number:"))
# random.seed(seedn)

# names= input("Give everybody's name, separated by coma.")
# splitname= names.split(", ")

# length= len(splitname)
# num= random.randint(0,length-1)
# payer= splitname[num]
# print(payer+" will pay the bill.")

# usa_cities = ["New York","Seatle","San Francisco","Atlanta","Massachussets"]
# usa_states = ["California","Florida","Washington","Arkansas"]
# usa_cities.extend(['Miami','Texas'])
# usa_states.append("LA")
# print(usa_cities)
# print(usa_states)
# usa = [usa_cities,usa_states]
# print(usa)

# row1=["⬜","⬜","⬜"]
# row2=["⬜","⬜","⬜"]
# row3=["⬜","⬜","⬜"]
# map=[row1,row2,row3]
# print(f"{row1}\n{row2}\n{row3}")
# position=input("Where do you want to place the treasure?")
# vertical = int(position[0])
# horizontal = int(position[1])
# map[horizontal-1][vertical-1]= "X"
# print(f"{row1}\n{row2}\n{row3}")

# import random
# rock='''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
# paper='''
#     _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)
# '''
# scissors='''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# choice= int(input("Choose 0 for rocks, 1 for paper and 2 for scissors. "))
# if choice==0:
#     print(rock)
# elif choice==1:
#     print(paper)
# else:
#     print(scissors)
# comp_choice= random.randint(0,2)
# if comp_choice==0:
#     print(rock)
# elif comp_choice==1:
#     print(paper)
# else:
#     print(scissors)
# if choice==comp_choice:
#     print("Draw!")
# elif (choice ==0 and comp_choice==1) or (choice==1 and comp_choice==2) or (choice==2 and comp_choice==0):
#     print("You lose!!")
# elif (choice ==1 and comp_choice==0) or (choice==2 and comp_choice==1) or (choice==0 and comp_choice==2):
#     print("You win!!!")
# else:
#     print("Invalid character. You lose")

# day 5

# student_heights= input("Enter the heights of students:").split()
# for n in range(0,len(student_heights)):
#     student_heights[n] =int(student_heights[n])
# print(student_heights)

# total_height=0
# for height in student_heights:
#     total_height+=height

# total_students=0
# for number in student_heights:
#     total_students+=1

# average_height= round(total_height/total_students)
# print(average_height)

# student_scores= input("Enter the scores of students: ").split()
# for n in range(0,len(student_scores)):
#     student_scores[n]=int(student_scores[n])
# print(student_scores)
# highest_score=0
# for score in student_scores:
#     if score > highest_score:
#         highest_score=score
# print(f"The highest score is {highest_score}.")

# total=0
# for n in range(2,101,2):
#      total+=n
# print(total)

# total=0
# for n in range(1,101):
#     if n%3==0 and n%5==0:
#         print("FizzBuzz")
#     elif n%3==0:
#         print("Fizz")
#     elif n%5==0:
#         print("Buzz")
#     else:
#         print(n)

# import random

# letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# number=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]        
# symbol=['!','@','#','$','%','^','&','*','(',')']

# print("Welcome to the password generator.")
# n_letters=int(input("How many letters would you like for you password? "))
# n_numbers=int(input("How many numbers would you like?"))
# n_symbols=int(input("How many symbols would you like?"))
# password=""
# for n in range(1,n_letters+1):
#     password+=random.choice(letters)
# for n in range(1,n_numbers+1):
#     password+=random.choice(number)
# for n in range(1,n_symbols+1):
#     password+=random.choice(symbol)

# print(password)

# import random

# letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# number=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]        
# symbol=['!','@','#','$','%','^','&','*','(',')']

# print("Welcome to the password generator.")
# n_letters=int(input("How many letters would you like for you password? "))
# n_numbers=int(input("How many numbers would you like?"))
# n_symbols=int(input("How many symbols would you like?"))
# password=[]
# for n in range(1,n_letters+1):
#     password.append(random.choice(letters))
# for n in range(1,n_numbers+1):
#     password+=random.choice(number)
# for n in range(1,n_symbols+1):
#     password+=random.choice(symbol)
# random.shuffle(password)
# shuffled_password=""
# for char in password:
#     shuffled_password+=char
# print (shuffled_password)


# Day 6
# import random
# levels = ['''
# 	  +---+
# 	  |   |
# 	  O   |
# 	 /|\  |
# 	 / \  |
# 	      |
# 	=========''','''
# 	  +---+
# 	  |   |
# 	  O   |
# 	 /|\  |
# 	 /    |
# 	      |
# 	=========''','''
# 	  +---+
# 	  |   |
# 	  O   |
# 	 /|\  |
# 	      |
# 	      |
# 	=========''','''
# 	  +---+
# 	  |   |
# 	  O   |
# 	 /|   |
# 	      |
# 	      |
# 	=========''','''
# 	  +---+
# 	  |   |
# 	  O   |
# 	  |   |
# 	      |
# 	      |
# 	=========''','''
# 	  +---+
# 	  |   |
# 	  O   |
# 	      |
# 	      |
# 	      |
# 	=========''','''
# 	  +---+
# 	  |   |
# 	      |
# 	      |
# 	      |
# 	      |
# 	=========''']

# words=['mouse','keyboard','monitor','assassination']
# random_word=random.choice(words)
# guess=input("Guess the letter: ").lower()
# for letter in random_word:
#     if guess==letter:
#         print("Right")
#     else:
#         print("wrong")

# import random

# words=['mouse','keyboard','monitor','assassination']
# random_word=random.choice(words)
# lives=6
# end_of_game=False
# #testing
# print(f"The word is {random_word}.")
# blank=[]
# for n in random_word:
#     blank.append("_")
# print(blank)
# while not end_of_game:
# 	guess=input("Guess the letter: ").lower()
# 	for position in range(len(random_word)):
# 		letter=random_word[position]
# 		if letter==guess:
# 			blank[position]=letter
# 	print(blank)
# 	if guess not in random_word:
# 		lives-=1
# 	print(levels[lives])
# 	if lives==0:
# 			end_of_game=True
# 			print("you lose!!")
# 	if "_" not in blank:
# 		end_of_game =True
# if not lives==0:
# 	print("You won")   


# day 8

# def greet():
#     print("Hello!")
#     print("Good morning")
#     print("How are you?")

# greet()
    
# def greet(name, add):
#     print(f"My name is {name}.")
#     print(f"i live in {add}")
# greet(add="NPJ",name="Hari")

# import math
# def paint(height,width,cover):
#     num=math.ceil((height*width)/cover)
#     print(f"You need {num} cans.")
# wall_height=int(input("Enter the height of wall: "))
# wall_width=int(input("Enter the width of wall: "))
# coverage=5
# paint(height=wall_height,width=wall_width,cover=coverage)

# def prime_num_checker(x):
#     is_prime_number=True
#     for i in (2,x-1):
#         if x%i==0:
#             is_prime_number=False
#     if is_prime_number:
#         print(f"{x} is a prime number.")
#     else:
#         print(f"{x} is not a prime number.")

# num=int(input("Enter the number: "))
# prime_num_checker(x=num)


# def caesar(texts,shifts,directions):
#     cypher_text=""
#     if directions=="decode":
#         shifts*= -1
#     for let in texts:
#         position= alphabet.index(let)
#         new_position=position + shifts
#         new_let= alphabet[new_position]
#         cypher_text+=new_let
#     print(f"The {directions}d text is {cypher_text}")

                

# alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m',
# 'n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c',
# 'd','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# direction=input("Type 'encode' to encrypt or 'decode' to decrypt:" )
# text_in= input("Type your message: ").lower()
# shift_in=int(input("Type the shift number: "))

# caesar(texts=text_in,shifts=shift_in,directions=direction)


#day 9

# book={"Bug":"i don't care","loop":"i don't care got repeated","function":"I don't know but is useful"}
# print(book)
# # book["soup"]="unrelated topic"
# # book["Bug"]="not good tho"
# # print(book["function"])
# # print(book)
# # book={}
# # print(book)
# for thing in book:
#     print(thing)
#     print(book[thing])


# student_scores={
#     "Hari":99,
#     "Alex":85,
#     "Prith":66
# }
# student_grades={}
# for students in student_scores:
#     if student_scores[students]>90:
#         student_grades[students]="Outstanding"
#     elif student_scores[students]>80:
#         student_grades[students]="Exceeds expectations"
#     elif student_scores[students]>60:
#         student_grades[students]="Acceptable"


# print(student_grades)


#nesting dictionary in a list

# travel_log=[
#     {   
#     "country_visited":"USA",
#     "cities_visited":["New york","Washinton DC","New jersey"],
#     "state_visited":["SF","Florida"]
#     },
#     {
#     "country_visited":"Germany",
#     "cities_visited":["Berlin","Frankfurt"],
#     "total_visits":2
#     }
# ]
# print(travel_log)



# travel_log=[
#     {   
#     "country":"USA",
#     "cities":["New york","Washinton DC","New jersey"],
#     "total_visits":3
#     },
#     {
#     "country":"Germany",
#     "cities":["Berlin","Frankfurt"],
#     "total_visits":2
#     }
# ]


# def add_new_country(country_visited,cities_visited,times_visited):
#     new_country={}
#     new_country["country"]=country_visited
#     new_country["cities"]=cities_visited
#     new_country["total_visits"]=times_visited
#     travel_log.append(new_country)
# add_new_country("France",["Paris,Nice"],12)
# print(travel_log)


# import os
# add="yes"
# bids={}
# def winner_finder(biddings):
#     highest_bid=0
#     for persons in biddings:
#         if biddings[persons]>highest_bid:
#             highest_bid=biddings[persons]
#             winner=persons
#     print(f"The winner of the bidding is {winner} with a bid of {highest_bid}")

# while add=="yes":
#     name=input("Enter the name: ")
#     amount=int(input("What's your bid: "))
#     bids[name]=amount
#     add=input("Are there any other? Type 'yes' or 'no'. ")
#     os.system("cls")
# if add=="no":
#     winner_finder(bids)

# day 10

# def formatted_name(f_name,l_name):
#     first_name=f_name.title()
#     last_name=l_name.title()
#     return f"{first_name} {last_name}"
# print(formatted_name("DaMesHwor","MisHra"))
# output=len("dameshwor")
# print(output)

# def formatted_name(f_name,l_name):
#     if f_name=="" or l_name=="":
#         return "No input!"
#     first_name=f_name.title()
#     last_name=l_name.title()
#     return f"{first_name} {last_name}"

# print(formatted_name(input("Enter the first name: "),input("Enter the last name: ")))

# def is_leap_year(year):
#     if year%4!=0:
#         return False
#     else:
#         if year%100==0:
#             if year%400==0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
# def days_in_month(check_year,check_month):
#     month_days=[31,28,31,30,31,30,31,31,30,31,30,31]
#     asked_month_days=month_days[check_month-1]

#     if is_leap_year(year) and check_month==2:
#         return 29
#     else:
#         return asked_month_days
# year= int(input("Enter the year: "))
# month= int(input("Enter the month: "))
# days= days_in_month(year,month)
# print(days) 

#calculator

# def add(n1,n2):
#     return n1+n2
# def subb(n1,n2):
#     return n1-n2
# def mul(n1,n2):
#     return n1*n2
# def div(n1,n2):
#     return n1/n2

# calc={
# "+":add,
# "-":subb,
# "*":mul,
# "/":div
# }
# def calculator():
#     num1=float(input("Enter the first number: "))
#     to_continue=True
#     while to_continue:
#         for symbols in calc:
#             print(symbols)
#         operation=input("Select the operation to be performed: ")
#         num2=float(input("Enter the next number: "))
#         calculation_function=calc[operation]
#         answer=calculation_function(num1,num2)
#         print(f"{num1} {operation} {num2} = {answer}")
        
#         decision= input(f"Type 'y' to continue calculating with{answer} or type 'n' to exit. If you want to reset the calculation, type 'r' ")
#         if decision.lower()=='y':
#             num1=answer
#         elif decision.lower()=='r':
#             calculator()
#         else:
#             to_continue=False
# calculator()



# day 13
#4.fixing the error

# age= int(input("How old are you?"))
# if age>18:
#     print("You can drive")

#print is your friend
# pages=0
# words_per_page=0
# pages=int(input("Number of pages: "))
# words_per_page=int(input("Number of words per page: "))
# total_words=words_per_page*pages
# print(pages)
# print(words_per_page)
# print(total_words)


#use a debugger

# def mutate(a_list):
#     b_list=[]
#     for item in a_list:
#         new_item=item*2
#         b_list.append(new_item)
#         print(b_list)

# mutate([1,2,3,5,8,13])


