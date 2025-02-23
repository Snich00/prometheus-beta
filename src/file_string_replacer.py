"""
Module for replacing strings in files.
"""

def replace_string_in_file(file_path, old_string, new_string):
    """
    Replace all occurrences of a given string in a file.

    Args:
        file_path (str): Path to the file to be modified.
        old_string (str): The string to be replaced.
        new_string (str): The string to replace with.

    Returns:
        int: Number of replacements made.

    Raises:
        TypeError: If any argument is not a string.
        FileNotFoundError: If the file does not exist.
        PermissionError: If there are insufficient permissions to read/write the file.
    """
    # Type checking
    if not all(isinstance(arg, str) for arg in [file_path, old_string, new_string]):
        raise TypeError("All arguments must be strings")

    # Check if old_string is empty
    if not old_string:
        raise ValueError("Old string cannot be empty")

    # Read the file contents
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_contents = file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except PermissionError:
        raise PermissionError(f"Permission denied when reading file: {file_path}")

    # Count and replace occurrences
    replacements = file_contents.count(old_string)
    modified_contents = file_contents.replace(old_string, new_string)

    # Write back to the file
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(modified_contents)
    except PermissionError:
        raise PermissionError(f"Permission denied when writing to file: {file_path}")

    return replacements