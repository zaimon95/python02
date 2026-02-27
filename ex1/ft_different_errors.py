#!/usr/bin/env python3

def garden_operations():
    try:

    except ValueError as e:
        raise
        print(f"Caught ValueError: {e} invalid literal for int()")
    except ZeroDivisionError as e:
        raise
        print(f"Caught ZeroDivisionError: {e} division by zero")
    except FileNotFoundError as e:
        raise
        print(f"Caught FileNotFoundError: {e} No such file 'missing.txt'")
    except KeyError as e:
        raise
        print(f"Caught KeyError: {e} 'missing\\_plant'")
