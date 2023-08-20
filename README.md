# tinyfrog

A networking library that simplifies common networking tasks, such as making HTTP requests,
and adds some useful features, such as retrying requests.

## Installation

```bash
pip install tinyfrog
```

## Usage

```python
import tinyfrog

# Make a GET request with retrying
response = tinyfrog.get_with_retries("https://example.com")


```

## License
Gnu GPL v3.0
