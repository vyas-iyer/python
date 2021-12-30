
while (True) :
    op1 = int(input("please tell the first number : "))
    if (op1 == 666) :
        break

    op2 = int(input("please tell the last number:" ))
    oporation = int(input ("please put 1 for multipication, 2 for divition, 3 for addition, and 4 for subtraction:"  ))
    result = 0

    if (oporation == 1):
        result = (op1*op2)
        opr="*"
    elif (oporation==2):
        if (op2 == 0):
            print ("oh noooo u divided by 0! you just tore the fabric of space and time >:(")
            continue
        result =(op1/op2)
        opr="/"
    elif (oporation==3):
        result =(op1 + op2)
        opr="+"
    elif (oporation==4):
        result =(op1-op2)
        opr="-"

    print (f"{op1} {opr} {op2} = {result}")
    print()
