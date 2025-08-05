from stats import get_word_count
from stats import get_letter_count
from stats import get_sorted_dict

def get_book_text(filepath):
    """
    It takes a filepath as input and returns the contents of the file as a string.
    """
    with open(filepath) as f:
        file_contents= f.read()
    return file_contents

def main():
    book_path =  "books/frankenstein.txt"
    num_words = get_word_count(get_book_text(book_path))
    letter_count = get_letter_count(get_book_text(book_path))
    letter_sort = get_sorted_dict(letter_count)

    print(f"""============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------""")
    for char_count_pair in letter_sort:
        if char_count_pair["char"].isalpha():
            print(f"{char_count_pair["char"]}: {char_count_pair["num"]}")
    print("============= END ===============")


main()