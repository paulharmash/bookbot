def count_words(text): # A general function that would work with any text
    return len(text.split()) # Returns the number of words

def number_of_characters(text):
    dictionary = {} # Dictionary for the result of number_of_characters()
    lowercase_text = text.lower() # Making the text all lowercase
    for character in lowercase_text:
        if character not in dictionary:
            dictionary[character] = 0 # Adding keys if they don't exist
        dictionary[character] += 1 # Adding values
    return dictionary