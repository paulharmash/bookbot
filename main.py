from stats import count_words
from stats import number_of_characters
from stats import sorted_list
from stats import remove_nonalph
path = "books/frankenstein.txt"

def get_book_text(path):
    with open(path) as f:
        return f.read() # Returns the text as a string

    
def print_report(path, num_words, sorted_chars):
    print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

def main():
    text = get_book_text(path)
    num_words = count_words(text)
    char_dict = number_of_characters(text) 
    alpha_char = remove_nonalph(char_dict)
    sorted_chars = sorted_list(alpha_char)
    print_report(path, num_words, sorted_chars)

main()
