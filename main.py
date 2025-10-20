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
    print("============ BOOKBOT ============")
    text_str = get_book_text("books/frankenstein.txt")

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
