"""
Tests for the file string replacer function.
"""

import os
import pytest
from src.file_string_replacer import replace_string_in_file

def test_replace_string_in_file(tmp_path):
    # Create a test file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Hello world! Hello universe!")

    # Replace string
    replacements = replace_string_in_file(str(test_file), "Hello", "Hi")

    # Check replacements and content
    assert replacements == 2
    assert test_file.read_text() == "Hi world! Hi universe!"

def test_replace_with_empty_new_string(tmp_path):
    # Create a test file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Hello world!")

    # Replace string with empty string
    replacements = replace_string_in_file(str(test_file), "world", "")

    # Check replacements and content
    assert replacements == 1
    assert test_file.read_text() == "Hello !"

def test_no_replacements(tmp_path):
    # Create a test file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Hello world!")

    # Try to replace non-existent string
    replacements = replace_string_in_file(str(test_file), "universe", "galaxy")

    # Check replacements and content
    assert replacements == 0
    assert test_file.read_text() == "Hello world!"

def test_invalid_input_types():
    # Test type errors
    with pytest.raises(TypeError):
        replace_string_in_file(123, "old", "new")
    with pytest.raises(TypeError):
        replace_string_in_file("file.txt", 123, "new")
    with pytest.raises(TypeError):
        replace_string_in_file("file.txt", "old", 123)

def test_empty_old_string():
    # Test empty old string
    with pytest.raises(ValueError):
        replace_string_in_file("file.txt", "", "new")

def test_nonexistent_file():
    # Test non-existent file
    with pytest.raises(FileNotFoundError):
        replace_string_in_file("nonexistent_file.txt", "old", "new")