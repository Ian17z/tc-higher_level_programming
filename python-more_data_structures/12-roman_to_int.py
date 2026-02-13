#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    valores = {'I': 1, 'V': 5, 'X': 10,
              'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numeros = list(map(lambda c: values.get(c, 0), roman_string))

    return sum(
        -nums[i] if i + 1 < len(nums) and nums[i] < nums[i + 1]
        else nums[i]
        for i in range(len(nums))
    )
