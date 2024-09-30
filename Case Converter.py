#takes a string in  cammel or pascal case as a parameter and converts it into snake case
def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = []

    #iterates over the string converting uppercase characters into lowercase
    #Adds an underscore before each converted character as they signify the start of a new word in camal and pascal case
    for char in pascal_or_camel_cased_string:

        #Condition to convert uppercase characters to lowercase
        #Adds character to a list after conversion 
        if char.isupper():
            converted_character = '_' + char.lower()
            snake_cased_char_list.append(converted_character)

        else:
            snake_cased_char_list.append(char)

    #joins all the characters in the list into one string with no '' inbetween 
    snake_cased_string = ''.join(snake_cased_char_list)

    #Removes any underscores from the start/end of the string 
    clean_snake_cased_string = snake_cased_string.strip('_')

    return clean_snake_cased_string



def main():
    print(convert_to_snake_case('aLongAndComplexString'))

main()