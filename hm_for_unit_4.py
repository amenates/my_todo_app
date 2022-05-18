def count_letter(words, letter):
    for word in words:
        print(word)
        if letter in word:
            print(letter)
            test = test + 1


city = ['Казань', 'Москва', 'Воронеж']
count_letter(city, 'а')