# tinyfrog

A Python library for creating and manipulating [TinyFrog]() files.

## Installation

```bash
pip install tinyfrog
```

## Usage

```python
import tinyfrog

# Create a new TinyFrog file
frog = tinyfrog.TinyFrog()

# Add a new entry
frog.add_entry("Hello, world!")

# Save the file
frog.save("hello.frog")

# Load the file
frog = tinyfrog.TinyFrog("hello.frog")

# Print the contents
print(frog.entries[0])
```

## License
Gnu GPL v3.0
