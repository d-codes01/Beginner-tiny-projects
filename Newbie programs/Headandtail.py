import random
num_seed = int(input("Create a seed."))
random.seed(num_seed)
rand_num= random.randint(0,1)
if rand_num== 1:
    print("Heads")
else:
    print("Tails")