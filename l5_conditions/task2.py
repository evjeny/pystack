word = input("Введите слово: ")
vowels_count = (
    word.count("a") + 
    word.count("e") +
    word.count("i") +
    word.count("o") +
    word.count("u")
)
consonants_count = len(word) - vowels_count

print("Гласных:", vowels_count)
print("Согласных:", consonants_count)

for letter_i in range(ord("a"), ord("z") + 1):
    letter = chr(letter_i)
    if word.count(letter) > 0:
        print(f"{letter}: {word.count(letter)}")
    else:
        print(f"{letter}: False")
