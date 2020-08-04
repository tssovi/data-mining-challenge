# define a function to conver a text file to string
def file_to_text_converter():
    text = open("output_file.txt", "r")
    text = text.read()

    text = text.replace(" ", "")
    text = text.split(',')

    return text

# define a function to check if it is an integer or not
def is_int(word):
    try:
        int(word)
    except ValueError:
        return False
    return True

# define a function to check if it is a real number or not
def is_real_num(word):
    try: 
        float(word)
    except ValueError: 
        return False
    return True

# define a function to identify word types
def identify_string_type(text):
    text_words = ""
    str_type = ""

    for word in text:
        if is_int(word):
            str_type = 'integer'
        elif is_real_num(word):
            str_type = 'real numbers'
        elif word.isalpha():
            str_type = 'alphabetical strings'
        elif word.isalnum():
            str_type = 'alphanumeric'
        
        if word:
            text_words += word + ' - ' + str_type + '\n'
    
    return text_words


text = file_to_text_converter()

text_words = identify_string_type(text)

print(text_words)