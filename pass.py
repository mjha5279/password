import random
import string
s=string.ascii_lowercase
s1=string.ascii_uppercase
s2=string.digits
s3=string.punctuation
s4=[]
s4.extend(s)
s4.extend(s1)
s4.extend(s2)
s4.extend(s3)
try:
    print("Enter length of password--")
    l=int(input())
    print("your password is--")
    print("".join(random.sample(s4,l)))
except Exception as Valueerror:
    print(" Warning:---  Enter integer")



