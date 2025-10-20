def get_word_count(content) -> int:
   return len(content.split())

def get_char_count(content) -> dict:
    char_dict = {}
    words = content.split()
#Need to check if it is a letter than change to lowercase.
    for word in words:
        for letter in word:
            if letter.lower() in char_dict:
                char_dict[letter.lower()] += 1
            else:
                char_dict[letter.lower()] = 1
    return char_dict

def sort_on(d):
    return d["num"]

def get_sorted_char_dict(char_dict) -> list[dict]:
    result = []
    for key, value in char_dict.items():
        entry = {"name": str(key), "num": int(value)}
        result.append(entry)
    result.sort(reverse=True, key=sort_on)
    return result