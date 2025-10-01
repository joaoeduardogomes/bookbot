from stats import get_book_text, count_characters
    
def main():
    text = get_book_text("./books/frankenstein.txt")
    chars = count_characters(text)
    print(chars)

main()