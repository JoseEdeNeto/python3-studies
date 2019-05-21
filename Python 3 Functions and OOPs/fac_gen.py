def fac_gen():
    a = 0
    while True:
        b = 1
        for i in range(a, 0, -1):
            b = b * i
        yield b
        a = a + 1

fs = fac_gen()

print(next(fs))
print(next(fs))
print(next(fs))
print(next(fs))
print(next(fs))
print(next(fs))