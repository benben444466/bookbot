def get_word_count(content) -> int:
   return len(content.split())

def get_char_count(content) -> dict:
    char_dict = {}
    words = content.split()
#Need to check if it is a letter than change to lowercase.
    for word in words:
        for letter in word:
            #print(letter + "0")
            if letter.lower() in char_dict:
                char_dict[letter.lower()] += 1
            else:
                char_dict[letter.lower()] = 1
    return char_dict