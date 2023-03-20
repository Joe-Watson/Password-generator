import random
letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
          "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbol = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "?"]
print("Welcome to the password Generator! ")
nr_latters = int(input("How many latters would you like in your password \n"))
nr_symbols = int(input("How many symbols would you like ?\n"))
nr_number = int(input("How many numbers would you like \n"))
password = ""
for char in range(1, nr_latters+1):
    password += random.choice(letter)
for num in range(1, nr_latters+1):
    password += random.choice(number)
for sym in range(1, nr_symbols+1):
    password += random.choice(symbol)
print(password)
