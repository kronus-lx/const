# Const

Const type for Python that wraps a value and throws a runtime error if attempts to override it.

Like C/C++ style const keyword, the const class will prevent the user from re-assigning the value once set.

## Example

Using pi as an example, the value of pi must always be 3.14159, so attempts to override this in runtime must be prohibited. This can be strictly enforced by wrapping in the const class 

```python
# Example usage of the const class

# Create an instance with an initial attribute
constant = const('pi', 3.14159)

# Attempt to print the current state
print(constant.release())  # Output: {'pi': 3.14159}

# Attempt to add another attribute (should raise RuntimeError)
try:
    constant.e = 2.71828
except RuntimeError as e:
    print(e)  # Output: Instance cannot contain more than one attribute

# Attempt to reassign the existing attribute (should raise RuntimeError)
try:
    constant.pi = 3.14
except RuntimeError as e:
    print(e)  # Output: Cannot reassign const attribute: pi

# Clear the content of the object
del constant
```