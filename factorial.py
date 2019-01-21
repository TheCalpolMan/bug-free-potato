def factorial(reeeee):
    rhe = 2
    rhee = 1
    while rhe <= reeeee:
        rhee *= rhe
        rhe += 1
    return(rhee)

print(factorial(int(input("What do you want to be factorial'd?\n"))))

for i in range(100):
    os = 0
    it = 1
    while it <= len(str(factorial(i))):
        if str(factorial(i))[-it] == "0":
            os += 1
        else:
            break
        it += 1
    if os == 1:
        print(str(factorial(i)) + " is " + str(i) + "! and has 1 0")
    else:
        print(str(factorial(i)) + " is " + str(i) + "! and has " + str(os) + " 0's")
    if os == (i // 5 + i // 25):
        print("True " + str(i // 5 + i // 25))
    else:
        print("False " + str(i // 5 + i // 25))