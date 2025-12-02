# Ontologica - Plaintext Ontology Parser

A Python program that parses plaintext ontology declarations and validates their structure. This implementation brings to life the ontology specification described in the `envisioning-ontologica` file.

## Overview

Ontologica allows you to define formal ontologies using simple English-like statements. It tracks:
- **Entities**: Things that exist in your ontology
- **Predicates**: Properties or relationships that entities can have
- **Values**: Specific assertions about entity predicates

The program validates that:
1. All declared predicates are "closed" (have at least one value)
2. Predicates can be marked as complete or incomplete

## Syntax

### Entity Declaration
```
A thing is <entity-name>.
```
Example: `A thing is first-order logic.`

### Predicate Declaration
```
A thing about <entity-name> is <predicate>.
```
Example: `A thing about first-order logic is what it's like.`

### Value Assignment
```
<entity-name> <predicate> <value>
```
Example: `first-order logic what it's like a formal language`

### Comments
Lines starting with `#` are treated as comments and ignored.

## Usage

### Basic Usage
```bash
python3 ontologica.py <ontology-file>
```

This will:
1. Parse the ontology file
2. Display the status of all entities and predicates
3. Report any unclosed predicates
4. Show a summary

### Interactive Mode
```bash
python3 ontologica.py <ontology-file> --interactive
```

Interactive mode asks you to confirm whether each predicate is complete after showing its current values.

## Examples

### Example 1: Basic Ontology (`example.ont`)

```
A thing is first-order logic.
A thing about first-order logic is what it is.
A thing about first-order logic is what it's like.

first-order logic what it is a formal system
first-order logic what it's like a formal language
```

Running: `python3 ontologica.py example.ont`

Output shows all predicates are closed and provides a summary.

### Example 2: Unclosed Predicates (`example-unclosed.ont`)

```
A thing is mathematics.
A thing about mathematics is what it is.
A thing about mathematics is what it's used for.

mathematics what it is a formal science
# Note: "what it's used for" has no value
```

Running this will report that the predicate "what it's used for" is not closed.

## Features

### Closure Detection
The program automatically detects predicates that have been declared but have no values. These are called "unclosed" predicates. At least one value must be provided for each predicate.

### Completeness Checking
In interactive mode, you can mark whether each predicate is complete (has all the values it should have) or incomplete (needs more values).

### Status Reporting
The program provides:
- List of all entities
- List of all predicates and their value counts
- Warnings for unclosed predicates
- Summary statistics

## Implementation Details

The parser uses regular expressions to match the three main statement patterns:
1. Entity declarations
2. Predicate declarations  
3. Value assignments

The ontology data is stored in:
- `entities`: Set of entity names
- `predicates`: Dictionary mapping entities to their predicates
- `values`: Dictionary mapping (entity, predicate) pairs to lists of values
- `complete_predicates`: Dictionary tracking completeness status

## Files in This Repository

- `ontologica.py` - Main implementation of the ontology parser
- `example.ont` - Complete ontology example with all predicates closed
- `example-unclosed.ont` - Example demonstrating unclosed predicate detection
- `envisioning-ontologica` - Original specification document
- `ONTOLOGICA.md` - This documentation file

## Future Enhancements

Possible extensions to this implementation:
- Support for queries on the ontology
- Export to other formats (JSON, RDF, etc.)
- Validation rules and constraints
- Inference engine for deriving new facts
- Graphical visualization of the ontology structure
- More sophisticated predicate matching algorithms

## Origin

This implementation is based on the specification described in the `envisioning-ontologica` file, which envisions a plaintext program for building formal ontologies with interactive validation.
