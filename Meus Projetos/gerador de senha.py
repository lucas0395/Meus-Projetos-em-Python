import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
symbols = "[]{}()*#;/,-_%$&!?"
qnt = 8
qntInt = int(qnt)
length = qntInt
all = lower + upper + digits + symbols
passwordAll = "".join(random.sample(all, length))
print("passwordAll= " + passwordAll)
