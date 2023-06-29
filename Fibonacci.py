# this code tells you what fibonachi number you want.

while True:
    previ = 0
    prev = 0
    total = 0
    fib = input('which fibonatchi number would you want: ')
    if fib == 'done':
        break
    try:
        ifib = int(fib)
    except ValueError:
        print ('needs to be a whole number for fibonacci')
        continue
    except:
        print ('something went wrong')
        continue

    if ifib <= 0:
        print('fibonacci number needs to be possitive')
        continue
        
    if ifib == 1:
        print (total)
        continue
        
    if ifib == 2:
        print (1)
        continue
        
    total = 1
        
    while ifib > 2:
        previ = total
        total = total + prev
        prev = previ
        ifib = ifib-1
        
    print('number: ', total)
        
        
# inf loop ends here
print ('bye bye!')
        
    
    
        
        
        
    
        
    
        
        
        
        
        
        
        
        
        


    