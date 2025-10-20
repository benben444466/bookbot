from stats import *

def get_book_text(filepath) -> str:
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    text_str = get_book_text("books/frankenstein.txt")
    num_words = get_word_count(text_str)
    print(f"Found {num_words} total words")
    print(get_char_count(text_str))    

if __name__ == "__main__":
    main()
