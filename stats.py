def get_word_count(book):
    num_words = book.split()
    return len(num_words)

def get_letter_count(book):
    count_letters = {}
    for letter in book:
        if letter.lower() in count_letters:
            count_letters[letter.lower()] += 1
        else:
            count_letters[letter.lower()] = 1
    return count_letters

def sort_on(items):
    return items["num"]

def get_sorted_dict(count_letters):
    letter_sort = []
    for letter in count_letters:
        letter_sort.append({"char": letter,"num": count_letters[letter]})
    letter_sort.sort(reverse=True, key=sort_on)
    return letter_sort