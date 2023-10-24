def main():
    total_students = int(input('Total number of students: '))
    student_scores = list(map(int, input(f'Enter {total_students} score(s) ').split()))
    #student_scores_valid = [int(x) for x in student_scores ]
    #print(student_scores_valid)
    best_score = max(student_scores)
    #print(best_score)
    for i, score in enumerate(student_scores):
        student_grade = 'F'
        if score >= best_score - 10:
            student_grade = 'A'
        elif score >= best_score - 20:
            student_grade = 'B'
        elif score >= best_score - 30:
            student_grade = 'C'
        elif score >= best_score - 40:
            student_grade = 'D'
        else:
            student_grade = 'F'
        print('Student {} score is {} and grade is {}'.format(i+1, score, student_grade))

if __name__ == '__main__':
    main()
