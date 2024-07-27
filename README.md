#Python Decorator Library

##A collection of Python decorators for various functionalities.

**Description**

This repository contains a set of Python decorators that can be used to enhance function behavior:

- **dt_check:** Checks if function arguments are of a specified type.
- **dt_convert:** Attempts to convert function arguments to a specified type.
- **timer:** Measures the execution time of a function.
- **count:** Counts the number of times a function is called.
- **ncalls:** Limits the number of times a function can be called.
- **bypass:** Silently catches and logs exceptions from a function.


**Installation:**

This project doesn't require any external dependencies. Simply clone or download the repository and use the `Decorator` class directly in your Python code.

**Use this git command to clone this repo**
```
git clone https://github.com/Sailor200/Decorators.git
```

**Usage Example:**

```python
from decorators import dt_check, dt_convert, timer, count, ncalls, bypass

# Example usage:
@dt_check(int)
def add(x, y):
    return x + y

@timer
@count
def my_function(a, b):
    time.sleep(0.5)
    return a * b

```

**Further Enhancements:**

- Expand type checking capabilities in dt_check to include more complex type structures.
- Implement additional type conversion options in dt_convert.
- Provide more granular control over exception handling in bypass.
- Develop decorators for caching, rate limiting, and other common use cases.

**Contribution:**

Feel free to fork this repository, make improvements, and submit issues or pull requests to contribute to the project's development.

**License**:

This project is licensed under the [MIT License](https://opensource.org/license/MIT).
