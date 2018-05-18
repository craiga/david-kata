list = [1, 2, 3, 4, 5]
word = "lol"
number = 1000
number2 = 5
a = 10

#should return 5
print(len(list))
#should return 6
print(len(list)+1)

#length is 3. Therefore print 'else'
if len(word) > 4:
    print("That's a big word")
else:
    print("That's a small word")

if number > 90:
    print("That's a big number")
else:
    print("That's a small number")

if number2 > 90:
    print("That's a big number")
else:
    print("That's a small number")

if a % 2 == 0:
    print("It's even")
else:
    print("Nope, it's odd")

# This is stackoverflow advise for finding out if is even.
# So, if it's divisble by 2 and returning 0?
if number2 % 2 == 0:
    print("It's even zz")
else:
    print("Nope, it's odd")
