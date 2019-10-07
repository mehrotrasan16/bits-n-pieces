#returning the max and min mean from a list of numbers in python
#with list comprehension practice
#
def mean(list):
    mean = 0
    for i in list:
        mean +=i
    return mean/len(list)

j = [4,4,4,9,10,11,12]

p = 3

#[i for i in len(j)]
#[i for i in len(j)-2]
#[j[i:i+3] for i in range(len(j)-2)]
#[mean(j[i:i+3]) for i in range(len(j)-2)]

avgs = [mean(j[i:i+3]) for i in range(len(j)-2)]
max_avg,min_avg = [max(avgs)],[min(avgs)]

print(avgs)
print(max_avg)
print(min_avg)







