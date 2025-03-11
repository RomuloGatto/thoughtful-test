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
