# importing the random modules
import random
Alpha = [];Numeric = []
for x in range(65,91):
    Alpha.append(chr(x))
for y in  range(48,58):
    Numeric.append(chr(y))
random.shuffle(Alpha); random.shuffle(Numeric)
Number = int(input("How many numbers do you want :------"))
for i in range(Number):
    print("Number is :",i+1)
    print("Vehicle number is : TN "+str("".join(random.choices(Numeric,k=2)))+" "+str("".join(random.choices(Alpha,k=2)))+" "+str("".join(random.choices(Numeric,k=4))))
