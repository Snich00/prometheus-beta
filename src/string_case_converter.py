def convert_to_alternating_dot_case(input_string):
    """
    Convert a string to alternating dot case.

    Args:
        input_string (str): The input string to be converted.

    Returns:
        str: The string converted to alternating dot case.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string
    if not input_string:
        return ""
    
    # Convert to alternating dot case
    result = []
    for i, char in enumerate(input_string):
        # Lowercase or uppercase based on index
        if i % 2 == 0:
            transformed_char = char.lower()
        else:
            transformed_char = char.upper()
        
        # Replace spaces with dots
        if transformed_char.isspace():
            result.append('.')
        else:
            result.append(transformed_char)
    
    return ''.join(result)