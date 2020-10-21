def main():
    my_list = []
    for i in range(1, n + 1):
        my_list.append(i)
    for i in range(0, len(my_list)):
        print(str(my_list[i]), end = '')

if __name__ == '__main__':
    n = int(input())
    main()