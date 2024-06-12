import secrets
import string

n =int(input("Enter the number of password you want to create: "))
alphabet = string.ascii_letters + string.digits + string.punctuation
password = ''.join(secrets.choice(alphabet) for i in range(n))
# print(alphabet)
print("Your password is: "+password)