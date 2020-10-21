def check_max(value, new_arr):
    i = 0
    while i < len(new_arr):
        if new_arr[i] > 0:
            if new_arr[i] >= value:
                new_arr.remove(value)
            elif new_arr[i] < value:
                value = value
        i += 1
    return value

def main():
    max_val, i = arr[0], 0
    while i < n:
        if max_val < arr[i]:
            max_val = arr[i]
        i += 1
    arr.remove(max_val)
    new_val = check_max(max_val, arr)
    for i in range(0, len(arr)):
        if max(arr) == new_val:
            arr.remove(new_val)
    print(max(arr))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    main()
