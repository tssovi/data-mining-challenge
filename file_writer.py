import random
import string
import os


# define a function for creating a string of random alphanumerical characters
def generate_random_alphanumerics_string():
    length = random.randint(5, 30)
    output_str = ''
    for _ in range(length):
        output_str += random.choice(string.ascii_lowercase + string.digits)
    return output_str

# define a function for creating a string of random alphabetical characters
def generate_random_alphabetical_string():
    length = random.randint(5, 30)
    output_str = ''.join(random.choice(string.ascii_lowercase) for x in range(length))
    return output_str

# define a function for creating a random integers and converting them to a string
def generate_random_integer_string():
    output_str = random.randint(0, 10000)
    output_str = '{}'.format(output_str)
    return output_str

# define a function for creating random real number and converting them to a string
def generate_random_real_number_string():
    length = random.randint(1, 10)
    output_str = round(random.uniform(0.0, 10000.0), length)
    output_str = '{}'.format(output_str)
    return output_str

# define a function to generate text file with random strings
def generate_text_file_with_random_strings():
    file_name = 'output_file.txt'
    open(file_name, 'w')
    file_size = os.stat(file_name).st_size

    with open(file_name, 'a') as text_file:
        # run the loop until file size reach 10 MB
        while file_size < 10485760:
            # put our functions into a list
            function_list = [
                generate_random_alphanumerics_string,
                generate_random_alphabetical_string,
                generate_random_integer_string,
                generate_random_real_number_string
            ]

            # randomly choose a function to generate string
            dataType = random.choice(function_list)

            if dataType == generate_random_alphanumerics_string:
                output_str = generate_random_alphanumerics_string()
                # whitespaces shouldn't be more than 9
                i = random.randint(0, 9)
                output_str = ' ' * i + output_str + ' ' * i
            else:
                output_str = dataType()
            text_file.write(output_str + ', ')
            file_size = os.stat(file_name).st_size
            print('Current file size is: {} MB\n'.format(file_size / 1000000))

        # once loop is done, print final file size and close file
        print('\nFinal file size is: {} MB\n'.format(file_size / 1000000))
        text_file.close()

generate_text_file_with_random_strings()