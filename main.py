import sys
from stats import get_book_text, count_words, count_characters, ordered_stats


def main(filepath):
    try: 
        text = get_book_text(filepath)
        words = count_words(text)
        chars = count_characters(text)
        ordered = ordered_stats(chars)

        print(f"""
============ BOOKBOT ============
Analyzing book found at {filepath}...
----------- Word Count ----------
Found {words} total words
--------- Character Count -------
        """)

        for item in ordered:
            if item[0].isalpha():
                print(f"{item[0]}: {item[1]}")

        print("============= END ===============")
    except FileNotFoundError:
        print("File not found. Please check the filepath.")
        sys.exit(1)


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main(sys.argv[1])