import random

print("0. Порівняння функцій модуля random")

print("\nrandom.random() повертає дробове число з проміжку [0, 1).")
print("0 може випасти, а 1 — ні.")
print("Результат:", random.random())

print("\nrandom.randint(1, 10) повертає ціле число від 1 до 10 включно.")
print("Результат:", random.randint(1, 10))

print("\nrandom.choice() повертає один випадковий елемент зі списку.")
print("Результат:", random.choice(["яблуко", "груша", "слива"]))

students = [
    "Акберова Шафіга",
    "Бабич Софія",
    "Вагіна Аліна",
    "Дмитрієва Анна",
    "Едокова Софія",
    "Іщенко Карина",
    "Клименко Наталія",
    "Крамаренко Ганна",
    "Карпова Христина",
    "Коржикова Софія",
    "Кучін Ілля",
    "Лісовець Дарина",
    "Леонова Поліна",
    "Міняйлик Аліна",
    "Наталуша Тетяна",
    "Немчинська Анастасія",
    "Поліщук Єлизавета",
    "Роменський Микита",
    "Ткачук Поліна",
    "Фесюк Вікторія",
    "Хмельницька Олександра",
    "Хміль Катерина",
    "Чомахашвілі Евеліна",
    "Щукіна Огнеяра",
]

print("\n1. Випадковий вибір студента")
for draw in range(1, 6):
    student = random.choice(students)
    print(f"Вибір {draw}: {student}")

print("\n2. Випадковий вибір трьох студентів")

selected_students = random.sample(students, 3)

for number, student in enumerate(selected_students, start=1):
    print(f"{number}. {student}")

def toss_coin():
    return random.choice(["орел", "решка"])


def count_tosses(number_of_tosses):
    counts = {"орел": 0, "решка": 0}

    for _ in range(number_of_tosses):
        result = toss_coin()
        counts[result] += 1

    return counts


print("\n3. Гра з монеткою")
print(f"Результат одного підкидання: {toss_coin()}")

for number_of_tosses in (100, 1000):
    counts = count_tosses(number_of_tosses)
    print(f"{number_of_tosses} підкидань:")
    print(f"  Орел: {counts['орел']}")
    print(f"  Решка: {counts['решка']}")

print("\n4*. Гра «Хто викине більше?»")
print("Ти й комп’ютер кидаєте по одному кубику. Більше число виграє.")

player_roll = random.randint(1, 6)
computer_roll = random.randint(1, 6)

print(f"Твій результат: {player_roll}")
print(f"Результат комп’ютера: {computer_roll}")

if player_roll > computer_roll:
    print("Ти перемогла!")
elif player_roll < computer_roll:
    print("Комп’ютер переміг!")
else:
    print("Нічия!")