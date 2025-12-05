path = "books/frankenstein.txt"

def get_book_text(path):
    with open(path) as f:
        return f.read() # Returns the text as a string

def count_words(text): # A general fucntion that would work with any text
    return len(text.split()) # Returns the number of words

def main():
    text = get_book_text(path)
    num_words = count_words(text)
    print(f"Found {num_words} total words")

main()
