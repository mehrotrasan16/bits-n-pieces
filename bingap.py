bingap = 0
bingaps = []

num = raw_input("Enter number: ")
x = bin(int(num))

print "the binary representation of  " + num + "  is  " + x

l = 2
x = list(x)

while( l < len(x) - 1 ):
    if (x[l] == '1' and x[l+1] == '0'):
        #start counting zeroes till you reach a one
        bingap = 0
        j = l+1
        while(x[j] <> '1'):
            bingap += 1
            j += 1
        bingaps.append(bingap)        
    l += 1

print bingaps
print max(bingaps)


	
