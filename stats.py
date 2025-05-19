def get_num_words(book_text):
    return len(book_text.split())

def get_chars_dict(book_text):
    chars = {}
    for char in book_text:
        chars[char.lower()] = chars.get(char.lower(), 0) + 1
    return chars

def sort_on(dict):
    return dict["num"]

def sort_chars_dict(char_dict):
    sorted_list = []
    for char, num in char_dict.items():
        sorted_list.append({"char": char, "num": num})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

    