#  Write a Python class which has two methods get_String and print_String. The
# get_String accept a string from the user and print_String print the string in uppercase.

class StringManipulator:
    def __init__(self):
        self.input_string = ""

    def get_string(self):
        self.input_string = input("Enter a string: ")

    def print_string(self):
        print(self.input_string.upper())

string_obj = StringManipulator()
string_obj.get_string()
string_obj.print_string()
