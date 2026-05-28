def create_rating(students):
    result = students.copy()
    n = len(result)

    for i in range(n):
        max_index = i

        for j in range(i + 1, n):
            if result[j][1] > result[max_index][1]:
                max_index = j

        result[i], result[max_index] = result[max_index], result[i]

    return result

students = [
    ("Олег",    7.4),
    ("Марія",   9.1),
    ("Іван",    8.3),
    ("Софія",   9.1),
    ("Дмитро",  6.8),
    ("Анна",    8.7),
]

print("До сортування:")
for name, grade in students:
    print(f"  {name}: {grade}")

rating = create_rating(students)

print("\nРейтинг (від найвищого до найнижчого):")
for place, (name, grade) in enumerate(rating, start=1):
    print(f"  {place}. {name}: {grade}")