#Problem Statement: Calculate the interquartile range for a dataset given the length of an array, its members and their frequencies
#Have to generate the dataset from each item and its freq

n = int(input())
array = [int(i) for i in input().split()]
freq = [int(i) for i in input().split()]
dataset = []
for i in range(n):
    dataset.append([array[i]]*freq[i])
dataset = [item for sublist in dataset for item in sublist]
dataset = sorted(dataset)
medarr = (dataset[n//2] + dataset[-(n//2+1)])/2
n = len(dataset)
mid = 0
if(n%2 == 0):
    mid = n//2
else:
    mid = n//2+1

upperhalf = dataset[mid:]
if(n%2 == 0):
    lowerhalf = dataset[:mid]
else:
    lowerhalf = dataset[:mid-1]

Q3 = (upperhalf[len(upperhalf) // 2] + upperhalf[-(len(upperhalf)//2 + 1)]) / 2
Q1 = (lowerhalf[len(lowerhalf)// 2] + lowerhalf[-(len(lowerhalf)//2 + 1)]) / 2

#print(lowerhalf, upperhalf)
#print(Q1,Q3)
print(Q3-Q1)
