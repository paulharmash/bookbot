def get_book_text(path):
    with open(path) as f:
        return f.read() # Returns the text as a string

#def count_words():
#    num_words = get_book_text().split()

def main():
    print(get_book_text("books/frankenstein.txt"))
    

main()
