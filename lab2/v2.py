def main():
    student_count = int(input('Total number of students: '))
    student_score = list(map(int, input(f'Enter {student_count} score(s): ').split()))

    highest_score = max(student_score)

    i = 0
    student_num = 1
    while i < student_count:
        student_grade = None
        if student_score[i] >= highest_score - 10:
            student_grade = 'A'
        elif student_score[i] >= highest_score - 20:
            student_grade = 'B'
        elif student_score[i] >= highest_score - 30:
            student_grade = 'C'
        elif student_score[i] >= highest_score - 40:
            student_grade = 'D'
        else:
            student_grade = 'F'

        print(f'Student {student_num} score is {student_score[i]} and grade is {student_grade}')
        student_num +=1
        i += 1

if __name__ == '__main__':
    main()
