#Problem Statement: Efficiently read a 1D list into a 2D matrix
#https://stackoverflow.com/questions/3636344/read-flat-list-into-multidimensional-array-matrix-in-python

list = [1,1,1,1,1,1,2,2,2,3,1,1,2,3,3,1,2,1,3,1]

def tomatrix(flat,rows):
    return [flat[i:i+rows] for i in range(0,len(flat),rows)]

twod = tomatrix(list,5)
for i in twod:
    print(i)    
