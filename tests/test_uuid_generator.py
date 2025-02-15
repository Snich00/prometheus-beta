import re
import pytest
from src.uuid_generator import generate_uuid

def test_generate_uuid():
    """Test that the generate_uuid function produces a valid UUID."""
    # Generate a UUID
    generated_uuid = generate_uuid()
    
    # Check that the generated UUID is a string
    assert isinstance(generated_uuid, str), "UUID should be a string"
    
    # UUID v4 format regex pattern (8-4-4-4-12 hexadecimal format)
    uuid_pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$'
    
    # Check that the UUID matches the expected pattern
    assert re.match(uuid_pattern, generated_uuid, re.IGNORECASE), "UUID does not match the expected format"
    
def test_generate_uuid_uniqueness():
    """Test that multiple generated UUIDs are unique."""
    uuid_set = set()
    
    # Generate multiple UUIDs
    for _ in range(1000):
        new_uuid = generate_uuid()
        
        # Ensure no duplicate UUIDs
        assert new_uuid not in uuid_set, "Generated a duplicate UUID"
        uuid_set.add(new_uuid)