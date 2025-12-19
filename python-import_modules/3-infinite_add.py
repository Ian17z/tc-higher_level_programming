#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    soma = 0
    for i in range(1, len(sys.argv)):
        soma += int(sys.argv[i])
print(soma)
