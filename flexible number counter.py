
def is_prime(num):
    if (num == 1):
        return False

    for i in range (2, int(num/2)+1):
        if (num % i == 0) :
            return False
    return True

#Askes the user to enter a number and that will be put in the "start" variable
start = int(input("Please enter from What number to start with:  "))
#Askes to enter a number > than start variable and that # will be put in the "end" variable
end = int(input("Please enter What number to end with: "))
#Askes the user to type 0 to write all even # from start to end 1 for all the odd # between them and 2 to write all the # between them :)
user_input = int(input("Please enter 0 for even, 1 for odd, 2 for all, 3 for all primes : "))

# when entering the for loop with a range of start to end the # it is currently at will be stored in "i" and when coming back, will start with i+1
for i in range(start, end+1):
#if the user types 2 at the user_input variable question, then print all numbers from "start"to "end"
    if (user_input == 2):
        print (i, end = ' ')
#if user input is not 2 then move on to this line. an even # divided by 2 will end with a remainder of 0 but for an odd # then the remainder would be 1 so for user_input variable if it is 0, then it will write all #'s from start to end but if it is 1 then it will list all the odd #
    elif (i % 2 == user_input):
        print (i, end = ' ')

    elif (user_input == 3):
        if (is_prime(i)):
            print (i, end = ' ')
