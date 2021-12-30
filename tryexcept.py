astr = input("Enter a number: ")
try:
    istr = int(astr)
except:
    istr = "can't convert into an integer"
print ("first:", istr)

astr = input("Enter a number: ")
try:
    istr = int(astr)
except:
    istr = "can't convert into integer"    
print ("second:", istr)
