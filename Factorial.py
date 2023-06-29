# This program calculates the factorial of any whole number

while True:

    factstore = 1
    factorial = input('what factorial would you want to calculate(type done to exit): ')
    
    if factorial == 'done':
        break
    
    try:
        ifactorial = int(factorial)
    except ValueError: 
        print('number needs to be an integer')
        continue
    except:
        print('something else went wrong')
        continue
    
    if ifactorial < 0:
        print('number needs to be a whole number')
        continue
    while ifactorial > 0:
        factstore = ifactorial * factstore
        ifactorial = ifactorial - 1 
        
    print('the factorial is: ', factstore)

#inf loop ends here
print ('bye bye!')
        
    
    
    