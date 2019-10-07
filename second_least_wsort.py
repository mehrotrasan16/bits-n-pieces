if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    min = arr[0]
    second_min = arr[0]
    for _ in range(len(arr):
        if arr[_] < min:
            second_min = arr[_]
    
    print(second_min)


