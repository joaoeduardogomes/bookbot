def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    chars = {}

    for char in text:
        key = char.lower()
        chars[key] = chars.get(key, 0) + 1 

    return chars

def ordered_stats(chars_dict):
    chars_list = []

    for pair in chars_dict.items():
        chars_list.append(pair)

    chars_list.sort()
    return chars_list