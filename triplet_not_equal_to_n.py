#You are given three integers  and  representing the dimensions of a cuboid along with an integer . You have to print a list of all possible coordinates given by  on a 3D grid where the sum of is not equal to the integer. 

Input Format

Four integers  and  each on four separate lines, respectively.

Constraints

Print the list in lexicographic increasing order.
#
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    #ans = list(map(lambda x,y,z: x,y,z in range(x,y,z) and x+y+z != n ))
     ans = [ [x1,y1,z1] for x1 in range(x+1) for y1 in range(y+1) for z1 in range(z+1) if x1+y1+z1 != n]
	print(ans)
    #ans = [i for i in range(x),j for j in range(y),k for k in range(z)]
    #anslist = [i,j,k] for i in range(x) for j in range(y) for k in range(z) if (x+y+z != n)
    anslist = []
    # for i in range(x+1):
        # for j in range(y+1):
            # for k in range(z+1):
                # if i+j+k != n:
                    # #print(i +','+ j+',' + k)
                    # anslist.append([i,j,k])
    
    # print(anslist)




