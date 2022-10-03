#dn = depreciation in a given year (d)
#IC = Initial Cost (i)
#s = salvage cost (s)
#tc = Tire cost (t)
#n = number of years (n)

print('Input the initial cost')
i = input()

print('Input the salvage cost')
s = input()

print('Input the tire cost')
t = input()

print('Input the Useful life')
n = input()

#Straight Line Depreciation
def strghtlinedep():
    d = ((float(i)-float(s)-float(t))/float(n))
    return d   
print('The depreciation by straight line method is {}'.format(strghtlinedep()))

#Sum of years digits depreciation
#Year n digit is the reverse order: n if solving for D1 or 1 if 
#solving for Dn
def sumofyrdep():

    d = ((float(n)/((float(n)*(float(n)+1)/2)))*(float(i)-float(s)-float(t)))
    return d
print('The depreciation by sum of years` digits method is {}'.format(sumofyrdep()))

def ddbdep():
    b = float(i)-float(t)
    d1 = (2/float(n))*(float(b))
    b = float(b) - float(d1)
    if float(d1) >= float(s):
        return d1
    else:
        pass

print('The depreciation by double declining balance method at the end of the first year is {}' .format(ddbdep()))

    
        
    