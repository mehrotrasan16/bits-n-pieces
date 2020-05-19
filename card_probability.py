import itertools

card_dict = {1:'A', 11:'J', 12:'Q', 13:'K'}
card_outcomes = [i for i in range(1,53)]

#suits can be calculated by
##>>> mod = [i%14 for i in deck]
##>>> mod
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sample_space = list(itertools.product(card_outcomes,repeat=2))
print(sample_space)

#favourable_outcomes = [sum(outcome) for outcome in sample_space if sum(outcome) <= 9]

#prob = len(favourable_outcomes)/len(sample_space)
#print(prob)

#fav2 = [(outcome) for outcome in sample_space if sum(outcome) == 6 and outcome[0] != outcome[1]]

#prob2 = len(fav2)/len(sample_space)

#print(f'probability that dice have different values and have a sum = 6 is: {prob2}')
