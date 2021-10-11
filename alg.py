import string
import random

string_pikkus = 20

suvakas_taht = "".join(random.choice(string.ascii_letters) for i in range(string_pikkus))
print(suvakas_taht)