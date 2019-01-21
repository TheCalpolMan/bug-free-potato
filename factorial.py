def factorial(reeeee):
    rhe = 2
    rhee = 1
    while rhe <= reeeee:
        rhee *= rhe
        rhe += 1
    return(rhee)

print(factorial(int(input("What do you want to be factorial'd?\n"))))
i = 0
while 6 < 8:
    i += 1
    os = 0
    it = 1
    while it <= len(str(factorial(i))):
        if str(factorial(i))[-it] == "0":
            os += 1
        else:
            break
        it += 1
    verycool = 1
    meant = 0
    while i // (5 ** verycool) != 0:
        meant += i // (5 ** verycool)
        verycool += 1
    print(str(meant) + " wow")
    if os == 1:
        print(str(factorial(i)) + " is " + str(i) + "! and has 1 0")
    else:
        print(str(factorial(i)) + " is " + str(i) + "! and has " + str(os) + " 0's")
    if os == meant:
        print("True " + str(meant))
    else:
        print("False " + str(meant))
        break
print("oh noes")
