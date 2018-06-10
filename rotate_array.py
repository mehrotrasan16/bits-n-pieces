
x = raw_input("Enter comma separated list of numbers:\n").split(',')
print x
#x = [int(n) for n in x] # one way of doing it
x = map(int,(i for i in x)) #better way of doing it.
print x

y = int(raw_input("enter number of rotations(right):"))
print y

#r = [None] * len(x)
r = list()
print r

for i in range(0,len(x)):
    print i, i+y,(len(x)-1),((i+y)-(len(x)-1))
    if (i+y) > len(x)-1:
        print "in case"
        r.insert((i+y)-len(x),x[i])
    #    r[-y] = x[i]
    else:
        r.insert(i+y,x[i])
    #    r[i+y] = x[i]

print r


    

