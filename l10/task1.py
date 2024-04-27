pets = dict()

animal_type = input("Введите вид животного: ")
animal_age = int(input("Введите возраст животного: "))
animal_name = input("Введите кличку животного: ")
animal_owner = input("Введите имя владельца: ")

pets[animal_name] = {
    "Вид питомца": animal_type,
    "Возраст питомца": animal_age,
    "Имя владельца": animal_owner
}

for pet_name in pets.keys():
    age = pets[pet_name]["Возраст питомца"]
    if age == 1:
        age_formatted = "год"
    elif age in range(2, 5):
        age_formatted = "года"
    elif 4 < age < 21:
        age_formatted = "лет"
    elif age % 10 == 1:
        age_formatted = "год"
    elif age % 10 in range(2, 5):
        age_formatted = "года"
    elif age % 10 in range(5, 10) or age % 10 == 0:
        age_formatted = "лет"
    print(f"Это {pets[pet_name]['Вид питомца']} по кличке \"{pet_name}\". Возраст питомца: {pets[pet_name]['Возраст питомца']} {age_formatted}. Имя владельца: {pets[pet_name]['Имя владельца']}")
