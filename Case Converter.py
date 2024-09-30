#takes a string in  cammel or pascal case as a parameter and converts it into snake case
def convert_to_snake_case(pascal_or_camel_cased_string):

    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]

    #joins all the characters in the list into one string with no '' inbetween 
    snake_cased_string = ''.join(snake_cased_char_list)

    #Removes any underscores from the start/end of the string 
    clean_snake_cased_string = snake_cased_string.strip('_')

    return clean_snake_cased_string



def main():
    print(convert_to_snake_case('aLongAndComplexString'))

main()