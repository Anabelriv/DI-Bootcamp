user = int(input("Enter a number: "))
sum1 = 0
for i in range(1,user):
    if (user % 1 == 0):
        sum1 = sum1 + i
if (sum1 == user):
    print("The number is a Perfect Number!")
else:
    print("The number is not a Perfect Number!")
