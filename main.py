from stats import count_words
from stats import number_of_characters
path = "books/frankenstein.txt"

def get_book_text(path):
    with open(path) as f:
        return f.read() # Returns the text as a string

def main():
    text = get_book_text(path)
    num_words = count_words(text)
    dictionary_of_symbols = number_of_characters(text) 
    print(f"Found {num_words} total words")
    print(dictionary_of_symbols)

main()
