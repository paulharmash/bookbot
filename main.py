import sys
from stats import count_words
from stats import number_of_characters
from stats import sorted_list
from stats import remove_nonalph

# Function to get text input
def text_input():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        return sys.argv[1]

# Function to convert a text in a string
def get_book_text(path):
    with open(path) as f:
        return f.read() 

# Function to print results in the console    
def print_report(path, num_words, sorted_chars):
    print(f"============ BOOKBOT ============\nAnalyzing book found at {path}...\n----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

def main():
    path = text_input()
    text = get_book_text(path)
    num_words = count_words(text)
    char_dict = number_of_characters(text) 
    alpha_char = remove_nonalph(char_dict)
    sorted_chars = sorted_list(alpha_char)
    print_report(path, num_words, sorted_chars)

main()
