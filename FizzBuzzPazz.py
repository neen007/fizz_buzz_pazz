# -*- coding: utf-8 -*-

print "Dobrodošli u FizzBuzzPazz igru!"
print "Z A I G R A J M O  ! ! ! !"

while True:
    try:
        end = int(raw_input("Unesite jedan broj između 1 i 1000: "))

        for num in range(1, end+1):
            if num % 3 == 0 and num % 5 == 0 and num % 7 == 0:
                print "FizzBuzzPazz"
            elif num % 3 == 0:
                print "Fizz"
            elif num % 5 == 0:
                print "Buzz"
            elif num % 7 == 0:
                print "Pazz"
            else:
                print num
    except Exception as e:
            print "Molimo Vas unesite cjeli broj.Hvala!"

    choice = raw_input("Da li se želite ponovno igrati? (d/n): ")

    if choice.lower() != "d":
        break

