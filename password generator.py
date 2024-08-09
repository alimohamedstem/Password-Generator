import random
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
symbols = "!@#$%^&*()_-+=}{';?>.,<"
numbers = "0123456789"


password = upper + lower + symbols + numbers
length = int(input('The length of the password\n'))
## Note: the password length not more than 86

password2 = "".join(random.sample(password,length))

print("The generated password is " + password2)