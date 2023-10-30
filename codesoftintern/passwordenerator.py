import random
print("PASSWORD GENERATOR")
uppercase_letters =['A','B','C','D','E','F','G','H','I','J','K','L','M',
          'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lowercase_letters=['a','b','c','d','e','f','g','h','i','j','k','l','m',
          'n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','_','-','+','/','?']

u_letters =int(input("How many UPPER CASE letters you want ?\n"))
l_letters =int(input("How many LOWER CASE letters you want ?\n"))
num =int(input("How many NUMBERS you want ?\n"))
sym =int(input("How many SYMBOLS you want ?\n"))

password=[]
for a in range(1,u_letters+1):
    characters = random.choice(uppercase_letters)
    password +=characters
for a in range(1,l_letters+1):
    characters = random.choice(lowercase_letters)
    password +=characters
for a in range(1,num+1):
    characters = random.choice(numbers)
    password+=characters
for a in range(1,sym+1):
    characters = random.choice(symbols)
    password+=characters

random.shuffle(password)
result=""
for characters in password:
    result += characters
print(result)

