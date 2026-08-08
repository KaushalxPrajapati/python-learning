def count_vowel(text):
    count = 0
    vowel_list = ["a", "e", "i", "o", "u"]

    for char in text.lower():
        if char in vowel_list:
            count += 1

    return count

result = count_vowel("Kaushal")
print(result)
