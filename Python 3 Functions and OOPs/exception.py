try:
    x = int(input())
    if not 0 <= x <= 100:
        raise ValueError()
except ValueError as e:
    print('Erro')

try:
    x = input()
    if len(x) > 10:
        raise ValueError()
except ValueError as e:
    print('Erro')

try:
    f = open("demofile.txt", "r")
    print(f.read())
except Exception as e:
    print('File not found')

