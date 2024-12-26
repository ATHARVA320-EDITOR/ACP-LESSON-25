import random
number1 = random.randint(1,9)
print("1st number of the password is: ",number1)
upper = "ABCDFGHIJLMNOPQRSTUVWXYZ"
upperletter = random.choice(upper)
print ("Upper case letter of the password is: ",upperletter)
special1 = "!@#$%^&*"
special1character = random.choice(special1)    
print("1st special symbol of the password is: ",special1character)
lower = "abcdefghijklmnopqrstuvwxyz"
lowerletter = random.choice(lower)
print ("Lower case letter of the password is: ",lowerletter)
number2 = random.randint(1,9)
print ("2nd number of the password is: ",number2)
number3 =   random.randint(1,9)
print("3rd number of the password is: ",number3)
special2 = "!@#$%^&*"
special2character = random.choice(special2)    
print("2nd special symbol of the password is: ",special2character)
password = print(number1,upperletter,special1character,lowerletter,number2,number3,special2character)