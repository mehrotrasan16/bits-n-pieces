import itertools

dice_outcomes = [1,2,3,4,5,6]
sample_space = list(itertools.product(dice_outcomes,repeat=2))
print(sample_space)

favourable_outcomes = [sum(outcome) for outcome in sample_space if sum(outcome) <= 9]

prob = len(favourable_outcomes)/len(sample_space)
print(prob)

fav2 = [(outcome) for outcome in sample_space if sum(outcome) == 6 and outcome[0] != outcome[1]]

prob2 = len(fav2)/len(sample_space)

print(f'probability that dice have different values and have a sum = 6 is: {prob2}')


