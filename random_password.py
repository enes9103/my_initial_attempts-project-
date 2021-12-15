import random
import string 
lower = string.ascii_lowercase
upper = string.ascii_uppercase
punctu = string.punctuation

l = [random.choice(lower) + random.choice(upper) + random.choice(punctu) for i in range(3)]
passw = list("".join(l))
random.shuffle(passw)
new_password = "".join(passw)
print(new_password)