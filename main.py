import sys
from stats import (
    get_word_count,
    get_char_count,
    get_sorted_char_dict
)

def get_book_text(filepath) -> str:
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        text_file_path = sys.argv[1]

    print("============ BOOKBOT ============")
    text_str = get_book_text(text_file_path)

    print("Analyzing book found at books/frankenstein.txt...")
    num_words = get_word_count(text_str)

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    unsorted_dict = get_char_count(text_str)
    print("--------- Character Count -------")
    sorted_list_of_dict = get_sorted_char_dict(unsorted_dict)
    for entry_dict in sorted_list_of_dict:
        if entry_dict["name"].isalpha():
            name, num = entry_dict["name"], entry_dict["num"]
            print(f"{name}: {num}")
    print("============= END ===============")

main()
