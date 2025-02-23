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
    
    # Handle single character
    if len(input_string) == 1:
        return input_string.lower()
    
    # Convert to alternating dot case
    result = []
    needs_uppercase = True  # Always start with lowercase
    word_start = True
    
    for char in input_string:
        if char.isspace():
            result.append('.')
            needs_uppercase = True  # Reset to starting state
            word_start = True
            continue
        
        # Apply case based on specific requirements
        if word_start or needs_uppercase:
            transformed_char = char.lower()
            needs_uppercase = False
            word_start = False
        else:
            transformed_char = char.upper()
            needs_uppercase = True
        
        result.append(transformed_char)
    
    return ''.join(result)