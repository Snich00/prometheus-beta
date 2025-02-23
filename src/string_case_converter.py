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
    start_with_lower = True  # Always start with lower case
    last_was_space = False
    
    for char in input_string:
        if char.isspace():
            result.append('.')
            last_was_space = True
            continue
        
        # Determine case: 
        # - If after a space, reset to lower
        # - Otherwise, alternate
        if last_was_space:
            start_with_lower = True
            last_was_space = False
        
        # Apply case based on flag
        if start_with_lower:
            transformed_char = char.lower()
        else:
            transformed_char = char.upper()
        
        result.append(transformed_char)
        start_with_lower = not start_with_lower
    
    return ''.join(result)