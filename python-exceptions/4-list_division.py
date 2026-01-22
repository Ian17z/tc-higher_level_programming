#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    resultado = []
    for i in range(list_length):
        div = 0
        try:
            div = my_list_1[i] / my_list_2[i]
        except Exception as e:
            if isinstance(e, IndexError):
                print("out of range")
            elif isinstance(e, ZeroDivisionError):
                print("division by 0")
            elif isinstance(e, TypeError):
                print("wrong type")
        finally:
            resultado.append(div)
    return resultado
