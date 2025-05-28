import csv
header = ["Name","Subject","Grade"]
data = [["Alice","Math",85], ["Bob","Science",78], ["Carol","Math",92], ["Dave","History",74]]
with open('grades.csv', 'w', newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)


with open('grades.csv', 'rt') as file:
    reader = csv.DictReader(file)
    rows = (list(reader))
    subject_grades = {}
    for row in rows:
        subject = row["Subject"]
        grade = int(row["Grade"])
        if subject not in subject_grades:
            subject_grades[subject] = []
        subject_grades[subject].append(grade)

with open('average_grades.csv', 'w', newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(["Subject", "Average Grade"])

    for subject, grades in subject_grades.items():
        avg = sum(grades)/len(grades)
        writer.writerow([subject, round(avg,1)])