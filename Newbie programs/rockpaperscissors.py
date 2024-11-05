import random
rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper='''
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice= int(input("Choose 0 for rocks, 1 for paper and 2 for scissors. "))
print("You chose:")
if choice==0:
    print(rock)
elif choice==1:
    print(paper)
else:
    print(scissors)
comp_choice= random.randint(0,2)
print("Computer chose:")
if comp_choice==0:
    print(rock)
elif comp_choice==1:
    print(paper)
else:
    print(scissors)
if choice==comp_choice:
    print("Draw!")
elif (choice ==0 and comp_choice==1) or (choice==1 and comp_choice==2) or (choice==2 and comp_choice==0):
    print("You lose!!")
elif (choice ==1 and comp_choice==0) or (choice==2 and comp_choice==1) or (choice==0 and comp_choice==2):
    print("You win!!!")
else:
    print("Invalid character. You lose")
    