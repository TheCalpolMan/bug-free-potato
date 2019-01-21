def factorial(reeeee):
    rhe = 2
    rhee = 1
    while rhe <= reeeee:
        rhee *= rhe
        rhe += 1
    return rhee

def ocounter(number):
    onum = 0
    it = 1
    while it <= len(str(number)):
        if str(number)[-it] == "0":
            onum += 1
        else:
            return onum
        it += 1

defactor = int(input("Enter the number that you want to de-factor\n"))
num = 1
number = 1
bad = False
onum = ocounter(defactor)
it = 1
while defactor / number != 1:
    num += 1
    number = factorial(num)
    if num > 10 and "00" not in str(factorial(num)):
        bad = True
        break
if bad == True:
    print("Not a factorial")
else:
    print(str(defactor) + " defactorial'd is " + str(num))
