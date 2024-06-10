import re
import ast

def extract_first_list_from_string(string):
    """
    Extracts the first list from a string containing list-like structures.

    Args:
    string (str): The input string.

    Returns:
    list or None: The first list extracted from the string, or None if no list is found.
    """
    pattern = r'\[.*?\]'  # Regular expression pattern to find the list portion
    match = re.search(pattern, string)  # Find the first list portion using regex

    if match:
        try:
            extracted_list = ast.literal_eval(match.group())  # Convert match to a list
            return extracted_list
        except ValueError:
            print("Invalid list format:", match.group())

    return None  # Return None if no list is found

if __name__ == "__main__":
    # Example usage:
    string_with_lists = "This is a list [1, 2, 3, 4, 5] and another list [6, 7, 8]"
    first_list = extract_first_list_from_string(string_with_lists)
    print("First Extracted List:", first_list)
