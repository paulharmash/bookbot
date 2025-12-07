# Function to calculate words in a text
def count_words(text): 
    return len(text.split())

# Function to calcualte the number of characters in a text
def number_of_characters(text):
    dictionary = {} # Dictionary for the result of number_of_characters()
    lowercase_text = text.lower() # Making the text all lowercase
    for character in lowercase_text:
        if character not in dictionary:
            dictionary[character] = 0 # Adding keys if they don't exist
        dictionary[character] += 1 # Adding values
    return dictionary

# Function to remove non-alphabetical symbols    
def remove_nonalph(char_dict):
    alpha_dict = {}
    for symbol in char_dict:
        if symbol.isalpha():
           alpha_dict[symbol] = char_dict[symbol]
        else:
            continue
    
    return alpha_dict

# Function to sort the results of number_of_characters(). Here we convers a dictionary in a list of dictionaries
def sorted_list(dictionary):
    char_dict = [] # List of dictionaries
    for pair in dictionary:
        sorted_list_item = {} # Dictionary item to combine in the result list
        sorted_list_item["char"] = pair
        sorted_list_item["num"] = dictionary[pair]
        char_dict.append(sorted_list_item)
    
    def sort_on(items):
        return items["num"]
    char_dict.sort(reverse=True, key=sort_on)
        
    return char_dict
