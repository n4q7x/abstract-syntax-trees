#!/usr/bin/env python3
"""
Simple tests for the Ontologica parser
"""

import sys
from ontologica import OntologyParser


def test_entity_declaration():
    """Test entity declaration parsing"""
    parser = OntologyParser()
    parser.parse_line("A thing is mathematics.")
    assert "mathematics" in parser.entities
    print("✓ test_entity_declaration passed")


def test_predicate_declaration():
    """Test predicate declaration parsing"""
    parser = OntologyParser()
    parser.parse_line("A thing is mathematics.")
    parser.parse_line("A thing about mathematics is what it is.")
    assert "mathematics" in parser.predicates
    assert "what it is" in parser.predicates["mathematics"]
    print("✓ test_predicate_declaration passed")


def test_value_assignment():
    """Test value assignment parsing"""
    parser = OntologyParser()
    parser.parse_line("A thing is mathematics.")
    parser.parse_line("A thing about mathematics is what it is.")
    parser.parse_line("mathematics what it is a formal science")
    
    values = parser.values.get(("mathematics", "what it is"), [])
    assert len(values) == 1
    assert "a formal science" in values[0]
    print("✓ test_value_assignment passed")


def test_closure_detection():
    """Test detection of unclosed predicates"""
    parser = OntologyParser()
    parser.parse_line("A thing is mathematics.")
    parser.parse_line("A thing about mathematics is what it is.")
    parser.parse_line("A thing about mathematics is what it's used for.")
    parser.parse_line("mathematics what it is a formal science")
    
    unclosed = parser.check_closure()
    assert "mathematics" in unclosed
    assert "what it's used for" in unclosed["mathematics"]
    assert "what it is" not in unclosed["mathematics"]
    print("✓ test_closure_detection passed")


def test_file_parsing():
    """Test parsing a complete file"""
    parser = OntologyParser()
    parser.parse_file("example.ont")
    
    assert "first-order logic" in parser.entities
    assert "theories" in parser.entities
    assert "formulae" in parser.entities
    
    unclosed = parser.check_closure()
    assert len(unclosed) == 0, "All predicates should be closed in example.ont"
    print("✓ test_file_parsing passed")


def test_unclosed_file():
    """Test parsing a file with unclosed predicates"""
    parser = OntologyParser()
    parser.parse_file("example-unclosed.ont")
    
    unclosed = parser.check_closure()
    assert "mathematics" in unclosed
    assert "what it's used for" in unclosed["mathematics"]
    print("✓ test_unclosed_file passed")


def run_tests():
    """Run all tests"""
    print("\nRunning Ontologica tests...\n")
    
    tests = [
        test_entity_declaration,
        test_predicate_declaration,
        test_value_assignment,
        test_closure_detection,
        test_file_parsing,
        test_unclosed_file,
    ]
    
    failed = 0
    for test in tests:
        try:
            test()
        except Exception as e:
            print(f"✗ {test.__name__} failed: {e}")
            failed += 1
    
    print(f"\n{'='*50}")
    print(f"Tests run: {len(tests)}")
    print(f"Passed: {len(tests) - failed}")
    print(f"Failed: {failed}")
    print(f"{'='*50}\n")
    
    return failed == 0


if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)
