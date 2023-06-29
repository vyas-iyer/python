while True:
    
    total = 0
    x = input('what numbers do you want for doing addition using the gause method: ')
    if x=="done":
        break
    try:
        y=int(x)
    except ValueError:
        print('number needs to be an integer')
        continue
    except:
        print("Something else went wrong")
        continue


    if y<0:
        print('number needs to be a non-negative integer')
        continue
    while y>0:
        total = total + y
        y = y-1
    print('sum:', total)
#inf loop ends here
print('bye bye!')