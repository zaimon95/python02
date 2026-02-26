#!/usr/bin/env python3

def garden_operations():
    a = 3
    text = int("ABC")
    value = my_dict.get('key', 'default')
    try:
        b = a / 0
        print(test)
        value = my_dict['key']
        open("missing.txt")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    except KeyError:
        print("Caught KeyError: 'missing\_plant'")


