# Package Sorting System

This project defines a package sorting system that categorizes packages into three types based on their volume and mass:

- **STANDARD**: Packages that are neither bulky nor heavy.
- **SPECIAL**: Packages that are either bulky or heavy.
- **REJECTED**: Packages that are both bulky and heavy.
- **INVALID**: Packages with invalid dimensions or mass.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Code Structure](#code-structure)
- [License](#license)

## Overview

This Python program provides a function `sort(width, height, length, mass)` that sorts packages based on:
- Volume (calculated by multiplying width, height, and length).
- Mass (weight of the package).

The categorization is based on:
- **Bulky**: If the volume is greater than or equal to 1,000,000 cm³, or any dimension (width, height, length) is greater than or equal to 150 cm.
- **Heavy**: If the mass is greater than or equal to 20 kg.
  
The packages are classified into the following categories:
- **STANDARD**: If the package is neither bulky nor heavy.
- **SPECIAL**: If the package is either bulky or heavy.
- **REJECTED**: If the package is both bulky and heavy.
- **INVALID**: If any input is invalid (non-positive dimensions or mass).

## Installation

You don't need any special dependencies to run this project, as it is written in plain Python. To set up the project:

1. Clone the repository:
   ```bash
   git clone https://github.com/romulogatto/thoughtful-test.git
   cd thoughtful-test
   ```

## Usage

The main function to sort the packages is `sort(width, height, length, mass)`, which returns one of the following stack types:

- `STANDARD`: For packages that are neither bulky nor heavy.
- `SPECIAL`: For packages that are either bulky or heavy.
- `REJECTED`: For packages that are both bulky and heavy.
- `INVALID`: For packages with invalid dimensions or mass.

### Example Usage:

```python
from app import sort

# Sort a normal package
result = sort(10.0, 10.0, 10.0, 5.0)
print(result)  # Output: STANDARD

# Sort a bulky package
result = sort(200.0, 200.0, 5.0, 10.0)
print(result)  # Output: SPECIAL

# Sort a heavy package
result = sort(50.0, 50.0, 50.0, 25.0)
print(result)  # Output: SPECIAL

# Sort a bulky and heavy package
result = sort(200.0, 200.0, 200.0, 30.0)
print(result)  # Output: REJECTED
```

## Testing

We use Python's built-in `unittest` framework to test the package sorting logic. The tests cover various scenarios, including:

- Standard packages
- Bulky packages
- Heavy packages
- Invalid inputs (negative or zero dimensions or mass)
- Edge cases (bulky but not heavy, heavy but not bulky)

### To run tests:

1. Make sure you're in the project directory.
2. Run the following command:
   ```bash
   python -m unittest app_test.py
   ```

## Code Structure

- **`app.py`**: Contains the logic for sorting the packages based on their volume and mass.
- **`app_test.py`**: Contains the unit tests for verifying the functionality of the sorting system.
- **`README.md`**: This file.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
