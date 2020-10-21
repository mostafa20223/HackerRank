def main():
    my_list = [['Mostafa', 21.0], ['Hadeer', 24.0], ['Hanaa', 53.0], ['Yehia', 60.0], ['Ahmed', 30.0]]
    values = []
    min_val = []
    minimum = []
    for i in range(0, len(my_list)):
        values.append(max(my_list[i:i+1])[1])
    print(values)
    i = 0
    while i < len(values):
        minimum.append(min(values))
        values.remove(minimum[i])
        i += 1
    print(minimum)
    min_val.append(minimum[0:2])
    print(min_val)
    print(my_list.index(['Hadeer', 24.0]))

if __name__ == '__main__':
    # my_list = []
    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())
    #     my_list.append([name, score])
    main()
