def main():
    if query_name == name:
        summation = 0
        for i in range(0, len(student_marks[name])):
            summation += student_marks[name][i]
        avg = summation / len(student_marks[name])
        print('{0:.2f}'.format(avg))
    else:
        summation = 0
        for i in range(0, len(student_marks[query_name])):
            summation += student_marks[query_name][i]
        avg = summation / len(student_marks[query_name])
        print('{0:.2f}'.format(avg))

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    main()