number = int(input("Bir eded daxil edin: "))
count = 0
while number > 1:
    if number % 2 == 0:
        number //= 2
    else:
        number = number * 3 + 1
    count += 1
    print(number)
    print ("---")
print (f"{count} addima 1 e catdi")
