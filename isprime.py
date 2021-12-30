
#Receives num
#Returns True if the num is prime; Returns False otherwise
def is_prime(num):
    for i in range (2, int(num/2)):
        if (num % i == 0) :
            print ('first multiple', end = ' ')
            print (i)
            return False
    return True



#Invoking the function
num = int(input('Enter number:'))
if (is_prime(num)) :
    print ('yes')
else:
    print ('no')
