#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    numeros_romanos = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }  
    total = 0
    valor1 = 0
    for char in reversed(roman_string):
        valorreal = numeros_romanos[char]
        if valorreal < valor1:
            total -= valorreal
        else:
            total += valorreal    
        valor1 = valorreal    
    return total
