#!/usr/bin/env python3
"""
Ontologica - A plaintext ontology parser and validator

This program parses plaintext ontology declarations and tracks entities,
predicates, and their values. It validates that predicates are "closed"
(have at least one value) and can interactively check for completeness.
"""

import re
import sys
from collections import defaultdict
from typing import Dict, Set, List, Tuple


class OntologyParser:
    """Parser for plaintext ontology declarations"""
    
    def __init__(self):
        self.entities: Set[str] = set()
        self.predicates: Dict[str, Set[str]] = defaultdict(set)  # entity -> set of predicates
        self.values: Dict[Tuple[str, str], List[str]] = defaultdict(list)  # (entity, predicate) -> list of values
        self.complete_predicates: Dict[Tuple[str, str], bool] = {}  # (entity, predicate) -> is_complete
        
    def parse_file(self, filename: str):
        """Parse an ontology file"""
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        for line_num, line in enumerate(lines, 1):
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            
            try:
                self.parse_line(line)
            except Exception as e:
                print(f"Warning: Could not parse line {line_num}: {line}", file=sys.stderr)
                print(f"  Error: {e}", file=sys.stderr)
    
    def parse_line(self, line: str):
        """Parse a single line of ontology declaration"""
        # Pattern 1: "A thing is <entity>."
        match = re.match(r'^A thing is (.+)\.$', line, re.IGNORECASE)
        if match:
            entity = match.group(1).strip()
            self.entities.add(entity)
            return
        
        # Pattern 2: "A thing about <entity> is <predicate>."
        match = re.match(r'^A thing about (.+?) is (.+)\.$', line, re.IGNORECASE)
        if match:
            entity = match.group(1).strip()
            predicate = match.group(2).strip()
            self.predicates[entity].add(predicate)
            return
        
        # Pattern 3: "<entity> <predicate> <value>"
        # This is more complex as we need to find where the predicate starts
        # We'll try to match known predicates
        for entity in self.entities:
            if line.lower().startswith(entity.lower()):
                rest = line[len(entity):].strip()
                for predicate in self.predicates.get(entity, []):
                    if rest.lower().startswith(predicate.lower()):
                        value = rest[len(predicate):].strip()
                        if value:
                            self.values[(entity, predicate)].append(value)
                            return
    
    def check_closure(self) -> Dict[str, List[str]]:
        """Check which predicates are not closed (have no values)"""
        unclosed = defaultdict(list)
        
        for entity, predicates in self.predicates.items():
            for predicate in predicates:
                if not self.values.get((entity, predicate)):
                    unclosed[entity].append(predicate)
        
        return dict(unclosed)
    
    def print_status(self):
        """Print the current status of the ontology"""
        print("\n=== Ontology Status ===\n")
        
        print(f"Entities declared: {len(self.entities)}")
        for entity in sorted(self.entities):
            print(f"  - {entity}")
        
        print(f"\nPredicates declared: {sum(len(preds) for preds in self.predicates.values())}")
        for entity in sorted(self.predicates.keys()):
            predicates = self.predicates[entity]
            print(f"  {entity}:")
            for predicate in sorted(predicates):
                values = self.values.get((entity, predicate), [])
                status = f"{len(values)} value(s)" if values else "NO VALUES (not closed)"
                print(f"    - {predicate}: {status}")
        
        print()
    
    def check_completeness_interactive(self):
        """Interactively check if predicates are complete"""
        print("\n=== Completeness Check ===\n")
        
        for entity in sorted(self.predicates.keys()):
            print(f"\nEntity: {entity}")
            for predicate in sorted(self.predicates[entity]):
                values = self.values.get((entity, predicate), [])
                if not values:
                    print(f"  Predicate '{predicate}' has no values (not closed)")
                    continue
                
                print(f"  Predicate: {predicate}")
                print(f"  Values:")
                for value in values:
                    print(f"    - {value}")
                
                response = input(f"  Is this predicate complete? (y/n): ").strip().lower()
                self.complete_predicates[(entity, predicate)] = response == 'y'
    
    def report(self):
        """Generate a comprehensive report of the ontology"""
        print("\n=== Ontology Report ===\n")
        
        # Check closure
        unclosed = self.check_closure()
        if unclosed:
            print("⚠️  PREDICATES NOT CLOSED (need at least one value):\n")
            for entity, predicates in unclosed.items():
                print(f"  Entity: {entity}")
                for predicate in predicates:
                    print(f"    - {predicate}")
            print()
        else:
            print("✓ All predicates are closed (have at least one value)\n")
        
        # Check completeness
        incomplete = []
        for (entity, predicate), is_complete in self.complete_predicates.items():
            if not is_complete:
                incomplete.append((entity, predicate))
        
        if incomplete:
            print("⚠️  PREDICATES MARKED AS INCOMPLETE:\n")
            for entity, predicate in incomplete:
                print(f"  {entity} / {predicate}")
            print()
        elif self.complete_predicates:
            print("✓ All checked predicates are marked as complete\n")
        
        # Summary
        print("Summary:")
        print(f"  Entities: {len(self.entities)}")
        print(f"  Predicates: {sum(len(preds) for preds in self.predicates.values())}")
        print(f"  Values: {sum(len(vals) for vals in self.values.values())}")
        if unclosed:
            print(f"  Unclosed predicates: {sum(len(preds) for preds in unclosed.values())}")
        if incomplete:
            print(f"  Incomplete predicates: {len(incomplete)}")


def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("Usage: python ontologica.py <ontology-file> [--interactive]")
        print("\nExample:")
        print("  python ontologica.py example.ont")
        print("  python ontologica.py example.ont --interactive")
        sys.exit(1)
    
    filename = sys.argv[1]
    interactive = '--interactive' in sys.argv
    
    parser = OntologyParser()
    
    print(f"Parsing ontology file: {filename}")
    parser.parse_file(filename)
    
    parser.print_status()
    
    if interactive:
        parser.check_completeness_interactive()
    
    parser.report()


if __name__ == '__main__':
    main()
