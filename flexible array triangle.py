# (C) Vyas 2021-

while True:
    num = input("enter the depth of the right angle triangle you desire and type done if you want to stop: ");
    if num == "done":
        break
    char = input("enter a character you want: ");


    try:
        int_num = int(num)
    except:
        print(num, "can't convert into a number")
        continue
    i = 1
    j = 1
    for i in range(int_num):
        for j in range(i+1):
            print(char, end = " ")
        print()
        i = i+1
