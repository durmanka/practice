def create_rating(students: list) -> list:
    n = len(students)

    for i in range(n):
        max_index = i

        for j in range(i + 1, n):
            if students[j][1] > students[max_index][1]:
                max_index = j

        students[i], students[max_index] = students[max_index], students[i]

    return students


students = [
    ("Олена", 91.5),
    ("Андрій", 87.0),
    ("Марія", 95.2),
    ("Іван", 89.8),
    ("Софія", 93.4)
]

rating = create_rating(students)

print("Рейтинг студентів:")
for i, (name, grade) in enumerate(rating, start=1):
    print(f"{i}. {name} - {grade}")