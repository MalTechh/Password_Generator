from math import ceil
import random
num_chars = int(input("How many charecters would you like your password to be?: "))
up = num_chars//4
low = ceil(num_chars/4)
symb = num_chars//4
num = ceil(num_chars/4)
upper_chars = []
lower_chars = []
symbs = []
nums = []
passlist = []
while len(upper_chars)<up:
    upper_chars.append(chr(random.randint(65,90)))
while len(lower_chars)<low:
    lower_chars.append(chr(random.randint(97,122)))
while len(symbs)<symb:
    symbs.append(chr(random.randint(33,38)))
while len(nums)<num:
    nums.append(random.randint(1,9))
passlist = upper_chars + lower_chars + symbs + nums
stringpass = ""
while len(passlist)>0:
    index = random.randint(0,len(passlist)-1)
    stringpass += str(passlist[index])
    del passlist[index]
print(stringpass)
passuse = input("What site will this password be used on?: ")
passfile = open("Password list", "a")
passfile.write(passuse + " password: " + "\n" + stringpass + "\n")
passfile.close()
