lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}


# Add your function below!
def average(number):
    total = sum(number)
    otal = float(total)
    average = total / float(len(number))
    return (average)


def get_average(student):
    homework = float(sum(student['homework'])) / float(len(student['homework']))
    quizzes = float(sum(student['quizzes'])) / float(len(student['quizzes']))
    tests = float(sum(student['tests'])) / float(len(student['tests']))
    summ = 0.1 * homework + quizzes * 0.3 + tests * 0.6
    return summ
print(get_average(alice))

