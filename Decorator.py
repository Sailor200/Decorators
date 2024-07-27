import time


def dt_check(dt: type = str, error: bool = True):
    """
    Checks if input arguments are of a specified type.

        Args:
            dt: The expected type (default value: dt = str).
            error: If True, raises a TypeError for type mismatches, otherwise prints a warning (default value: error = True).

        Returns:
            A decorator that checks the types of arguments.
        """
    def outer_wrapper(f):
        def inner_wrapper(*a):
            for i in a:
                if not isinstance(i, dt):
                    if error:
                        raise TypeError(f'Expected type {dt}, but got {type(i).__name__}')
                    else:
                        print("Function call is not executed due to mismatch of DT")
                        return
            return f(*a)

        return inner_wrapper

    return outer_wrapper


def dt_convert(dt: type = str):
    """
    Attempts to convert input arguments to a specified type.

        Args:
            dt: The target type for conversion (default value: dt = str).

        Returns:
            A decorator that attempts to convert arguments.
    """
    def outer_wrapper(f):
        def inner_wrapper(*a):
            try:
                ah = [dt(i) for i in a]
                return f(*ah)
            except Exception as e:
                print(f"Error:{e} \nFunction couldn't be executed")

        return inner_wrapper

    return outer_wrapper


def timer(f):
    """
    Measures the execution time of a function.

        Args:
            f: The function to be timed.

        Returns:
            A decorator that measures the execution time and prints the result.

    """
    def wrapper(*a):
        k = time.perf_counter()
        h = f(*a)
        print(f"time taken to execute this function is: {time.perf_counter() - k:.6f} seconds")
        return h

    return wrapper


def count(f):
    """
    Counts the number of times a function is called.

        Args:
            f: The function to be counted.

        Returns:
        A decorator that counts the number of function calls and prints the result.
    """
    k = 0

    def wrapper(*a):
        nonlocal k
        k += 1
        h = f(*a)
        print(f"this function {f.__name__} is called for {k} times")
        return h

    return wrapper


def ncalls(n: int, error: bool = True):
    """
    Limits the number of times a function can be called.

        Args:
            n: The maximum number of allowed calls.
            error: If True, raises an exception when the call limit is exceeded, otherwise prints a warning.

        Returns:
            A decorator that limits the number of function calls.
    """
    if n <= 0:
        raise ValueError("Number of calls must be greater than 0")

    def outer_wrapper(f):
        call_count = 0

        def inner_wrapper(*a):
            nonlocal call_count
            if call_count >= n:
                if error:
                    raise Exception("No. of calls exceeded")
                else:
                    print("No. of calls exceeded")
                    return
            call_count += 1
            return f(*a)

        return inner_wrapper

    return outer_wrapper


def bypass(f):
    """
    Silently catches exceptions from a function.

        Args:
            f: The function to be wrapped.

        Returns:
            A decorator that catches exceptions.
    """
    def wrapper(*a):
        try:
            return f(*a)
        except Exception as e:
            print(f"Error in {f.__name__} : {type(e).__name__} => {str(e)}")
            return None
    return wrapper
