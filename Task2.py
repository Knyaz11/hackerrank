def grading_students(grades):
    result = []
    for grade in grades:
        if grade < 38:
            result.append(grade)
        else:
            next_multiple = ((grade + 4) // 5) * 5
            if next_multiple - grade < 3:
                result.append(next_multiple)
            else:
                result.append(grade)
    return result


if __name__ == '__main__':
    n = int(input().strip())
    grades = []

    for _ in range(n):
        grades.append(int(input().strip()))

    result = grading_students(grades)

    for g in result:
        print(g)
