import random

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]        
symbol=['!','@','#','$','%','^','&','*','(',')']

print("Welcome to the password generator.")
n_letters=int(input("How many letters would you like for you password? "))
n_numbers=int(input("How many numbers would you like?"))
n_symbols=int(input("How many symbols would you like?"))
password=[]
for n in range(1,n_letters+1):
    password.append(random.choice(letters))
for n in range(1,n_numbers+1):
    password+=random.choice(number)
for n in range(1,n_symbols+1):
    password+=random.choice(symbol)
random.shuffle(password)
shuffled_password=""
for char in password:
    shuffled_password+=char
print(shuffled_password)
