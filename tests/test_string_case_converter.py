import pytest
from src.string_case_converter import convert_to_alternating_dot_case

def test_basic_conversion():
    assert convert_to_alternating_dot_case("hello world") == "hElLo.WoRlD"

def test_empty_string():
    assert convert_to_alternating_dot_case("") == ""

def test_single_character():
    assert convert_to_alternating_dot_case("a") == "a"

def test_multiple_spaces():
    assert convert_to_alternating_dot_case("hello  world") == "hElLo..WoRlD"

def test_mixed_case_input():
    assert convert_to_alternating_dot_case("HeLLo WoRLD") == "hElLo.WoRlD"

def test_special_characters():
    assert convert_to_alternating_dot_case("hello! world") == "hElLo!.WoRlD"

def test_invalid_input_type():
    with pytest.raises(TypeError):
        convert_to_alternating_dot_case(123)
    
    with pytest.raises(TypeError):
        convert_to_alternating_dot_case(None)