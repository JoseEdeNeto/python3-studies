s = 'tata consultancy services limited'
contador = len(s) - 1
count = 0
while contador >= 0:
    if s[contador]=='a' or s[contador]=='e' or s[contador]=='i' or s[contador]=='o' or s[contador]=='u':
        count = count + 1
    contador = contador - 1
print(count)
