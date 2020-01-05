array = [4 ,4, 4, 99, 9, 9, 10, 11, 12]

window = 3

window_arr = [array[i:i+3] for i in range(len(array) - 2)]
print(window_arr)
