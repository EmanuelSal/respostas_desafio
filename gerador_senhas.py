import random

lower = "abcdefghijlmnopqrstuvxwyzç"
upper = "ABCDEFGHIJLMNOPQRSTUVXWYZÇ"
digits = "0123456789"
symbols = "[]{}()*#;/,-_%."

qnt = 8
qntint = int(qnt)
length = qntint

all = lower + upper + digits + symbols
password = "".join(random.sample(all, length))
print("-" * 30)
print("Sua senha geral = " + password)
print()
MAXnum = upper + digits
password_MAXnum = "".join(random.sample(MAXnum, length))

print("Sua apenas com maiúsculas e nums = " + password_MAXnum)
print()
just_letters = upper + lower 
password_letters = "".join(random.sample(just_letters, length))

print("Sua senha apenas com letras = " + password_letters)
print()
digts = digits
password_digits = "".join(random.sample(digts, length))

print("Sua senha apenas com números = " + password_digits)
print("-" * 30)