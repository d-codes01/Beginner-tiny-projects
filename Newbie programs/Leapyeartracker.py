
year = int(input("Enter the year: "))
if year%4!=0:
    print("Not a leap year.")
else:
    if year%100==0:
        if year%400==0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")