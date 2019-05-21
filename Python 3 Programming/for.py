s = 'tata consultancy services limited'
count = 0
for contador in range(0,len(s)-1):
    if s[contador]=='a' or s[contador]=='e' or s[contador]=='i' or s[contador]=='o' or s[contador]=='u':
        count = count + 1
print(count)
