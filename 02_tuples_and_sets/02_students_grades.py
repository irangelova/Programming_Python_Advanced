number_of_students = int(input())
students_info = {}

for _ in range(number_of_students):
    name, grade = input().split()
    if name not in students_info.keys():
        students_info[name] = []
    students_info[name].append(float(grade))

for key, value in students_info.items():
    formatted_grades = [str(f"{grade:.2f}") for grade in value]
    average_grade = sum(value) / len(value)
    print(f"{key} -> {' '.join(formatted_grades)} (avg: {average_grade:.2f})")
