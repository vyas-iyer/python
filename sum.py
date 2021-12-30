

sum = 0
count = 0

while True:
    num = input("enter a number and type done when you want to find the sum of them all: ")
    if num == "done":
        break
    try:
        float_num = float(num)
    except:
        print(num, "can't convert into a number");
        continue

    sum = sum + float_num
    count = count + 1
# end of loop

avg = sum/count
print ('Sum of all the inputs:', sum)
print ("the number of numbers you entered:", count)
print("avarage of the numbers you entered:", avg)
